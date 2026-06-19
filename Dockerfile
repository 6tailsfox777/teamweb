FROM python:3.12-slim

# 🚀 直接寫成一整行，不使用任何反斜線換行，防呆效果 100%
RUN apt-get update && apt-get install -y default-libmysqlclient-dev pkg-config build-essential && rm -rf /var/lib/apt/lists/*

WORKDIR /code

COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /code/