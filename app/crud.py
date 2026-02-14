from sqlalchemy.orm import Session
from sqlalchemy import select
from app import models, schemas

# ---------- Category CRUD ----------
def get_categories(db: Session, skip: int = 0, limit: int = 100):
    try:
        print(">>> get_categories called")

        # Проверим подключение к БД
        from sqlalchemy import text
        db.execute(text("SELECT 1"))
        print(">>> DB connection OK")

        # Выполним запрос
        categories = db.query(models.Category).offset(skip).limit(limit).all()
        print(f">>> Found {len(categories)} categories")

        # Вернём результат
        return categories

    except Exception as e:
        print(f"!!!---> CRASH: {type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()
        # Временно вернём пустой список, чтобы сервер не падал
        return []

def get_category(db: Session, category_id: int):
    return db.query(models.Category).filter(models.Category.id == category_id).first()

def get_category_by_name(db: Session, name: str):
    return db.query(models.Category).filter(models.Category.name == name).first()

def create_category(db: Session, category: schemas.CategoryCreate):
    db_category = models.Category(**category.dict())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def delete_category(db: Session, category_id: int):
    db_category = db.query(models.Category).filter(models.Category.id == category_id).first()
    if db_category:
        db.delete(db_category)
        db.commit()
    return db_category

# ---------- Product CRUD (обновленный) ----------
def get_products(db: Session, skip: int = 0, limit: int = 100, category_id: Optional[int] = None):
    query = db.query(models.Product)
    if category_id:
        query = query.filter(models.Product.category_id == category_id)
    return query.offset(skip).limit(limit).all()

def get_product(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.id == product_id).first()

def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def update_product_category(db: Session, product_id: int, category_id: int):
    db_product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if db_product:
        db_product.category_id = category_id
        db.commit()
        db.refresh(db_product)
    return db_product