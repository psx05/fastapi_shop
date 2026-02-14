from pydantic import BaseModel
from typing import Optional, List, ForwardRef

# Используем ForwardRef для корректных ссылок
ProductRef = ForwardRef("Product")


# ---------- Category Schemas ----------
class CategoryBase(BaseModel):
    name: str
    description: Optional[str] = None


class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase):
    id: int

    class Config:
        orm_mode = True


# Отдельная схема для категории с товарами (для GET /categories/{id})
class CategoryWithProducts(CategoryBase):
    id: int
    products: List["Product"] = []  # ← здесь товары есть, но используется только где нужно

    class Config:
        orm_mode = True


# ---------- Product Schemas ----------
class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    stock: int
    category_id: Optional[int] = None


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    id: int
    category: Optional[Category] = None

    class Config:
        orm_mode = True


# Обновляем ссылки
from .schemas import Product

CategoryWithProducts.model_rebuild()
Product.model_rebuild()