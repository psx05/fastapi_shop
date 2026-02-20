from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from app.database import engine, Base
from app.routers import products, categories, auth

# Создаём таблицы в БД
Base.metadata.create_all(bind=engine)

# Создаём приложение FastAPI
app = FastAPI(
    title="FastAPI Shop",
    description="Интернет-магазин на FastAPI + PostgreSQL",
    version="1.0.0"
)

# Настройка CORS (для фронтенда)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # В продакшене заменить на конкретные домены
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Подключаем роутеры API
app.include_router(products.router)
app.include_router(categories.router)
app.include_router(auth.router)

# Подключаем шаблоны (для HTML страниц)
templates = Jinja2Templates(directory="templates")

# ----- HTML СТРАНИЦЫ -----

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Главная страница магазина"""
    return templates.TemplateResponse(
        "shop.html",
        {"request": request}
    )

@app.get("/register", response_class=HTMLResponse)
async def register_page(request: Request):
    """Страница регистрации"""
    return templates.TemplateResponse(
        "register.html",
        {"request": request}
    )

@app.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    """Страница входа"""
    return templates.TemplateResponse(
        "login.html",
        {"request": request}
    )

# ----- API ЭНДПОИНТЫ (JSON) -----

@app.get("/api/health")
async def health_check():
    """Проверка работоспособности сервера"""
    return {"status": "healthy", "message": "FastAPI Shop is running!"}

# Подключаем админку (SQLAdmin)
from app.admin import admin
# admin уже инициализирован в app/admin.py и подключён