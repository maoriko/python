FROM python:3.9.10-alpine3.15 as base

ENV FLASK_APP=flask_web_server.py
ENV environment=dev

RUN python -m pip install --upgrade pip

RUN mkdir /app/
WORKDIR /app/

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY ./flask_server/flask_web_server.py /app/


COPY vault_connection_test.py /app/vault_connection_test.py

################### START NEW IMAGE: PRODUCTION ###################
FROM base as prod

RUN apk update
RUN apk add busybox-extras
RUN apk add curl


CMD flask run -h 0.0.0.0 -p 5000