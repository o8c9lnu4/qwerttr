#!/usr/bin/env python3
"""
Простой HTTP сервер для тестирования статической версии сайта
"""
import http.server
import socketserver
import os
from pathlib import Path

def start_server():
    """Запуск локального сервера для тестирования"""
    
    # Проверяем, существует ли папка static
    static_dir = Path("static")
    if not static_dir.exists():
        print("❌ Папка 'static' не найдена!")
        print("Сначала выполните: python manage.py build_static")
        return
    
    # Переходим в папку static
    os.chdir(static_dir)
    
    # Настройки сервера
    PORT = 8001
    Handler = http.server.SimpleHTTPRequestHandler
    
    try:
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            print(f"🚀 Статический сервер запущен на http://localhost:{PORT}")
            print(f"📁 Корневая папка: {static_dir.absolute()}")
            print("🌐 Откройте браузер и перейдите по адресу выше")
            print("⏹️  Для остановки нажмите Ctrl+C")
            print("-" * 50)
            
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print("\n👋 Сервер остановлен")
    except OSError as e:
        if e.errno == 48:  # Address already in use
            print(f"❌ Порт {PORT} уже занят!")
            print(f"Попробуйте другой порт или остановите процесс на порту {PORT}")
        else:
            print(f"❌ Ошибка запуска сервера: {e}")

if __name__ == "__main__":
    start_server()
