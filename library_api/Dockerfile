FROM python:3.10-slim

WORKDIR /app

ENV PYTHONUNBUFFERED=1

COPY ../poetry.lock ./pyproject.toml ./

RUN pip install poetry==1.5.1

RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi --no-root --only main

COPY ./library_api .

RUN chmod +x entrypoint.sh
