FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7
RUN apk --update --no-cache add bash nano python3-dev && pip3 install --upgrade pip
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 3333
CMD python3 app