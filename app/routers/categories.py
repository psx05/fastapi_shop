from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import crud, schemas
from app.database import get_db

router = APIRouter(
    prefix="/categories",
    tags=["categories"]
)

# GET /categories — быстрый список без товаров
@router.get("/", response_model=List[schemas.Category])
def read_categories(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    categories = crud.get_categories(db, skip=skip, limit=limit)
    return categories

# GET /categories/{id} — категория с товарами
@router.get("/{category_id}", response_model=schemas.CategoryWithProducts)
def read_category(category_id: int, db: Session = Depends(get_db)):
    db_category = crud.get_category(db, category_id=category_id)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return db_category

@router.post("/", response_model=schemas.Category)
def create_category(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    db_category = crud.get_category_by_name(db, name=category.name)
    if db_category:
        raise HTTPException(status_code=400, detail="Category already exists")
    return crud.create_category(db, category=category)

@router.delete("/{category_id}", response_model=schemas.Category)
def delete_category(category_id: int, db: Session = Depends(get_db)):
    db_category = crud.delete_category(db, category_id=category_id)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return db_category

@router.put("/{product_id}/category/{category_id}", response_model=schemas.Product)
def update_product_category(product_id: int, category_id: int, db: Session = Depends(get_db)):
    db_product = crud.update_product_category(db, product_id=product_id, category_id=category_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product or Category not found")
    return db_product