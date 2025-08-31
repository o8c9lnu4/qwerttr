@echo off
echo ========================================
echo   ПОДГОТОВКА К ДЕПЛОЮ НА NETLIFY
echo ========================================
echo.

echo ✅ Проект настроен для деплоя frontend!
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
echo Теперь у вас есть 2 варианта:
echo.
echo 1. ПРОСТОЙ СПОСОБ:
echo    - Перетащите папку frontend/dist на netlify.com
echo.
echo 2. ЧЕРЕЗ GIT (РЕКОМЕНДУЕТСЯ):
echo    - Загрузите код на GitHub
echo    - В Netlify выберите "New site from Git"
echo    - Build команды уже настроены в netlify.toml
echo.
echo Папка dist находится в: frontend\dist
echo.
echo Нажмите любую клавишу для выхода...
pause >nul
