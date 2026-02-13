from fastapi import FastAPI
from app.database import engine, Base
from app.routers import products

# Создаём таблицы в базе данных
Base.metadata.create_all(bind=engine)

# СОЗДАЁМ ПРИЛОЖЕНИЕ — ЭТО СТРОКА ВАЖНЕЕ ВСЕХ!
app = FastAPI(title="FastAPI Shop")

# Подключаем роутеры
app.include_router(products.router)

@app.get("/")
def root():
    return {"message": "FastAPI Shop is running!"}
