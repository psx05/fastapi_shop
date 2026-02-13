<h1 align="center">🛒 FastAPI Shop</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.14+-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.14">
  <img src="https://img.shields.io/badge/FastAPI-0.115+-green?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI">
  <img src="https://img.shields.io/badge/PostgreSQL-18-blue?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL 18">
  <img src="https://img.shields.io/badge/SQLAlchemy-2.0-red?style=for-the-badge&logo=sqlalchemy&logoColor=white" alt="SQLAlchemy">
  <img src="https://img.shields.io/badge/Status-In%20Development-orange?style=for-the-badge" alt="Status">
</p>

<p align="center">
  <b>⚡ Интернет-магазин на самых современных версиях Python ⚡</b>
</p>

<p align="center">
  <i>Будущее уже здесь — бэкенд для интернет-магазина на Python 3.14 и PostgreSQL 18</i>
</p>

---

## 🌟 Ключевые особенности

### 🚀 Технологический стек будущего

| Технология | Версия | Почему это круто |
|------------|--------|------------------|
| **Python** | 3.14+ | Ультрасовременный синтаксис, JIT-компиляция, скорость как у C |
| **PostgreSQL** | 18 | Новейший движок БД с поддержкой JSONB super-powers |
| **FastAPI** | 0.115+ | Асинхронность из коробки, автодокументация |
| **SQLAlchemy** | 2.0+ | Современный ORM с асинхронными возможностями |

### ✅ Реализовано сейчас

- **Товары** — полный CRUD с пагинацией и фильтрацией
- **50+ тестовых товаров** — ноутбуки, мыши, клавиатуры и т.д.
- **PostgreSQL 18** — самая свежая версия
- **Python 3.14** — используем новейшие фичи языка
- **SQLAlchemy 2.0** — асинхронные запросы к БД

### 🔜 Скоро появится

- [ ] Категории товаров (many-to-many)
- [ ] JWT авторизация (Python 3.14 + криптография)
- [ ] Корзина покупок (асинхронная)
- [ ] Заказы с транзакциями
- [ ] Docker + docker-compose
- [ ] CI/CD через GitHub Actions
- [ ] Alembic миграции

---

## 🛠️ Технологический стек

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.14-3776AB?style=flat-square&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/FastAPI-0.115-009688?style=flat-square&logo=fastapi&logoColor=white" />
  <img src="https://img.shields.io/badge/PostgreSQL-18-316192?style=flat-square&logo=postgresql&logoColor=white" />
  <img src="https://img.shields.io/badge/SQLAlchemy-2.0-D71F00?style=flat-square&logo=sqlalchemy&logoColor=white" />
  <img src="https://img.shields.io/badge/Pydantic-2.9-E92063?style=flat-square&logo=pydantic&logoColor=white" />
  <img src="https://img.shields.io/badge/Uvicorn-0.30-2334A9?style=flat-square&logo=uvicorn&logoColor=white" />
</p>

| Компонент | Версия | Назначение |
|-----------|--------|------------|
| **Python** | 3.14+ | Основной язык разработки |
| **FastAPI** | 0.115+ | Современный веб-фреймворк |
| **PostgreSQL** | 18 | Реляционная база данных |
| **SQLAlchemy** | 2.0+ | ORM с асинхронной поддержкой |
| **Pydantic** | 2.9+ | Валидация данных через Python-типы |
| **python-dotenv** | 1.0+ | Безопасное хранение секретов |
| **Uvicorn** | 0.30+ | Высокопроизводительный ASGI-сервер |
| **psycopg3** | 3.2+ | Асинхронный драйвер PostgreSQL |

---

🗂️ Структура проекта
text
fastapi-shop/
├── 📁 app/
│   ├── 📄 __init__.py
│   ├── 📄 main.py                 # Точка входа, инициализация приложения
│   ├── 📄 database.py              # Подключение к БД, сессии
│   ├── 📄 models.py                # SQLAlchemy модели (таблицы)
│   ├── 📄 schemas.py               # Pydantic схемы (валидация)
│   ├── 📄 crud.py                  # CRUD операции
│   └── 📁 routers/
│       ├── 📄 __init__.py
│       └── 📄 products.py          # Роуты для товаров
├── 📁 scripts/
│   └── 📄 seed_db.py               # Скрипт для заполнения БД
├── 📁 tests/                        # Тесты (soon)
├── 📄 .env                          # Переменные окружения (не в Git!)
├── 📄 .gitignore                    # Игнорируемые файлы
├── 📄 requirements.txt              # Зависимости
├── 📄 seed.sql                      # Дамп тестовых данных
├── 📄 README.md                     # Документация
└── 📄 docker-compose.yml            # Docker-конфигурация (soon)


