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

## 📦 Установка и запуск

### Предварительные требования

- Python 3.14 или выше
- PostgreSQL 18
- Git
- (Опционально) Docker 24+

### 1. Клонирование репозитория

```bash
git clone https://github.com/psx05/fastapi_shop.git
cd fastapi-shop

2. Виртуальное окружение (Python 3.14)
Windows:

bash
python -m venv venv --python=3.14
venv\Scripts\activate
Linux/Mac:

bash
python3.14 -m venv venv
source venv/bin/activate
3. Установка зависимостей
bash
pip install --upgrade pip
pip install -r requirements.txt
4. Настройка PostgreSQL 18
Установка PostgreSQL 18:

Windows: Скачай с https://www.postgresql.org/download/windows/

Linux: sudo apt install postgresql-18

Mac: brew install postgresql@18

Создание базы данных:

bash
# Вход в psql
sudo -u postgres psql

# Создание БД
CREATE DATABASE fastapi_shop;

# Создание пользователя (если нужно)
CREATE USER shop_user WITH PASSWORD 'shop_password';
GRANT ALL PRIVILEGES ON DATABASE fastapi_shop TO shop_user;

# Выход
\q
5. Переменные окружения
Создай файл .env в корне проекта:

env
# Для пользователя postgres
DATABASE_URL=postgresql://postgres:postgres@localhost/fastapi_shop

# Или для отдельного пользователя
# DATABASE_URL=postgresql://shop_user:shop_password@localhost/fastapi_shop

# Настройки приложения
SECRET_KEY=your-super-secret-key-here
DEBUG=True
APP_NAME=FastAPI Shop
6. Инициализация базы данных
Автоматическое создание таблиц:

bash
# Таблицы создадутся автоматически при первом запуске
python -c "from app.database import engine, Base; from app import models; Base.metadata.create_all(bind=engine)"
Заполнение тестовыми данными:

bash
# Через psql
psql -U postgres -d fastapi_shop -f seed.sql

# Через Python (альтернатива)
python scripts/seed_db.py
7. Запуск приложения
bash
# Режим разработки
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Режим продакшена
uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
После запуска перейди по адресу: http://localhost:8000

📚 API Документация
FastAPI автоматически генерирует документацию:

Интерфейс	URL	Особенности
📖 Swagger UI	http://localhost:8000/docs	Интерактивное тестирование API
📗 ReDoc	http://localhost:8000/redoc	Альтернативный стиль документации
📋 OpenAPI JSON	http://localhost:8000/openapi.json	Сырая спецификация
Примеры запросов
Создание товара
bash
curl -X POST "http://localhost:8000/products" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Ноутбук ASUS ROG Strix G18",
    "description": "18-дюймовый игровой ноутбук, RTX 5090, 64GB RAM",
    "price": 299990.00,
    "stock": 3
  }'
Получение всех товаров
bash
curl "http://localhost:8000/products?skip=0&limit=10"
Получение товара по ID
bash
curl "http://localhost:8000/products/1"
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
💾 Тестовые данные
В проекте уже есть 50+ готовых товаров всех категорий:

💻 Ноутбуки (ASUS ROG, TUF, ZenBook)

🖥️ Мониторы (TUF, ProArt, ROG)

🖱️ Мыши (ROG Keris, Gladius, Spatha)

⌨️ Клавиатуры (ROG Azoth, Strix Scope)

🎧 Наушники (ROG Delta, Strix Go)

🎒 Сумки и рюкзаки

🎮 Аксессуары (коврики, подставки)

🔧 Комплектующие (RTX 4060, B760, SSD)

Проверка:

bash
curl http://localhost:8000/products | json_pp
🐳 Docker (soon)
yaml
version: '3.8'
services:
  db:
    image: postgres:18-alpine
    environment:
      POSTGRES_DB: fastapi_shop
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
  
  app:
    build: .
    ports:
      - "8000:8000"
    depends_on:
      - db
    env_file:
      - .env

volumes:
  postgres_data:
bash
# Запуск
docker-compose up -d

# Остановка
docker-compose down

# Просмотр логов
docker-compose logs -f app
🧪 Тестирование (soon)
bash
# Установка зависимостей для тестов
pip install pytest pytest-asyncio httpx

# Запуск тестов
pytest tests/ -v

# С coverage
pytest tests/ --cov=app --cov-report=html
📈 Roadmap
Фаза 1: Базовый функционал ✅
Настройка проекта

Модель товаров

CRUD операции

PostgreSQL 18 интеграция

50+ тестовых товаров

Фаза 2: Расширение 🔄
Категории товаров

Фильтрация и поиск

Пагинация

Валидация данных

Фаза 3: Пользователи 📝
Регистрация

JWT авторизация

Роли (админ/пользователь)

Профиль пользователя

Фаза 4: Покупки 🛒
Корзина

Заказы

История покупок

Статусы заказов

Фаза 5: Продакшен 🚀
Docker-контейнеризация

CI/CD

Мониторинг

Логирование

👨‍💻 Разработка
Правила работы с Git
bash
# 1. Проверь статус
git status

# 2. Добавь изменения
git add .

# 3. Сделай осмысленный коммит
git commit -m "feat: add product categories"

# 4. Запушь
git push origin main
Commit Convention
feat: — новый функционал

fix: — исправление багов

docs: — документация

style: — форматирование

refactor: — рефакторинг

test: — тесты

chore: — обслуживание

Code Style
Соблюдаем PEP 8

Используем type hints

Документируем функции

Пишем тесты для нового кода

🤝 Как внести вклад
Форкни репозиторий

Создай ветку (git checkout -b feature/amazing-feature)

Закоммить изменения (git commit -m 'feat: add amazing feature')

Запушь ветку (git push origin feature/amazing-feature)

Открой Pull Request

📄 Лицензия
MIT © Твоё Имя

📬 Контакты
GitHub: @psx05

Telegram: @mr_robot_05

Email: sanches.18@mail.ru

⭐ Поддержка проекта
Если проект оказался полезным:

Поставь звезду ⭐ на GitHub

Расскажи друзьям

Сделай форк и добавь свои фичи

<p align="center"> <b>Сделано с ❤️ для сообщества Python разработчиков</b> </p><p align="center"> <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=100&section=footer&text=FastAPI%20Shop%202026&fontSize=30&fontAlignY=70"/> </p><p align="center"> <img src="https://visitcount.itsvg.in/api?id=ТВОЙ_ЛОГИН&label=Views&color=12&icon=5&pretty=true" /> </p> ```

