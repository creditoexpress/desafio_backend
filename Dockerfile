FROM python:3-alpine
RUN apk add --virtual .build-dependencies \
            --no-cache \
            python3-dev \
            build-base \
            linux-headers \
            pcre-dev
RUN apk add --no-cache pcre
WORKDIR /application
COPY /application /application
COPY ./requirements.txt /application
RUN pip install -r /application/requirements.txt
RUN apk del .build-dependencies && rm -rf /var/cache/apk/*
EXPOSE 8080
CMD ["uwsgi", "--ini", "/app/wsgi.ini"]