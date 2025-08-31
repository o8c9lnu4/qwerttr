#!/bin/bash

echo "🚀 Silenceee Shop - Деплой на Netlify"
echo "======================================"

echo ""
echo "📦 Собираем статическую версию..."
python manage.py build_static

if [ $? -ne 0 ]; then
    echo "❌ Ошибка при сборке!"
    exit 1
fi

echo ""
echo "✅ Сборка завершена успешно!"
echo ""
echo "🌐 Для деплоя на Netlify выполните:"
echo "   netlify deploy --prod --dir=static"
echo ""
echo "📁 Статические файлы находятся в папке: static"
echo ""
echo "🧪 Для локального тестирования выполните:"
echo "   python test_static.py"
echo ""

read -p "Нажмите Enter для продолжения..."
