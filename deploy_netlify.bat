@echo off
echo Подготовка к деплою на Netlify...
echo.

echo Переходим в папку frontend...
cd frontend

echo Устанавливаем зависимости...
call npm install

echo Собираем проект...
call npm run build

echo.
echo Проект собран! Папка dist готова для деплоя.
echo.
echo Теперь вы можете:
echo 1. Перетащить папку frontend/dist на netlify.com
echo 2. Или использовать Git репозиторий
echo 3. Или использовать Netlify CLI
echo.
echo Нажмите любую клавишу для выхода...
pause >nul
