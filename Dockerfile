# Dockerfile
FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    libpq-dev \
    build-essential \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

# Установим рабочую директорию
WORKDIR /app

# Скопируем requirements.txt и установим зависимости
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Скопируем весь проект в контейнер
COPY . /app/

# Ожидаемую переменную окружения для запуска
ENV PYTHONUNBUFFERED=1

# Выполним миграции и стартуем сервер
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
