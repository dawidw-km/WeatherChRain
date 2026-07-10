FROM python:3.12-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev \
    cron \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN useradd -m -r appuser && \
    mkdir -p /app && \
    chown -R appuser:appuser /app

COPY cron/fetch_weather /etc/cron.d/fetch-weather
RUN chmod 0644 /etc/cron.d/fetch-weather

COPY cron/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 8000

CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]