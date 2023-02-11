FROM python:3.8-alpine

WORKDIR /agri

COPY requirements.txt /agri/

RUN pip install -r requirements.txt

COPY . /agri/

ENV DJANGO_SETTINGS_MODULE=config.settings.local


EXPOSE 8000

# Run the command to start the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
