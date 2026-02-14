from sqladmin import Admin, ModelView
from app.database import engine
from app.models import Product, Category
from app.main import app

# Настройка админки
admin = Admin(app, engine)


# Класс для отображения товаров в админке
class ProductAdmin(ModelView, model=Product):
    column_list = [
        Product.id,
        Product.name,
        Product.price,
        Product.stock,
        Product.category,  # ← ИЗМЕНЕНО: показываем объект категории, а не ID
    ]
    column_searchable_list = [Product.name]
    column_sortable_list = [Product.id, Product.price, Product.stock]
    form_columns = [Product.name, Product.description, Product.price, Product.stock, Product.category_id]

    # Форматируем отображение категории
    column_formatters = {
        Product.category: lambda m, a: m.category.name if m.category else "-"
    }

    name = "Товар"
    name_plural = "Товары"
    icon = "fa-solid fa-box"


# Класс для отображения категорий в админке
class CategoryAdmin(ModelView, model=Category):
    column_list = [
        Category.id,
        Category.name,
        Category.description,
    ]

    column_searchable_list = [Category.name]
    form_columns = [Category.name, Category.description]
    column_sortable_list = [Category.id, Category.name]

    name = "Категория"
    name_plural = "Категории"
    icon = "fa-solid fa-tags"


# Регистрируем модели в админке
admin.add_view(ProductAdmin)
admin.add_view(CategoryAdmin)