FROM python:3.11.10-slim@sha256:7bc5084992524a13d7c57d54b830d676834ff448bde97e2f5f79ad30e0176b6d

RUN pip install --no-cache-dir pytest==8.4.1 pytest-json-ctrf==0.3.5

WORKDIR /app

RUN mkdir -p /logs/verifier

COPY access.log /app/access.log
