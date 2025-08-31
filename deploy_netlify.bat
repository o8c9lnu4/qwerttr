@echo off
echo ========================================
echo   ПОДГОТОВКА К ДЕПЛОЮ НА NETLIFY
echo ========================================
echo.

echo ✅ Проект исправлен и готов к деплою!
echo.

echo Переходим в папку frontend...
cd frontend

echo Устанавливаем зависимости...
call npm install

echo Собираем проект...
call npm run build

echo.
echo ========================================
echo   ПРОЕКТ ГОТОВ К ДЕПЛОЮ! 🚀
echo ========================================
echo.
echo Теперь:
echo 1. Перейдите на netlify.com
echo 2. Перетащите папку frontend/dist в область деплоя
echo 3. Готово! Ваш сайт будет доступен
echo.
echo Папка dist находится в: frontend\dist
echo.
echo Нажмите любую клавишу для выхода...
pause >nul
