# syntax=docker/dockerfile:1
FROM python:3.8.2
ENV PYTHONUNBUFFERED=1
WORKDIR /flaskapp
COPY requirements.txt /flaskapp/
RUN pip install -r requirements.txt
COPY . /flaskapp/
