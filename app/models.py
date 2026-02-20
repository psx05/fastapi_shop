from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime
from sqlalchemy import Boolean, DateTime


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    description = Column(Text)

    # Связь с товарами (один ко многим)
    products = relationship("Product", back_populates="category")


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(Text)
    price = Column(Float)
    stock = Column(Integer)

    # Внешний ключ на категорию
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=True)

    # Связь с категорией
    category = relationship("Category", back_populates="products")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Связи (потом добавим корзину и заказы)
    # cart = relationship("Cart", back_populates="user")
    # orders = relationship("Order", back_populates="user")