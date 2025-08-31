@echo off
echo 🚀 Silenceee Shop - Деплой на Netlify
echo ======================================

echo.
echo 📦 Собираем статическую версию...
python manage.py build_static

if %errorlevel% neq 0 (
    echo ❌ Ошибка при сборке!
    pause
    exit /b 1
)

echo.
echo ✅ Сборка завершена успешно!
echo.
echo 🌐 Для деплоя на Netlify выполните:
echo    netlify deploy --prod --dir=static
echo.
echo 📁 Статические файлы находятся в папке: static
echo.
echo 🧪 Для локального тестирования выполните:
echo    python test_static.py
echo.
pause
