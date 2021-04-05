FROM python:3.9-slim

ENV PYTHONUNBUFFERED True

ENV APP_HOME /application
WORKDIR $APP_HOME
COPY /application /application
COPY ./requirements.txt /application

RUN pip install -r /application/requirements.txt

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout main:app