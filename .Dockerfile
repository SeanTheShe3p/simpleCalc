FROM python:3.10-slim

WORKDIR /

COPY requirements /home

RUN pip install -r requirements.txt

COPY . .
