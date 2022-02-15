FROM python:3.9-slim

WORKDIR /backend-fast-api-app

COPY /src /backend-fast-api-app

RUN pip install -r /backend-fast-api-app/requirements.txt

WORKDIR /backend-fast-api-app
ENV PYTHONPATH /backend-fast-api-app

RUN uvicorn main:app --host 0.0.0.0 --reload --debug