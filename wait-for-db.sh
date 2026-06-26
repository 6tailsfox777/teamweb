#!/bin/sh
set -e

echo "Waiting for MySQL at db:3306..."

python << 'EOF'
import socket
import time

while True:
    try:
        s = socket.socket()
        s.settimeout(1)
        s.connect(("db", 3306))
        s.close()
        print("MySQL is ready")
        break
    except Exception:
        print(".", end="", flush=True)
        time.sleep(1)
EOF

echo ""
echo "Cleaning cache..."
find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
find . -type f -name "*.pyc" -delete 2>/dev/null || true

echo "Running migrations..."
python manage.py migrate --no-input

echo "Starting Django..."
exec python manage.py runserver 0.0.0.0:8000