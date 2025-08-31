# Silenceee Shop

Современный интернет-магазин, построенный на Django с красивым дизайном и функциональностью корзины.

## 🚀 Деплой на Netlify

### Подготовка к деплою

1. **Убедитесь, что у вас установлен Python 3.11+**
2. **Установите зависимости:**
   ```bash
   pip install -r requirements.txt
   ```

### Сборка статической версии

Для создания статической версии сайта выполните:

```bash
python manage.py build_static
```

Эта команда создаст папку `static/` со всеми необходимыми HTML файлами и статическими ресурсами.

### Деплой на Netlify

#### Способ 1: Через Netlify CLI

1. **Установите Netlify CLI:**
   ```bash
   npm install -g netlify-cli
   ```

2. **Войдите в аккаунт:**
   ```bash
   netlify login
   ```

3. **Инициализируйте проект:**
   ```bash
   netlify init
   ```

4. **Соберите статическую версию:**
   ```bash
   python manage.py build_static
   ```

5. **Деплой:**
   ```bash
   netlify deploy --prod --dir=static
   ```

#### Способ 2: Через GitHub + Netlify

1. **Загрузите код в GitHub репозиторий**

2. **Подключите репозиторий к Netlify:**
   - Зайдите на [netlify.com](https://netlify.com)
   - Нажмите "New site from Git"
   - Выберите ваш репозиторий

3. **Настройте параметры сборки:**
   - **Build command:** `python manage.py build_static`
   - **Publish directory:** `static`
   - **Python version:** `3.11`

4. **Нажмите "Deploy site"**

### Структура проекта

```
silenceee-shop/
├── blog/                    # Django приложение
│   ├── models.py           # Модели данных
│   ├── views.py            # Представления
│   ├── urls.py             # URL маршруты
│   └── templates/          # HTML шаблоны
├── blog_project/           # Настройки Django
├── static/                 # Статические файлы (создается при сборке)
├── templates/              # Основные шаблоны
├── netlify.toml           # Конфигурация Netlify
├── requirements.txt        # Python зависимости
└── README.md              # Этот файл
```

### Функциональность

- ✅ Красивый современный дизайн
- ✅ Каталог товаров с категориями
- ✅ Детальные страницы товаров
- ✅ Система корзины (требует авторизации)
- ✅ Авторизация и регистрация пользователей
- ✅ Адаптивный дизайн для мобильных устройств
- ✅ SEO-оптимизация (sitemap, robots.txt)

### Технологии

- **Backend:** Django 4.2.7
- **Frontend:** HTML5, CSS3, JavaScript (ES6+)
- **База данных:** SQLite (для разработки)
- **Статика:** Django collectstatic
- **Деплой:** Netlify

### Локальная разработка

1. **Клонируйте репозиторий:**
   ```bash
   git clone <your-repo-url>
   cd silenceee-shop
   ```

2. **Создайте виртуальное окружение:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # или
   venv\Scripts\activate     # Windows
   ```

3. **Установите зависимости:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Примените миграции:**
   ```bash
   python manage.py migrate
   ```

5. **Создайте суперпользователя:**
   ```bash
   python manage.py createsuperuser
   ```

6. **Запустите сервер:**
   ```bash
   python manage.py runserver
   ```

7. **Откройте браузер:** http://127.0.0.1:8000

### Важные замечания

⚠️ **Внимание:** Статическая версия сайта не поддерживает динамические функции Django (авторизация, корзина, API). Это демо-версия для показа дизайна и структуры.

Для полнофункционального магазина рекомендуется:
- Использовать Django на хостинге (PythonAnywhere, Heroku, DigitalOcean)
- Или переписать на статический генератор (Next.js, Gatsby, Hugo)

### Поддержка

Если у вас возникли вопросы или проблемы с деплоем, создайте issue в репозитории.

---

**Удачного деплоя! 🚀**
