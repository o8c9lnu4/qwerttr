#!/usr/bin/env python
"""
Скрипт для сборки статической версии Django сайта
"""
import os
import sys
import django
from pathlib import Path

# Добавляем путь к проекту
sys.path.append(str(Path(__file__).parent))

# Настраиваем Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog_project.settings')
django.setup()

from django.core.management import call_command
from django.conf import settings
from django.template.loader import render_to_string
from django.urls import reverse
from blog.models import Category, Product
from blog.views import home_view, category_view, product_detail_view
import json

def build_static_site():
    """Сборка статической версии сайта"""
    print("🚀 Начинаем сборку статической версии сайта...")
    
    # Создаем папку для статических файлов
    static_dir = Path("static")
    static_dir.mkdir(exist_ok=True)
    
    # Копируем статические файлы Django
    print("📁 Копируем статические файлы...")
    call_command('collectstatic', '--noinput', '--clear')
    
    # Создаем главную страницу
    print("🏠 Создаем главную страницу...")
    context = home_view(None).context_data
    html_content = render_to_string('index.html', context)
    
    with open(static_dir / "index.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    
    # Создаем страницы категорий
    print("📂 Создаем страницы категорий...")
    categories = Category.objects.all()
    for category in categories:
        context = category_view(None, category.slug).context_data
        html_content = render_to_string('category.html', context)
        
        category_dir = static_dir / "category" / category.slug
        category_dir.mkdir(parents=True, exist_ok=True)
        
        with open(category_dir / "index.html", "w", encoding="utf-8") as f:
            f.write(html_content)
    
    # Создаем страницы товаров
    print("🛍️ Создаем страницы товаров...")
    products = Product.objects.all()
    for product in products:
        context = product_detail_view(None, product.id).context_data
        html_content = render_to_string('product_detail.html', context)
        
        product_dir = static_dir / "product" / str(product.id)
        product_dir.mkdir(parents=True, exist_ok=True)
        
        with open(product_dir / "index.html", "w", encoding="utf-8") as f:
            f.write(html_content)
    
    # Создаем sitemap
    print("🗺️ Создаем sitemap...")
    sitemap = {
        "pages": [
            {"url": "/", "title": "Главная"},
        ],
        "categories": [
            {"url": f"/category/{cat.slug}/", "title": cat.name} 
            for cat in categories
        ],
        "products": [
            {"url": f"/product/{prod.id}/", "title": prod.name}
            for prod in products
        ]
    }
    
    with open(static_dir / "sitemap.json", "w", encoding="utf-8") as f:
        json.dump(sitemap, f, ensure_ascii=False, indent=2)
    
    # Создаем robots.txt
    print("🤖 Создаем robots.txt...")
    robots_content = """User-agent: *
Allow: /

Sitemap: /sitemap.json
"""
    
    with open(static_dir / "robots.txt", "w", encoding="utf-8") as f:
        f.write(robots_content)
    
    print("✅ Статическая версия сайта успешно собрана!")
    print(f"📁 Файлы находятся в папке: {static_dir.absolute()}")

if __name__ == "__main__":
    build_static_site()
