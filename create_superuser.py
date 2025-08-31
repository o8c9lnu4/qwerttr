#!/usr/bin/env python
import os
import django

# Настройка Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog_project.settings')
django.setup()

from django.contrib.auth.models import User

def create_superuser():
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
        print('Суперпользователь создан:')
        print('Логин: admin')
        print('Пароль: admin123')
    else:
        print('Суперпользователь уже существует')

if __name__ == '__main__':
    create_superuser()
