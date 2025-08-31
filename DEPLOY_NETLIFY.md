# Деплой на Netlify

## ✅ Важно: Настройка для Frontend

Проект настроен для деплоя **только frontend части** (Vue.js) на Netlify. Backend (Django) остается на вашем сервере.

## Подготовка проекта

1. Убедитесь, что у вас установлен Node.js (версия 16 или выше)
2. Перейдите в папку frontend: `cd frontend`
3. Установите зависимости: `npm install`
4. Соберите проект: `npm run build`

## Деплой на Netlify

### Способ 1: Drag & Drop (самый простой)

1. Перейдите на [netlify.com](https://netlify.com)
2. Зарегистрируйтесь или войдите в аккаунт
3. Перетащите папку `frontend/dist` в область деплоя на главной странице
4. Netlify автоматически загрузит и развернет ваш сайт

### Способ 2: Через Git репозиторий (РЕКОМЕНДУЕТСЯ)

1. Загрузите ваш код на GitHub/GitLab/Bitbucket
2. В Netlify выберите "New site from Git"
3. Подключите ваш репозиторий
4. **Build команды уже настроены в netlify.toml:**
   - Build command: `cd frontend && npm install && npm run build`
   - Publish directory: `frontend/dist`
5. Нажмите "Deploy site"

### Способ 3: Через Netlify CLI

1. Установите Netlify CLI: `npm install -g netlify-cli`
2. Войдите в аккаунт: `netlify login`
3. Перейдите в папку frontend: `cd frontend`
4. Выполните деплой: `netlify deploy --prod --dir=dist`

## Настройки после деплоя

1. **Домен**: Netlify автоматически присвоит вашему сайту случайный домен
2. **Кастомный домен**: В настройках сайта можно добавить свой домен
3. **HTTPS**: Автоматически включен для всех сайтов

## Важные моменты

- ✅ `netlify.toml` уже настроен для деплоя frontend
- ✅ Файл `_redirects` в папке dist обеспечивает правильную работу SPA
- ⚠️ **Backend API должен быть доступен из интернета**
- ⚠️ **Настройте CORS на Django backend для домена Netlify**
- ✅ Для production используйте переменные окружения для API URL

## Настройка Backend для Frontend

После деплоя frontend на Netlify, вам нужно:

1. **Развернуть Django backend** на хостинге (например, Heroku, DigitalOcean, AWS)
2. **Настроить CORS** в Django для домена Netlify:
   ```python
   CORS_ALLOWED_ORIGINS = [
       "https://your-site.netlify.app",
       "https://your-custom-domain.com"
   ]
   ```
3. **Обновить API URL** в frontend для production

## Возможные проблемы

1. **404 ошибки при обновлении страницы**: ✅ Решено файлом `_redirects`
2. **Проблемы с API**: Проверьте CORS настройки вашего backend
3. **Проблемы с роутингом**: ✅ Настроен historyApiFallback
4. **Build ошибки**: Убедитесь, что `netlify.toml` находится в корне проекта

## Полезные ссылки

- [Netlify Documentation](https://docs.netlify.com/)
- [Vue.js Deployment Guide](https://vuejs.org/guide/deployment.html)
- [SPA Routing on Netlify](https://docs.netlify.com/routing/redirects/rewrites-proxies/#history-pushstate-and-single-page-apps)
- [Django CORS Headers](https://pypi.org/project/django-cors-headers/)
