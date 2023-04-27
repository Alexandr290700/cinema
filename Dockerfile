# Установка базового образа
FROM python:3.10.6

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Установка рабочей директории
WORKDIR /app

# Установка зависимостей проекта в контейнер
COPY requirments.txt .

RUN pip install --upgrade pip

# Установка зависимостей проекта
RUN pip install -r requirments.txt

# Копирование файлов проекта в контейнер
COPY . .

# Запуск проекта
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# Запуск celery
# CMD ["celery", "-A", "mysite", "worker", "-l", "info"]

# # Запуск celery beat
# CMD [ "celery", "-A", "mysite", "beat", "-l", "INFO", "--scheduler", "django_celery_beat.schedulers:DatabaseScheduler" ]

# CMD ['celery' '-A' 'mysite' 'beat']

# CMD ["celery", "flower", "-A", "mysite", "--port=5566"]
