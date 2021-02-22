FROM python:3.7-alpine

# Added env var to disable poetry default create venv behavior
ENV POETRY_VIRTUALENVS_CREATE = false

# Installing required dependencies for the project setup and run
RUN apk add --no-cache alpine-sdk
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
ENV PATH = "${PATH}:/root/.poetry/bin"

# Fixing pip version
RUN python -m pip install --upgrade pip

# Move toml file for the app folder
WORKDIR /app
COPY poetry.lock pyproject.toml /app/
RUN poetry install

# Exposes the port 5000
EXPOSE 5000

# Defining the app folder
COPY ./app /app/app
COPY ./scripts /app/scripts

# Executing the app
CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000"]
