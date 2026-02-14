from fastapi import FastAPI
from app.database import engine, Base
from app.routers import products, categories  # Добавили categories

# Создаём таблицы в БД
Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI Shop")

# Подключаем роутеры
app.include_router(products.router)
app.include_router(categories.router)  # Добавили

@app.get("/")
def root():
    return {"message": "FastAPI Shop with Categories is running!"}

from app.admin import admin
