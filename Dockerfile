FROM mcr.microsoft.com/playwright/python:v1.50.0-noble

WORKDIR /app/src

COPY . .

COPY requirements.txt .

RUN pip install -r requirements.txt

ENV PYTHONPATH = /app/src
RUN playwright install chrome