FROM python:3.8-slim

RUN apt-get update

ADD . /flask-deploy

WORKDIR /flask-deploy


COPY . .

RUN pip install -r ./requirements.txt

ENTRYPOINT ["python3"]

CMD ["main.py"]