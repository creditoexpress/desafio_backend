FROM python:3.6.8-alpine3.9

LABEL MAINTAINER="Cleiton Soares <cleiton@c2hweb.com.br>"

ENV GROUP_ID=1000 \
    USER_ID=1000

WORKDIR /var/www/html/desafio_backend

ADD . /var/www/html/desafio_backend
RUN pip install -r requirements.txt
RUN pip install gunicorn
RUN pip install flask-restful
RUN pip install flask-mongoengine
RUN pip install flask-restful
RUN pip install flask-jwt-extended

RUN addgroup -g $GROUP_ID www
RUN adduser -D -u $USER_ID -G www www -s /bin/sh

USER www

EXPOSE 5000

CMD [ "gunicorn", "-w", "4", "--workers", "8", "--threads", "8", "-t", "120", "--bind", "0.0.0.0:5000", "wsgi", "--log-level", "debug" ]
