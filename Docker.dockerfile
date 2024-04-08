# Використовуємо офіційний образ Python з Docker Hub
FROM python:3.9-slim

# Встановлюємо необхідні залежності
RUN pip install requests

# Копіюємо файли проекту в контейнер
COPY . /app

# Задаємо робочу директорію
WORKDIR /app

# Команда для запуску   додатку
CMD ["python", "your_script.py"]
