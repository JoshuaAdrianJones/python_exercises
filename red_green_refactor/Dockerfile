# syntax=docker/dockerfile:1

FROM python:3.10.6-bullseye

WORKDIR /usr/src/app

COPY requirements.txt ./
COPY Makefile Makefile
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
CMD make run
