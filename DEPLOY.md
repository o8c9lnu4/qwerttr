# 🚀 Быстрый деплой на Netlify

## Способ 1: Через Netlify CLI (рекомендуется)

### 1. Установите Netlify CLI
```bash
npm install -g netlify-cli
```

### 2. Войдите в аккаунт
```bash
netlify login
```

### 3. Соберите статическую версию
```bash
python manage.py build_static
```

### 4. Деплой
```bash
netlify deploy --prod --dir=static
```

## Способ 2: Через GitHub + Netlify

### 1. Загрузите код в GitHub

### 2. Подключите к Netlify
- Зайдите на [netlify.com](https://netlify.com)
- Нажмите "New site from Git"
- Выберите ваш репозиторий

### 3. Настройте параметры сборки
- **Build command:** `python manage.py build_static`
- **Publish directory:** `static`
- **Python version:** `3.11`

### 4. Нажмите "Deploy site"

## Способ 3: Ручная загрузка

### 1. Соберите статику
```bash
python manage.py build_static
```

### 2. Сожмите папку `static` в ZIP

### 3. Загрузите на Netlify через drag & drop

## 🧪 Локальное тестирование

Перед деплоем протестируйте статическую версию:

```bash
python test_static.py
```

Откройте http://localhost:8001 в браузере.

## ⚠️ Важные замечания

- Статическая версия не поддерживает авторизацию и корзину
- Это демо-версия для показа дизайна
- Для полнофункционального магазина используйте Django на хостинге

## 🔧 Устранение проблем

### Ошибка "Port already in use"
```bash
# Найти процесс
lsof -i :8001
# Остановить процесс
kill -9 <PID>
```

### Ошибка сборки
```bash
# Очистить и пересобрать
rm -rf static/
python manage.py build_static
```

---

**Удачного деплоя! 🎉**
