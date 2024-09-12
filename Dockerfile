# Используем Python базовый образ
FROM python:3.9-slim

# Устанавливаем необходимые библиотеки
RUN pip install google-cloud-aiplatform

# Копируем скрипт для обучения
COPY app/train_model.py /app/train_model.py

# Устанавливаем рабочую директорию
WORKDIR /app

# Устанавливаем рабочие переменные окружения
ENV GOOGLE_APPLICATION_CREDENTIALS="/secrets/gcp/vertex-ai-key.json"

# Запускаем скрипт обучения
CMD ["python", "train_model.py"]
