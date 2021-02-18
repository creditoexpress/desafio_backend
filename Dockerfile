FROM python:3.7-alpine

# Installing the dependencies
RUN apk add --no-cache alpine-sdk
COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5000

# Defining the app folder
COPY ./app /app

# Running the app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000"]
