from pydantic import BaseModel
from typing import Optional, List, ForwardRef
from datetime import datetime
from typing import Optional

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

# ---------- User Schemas ----------
class UserBase(BaseModel):
    email: str
    username: str

class UserCreate(UserBase):
    password: str  # пароль приходит от клиента

class User(UserBase):
    id: int
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True  # orm_mode в новых версиях Pydantic

class UserInDB(User):
    hashed_password: str  # для внутреннего использования

# ---------- Token Schemas ----------
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None