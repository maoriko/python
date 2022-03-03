FROM python:3.9.10-alpine3.15 as base

ENV FLASK_APP=flask_web_server.py
ENV environment=dev

RUN mkdir /work/
WORKDIR /work/

COPY requirements.txt /work/requirements.txt
RUN pip install -r requirements.txt

COPY ./flask_server/flask_web_server.py /work/

###########START NEW IMAGE: PRODUCTION ###################
FROM base as prod

RUN apk add mysql-client

COPY ./src/entrypoint.sh /work/entrypoint.sh

CMD flask run -h 0.0.0.0 -p 5000
