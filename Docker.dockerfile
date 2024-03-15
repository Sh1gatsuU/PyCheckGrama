# Використовуємо офіційний образ Python
FROM python:3.9-slim

# Встановлюємо робочу директорію контейнера
WORKDIR /app

# Скопіюємо файли проекту в контейнер
COPY . /app

# Встановлюємо необхідні залежності
RUN pip install --no-cache-dir -r requirements.txt

# Вказуємо команду для запуску додатку
CMD ["python", "app.py"]
