FROM python:3.12-slim

# 🚀 直接寫成一整行，不使用任何反斜線換行，防呆效果 100%
RUN apt-get update && apt-get install -y default-libmysqlclient-dev pkg-config build-essential && rm -rf /var/lib/apt/lists/*

WORKDIR /code

COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /code/

# Clear Python cache to ensure fresh code runs
RUN find . -type d -name '__pycache__' -exec rm -rf {} + 2>/dev/null || true
RUN find . -type f -name '*.pyc' -delete 2>/dev/null || true