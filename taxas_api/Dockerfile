FROM python:latest

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN python3 -m pip install --user --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3", "app.py"]