FROM python:3.9-alpine

WORKDIR /app

COPY requirements.txt .

RUN apk add --no-cache postgresql-dev gcc musl-dev && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

COPY . .

ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE agri.settings

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
