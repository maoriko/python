FROM python:3.9.10-alpine3.15 as base

ENV FLASK_APP=server.py
ENV environment=dev

RUN mkdir /work/
WORKDIR /work/

COPY ./src/requirements.txt /work/requirements.txt
RUN pip install -r requirements.txt

COPY ./src/ /work/

############START NEW IMAGE : DEBUGGER ###################
#FROM base as debug
#RUN pip install ptvsd
#
#WORKDIR /work/
#CMD python -m ptvsd --host 0.0.0.0 --port 5678 --wait --multiprocess -m flask run -h 0.0.0.0 -p 5000

###########START NEW IMAGE: PRODUCTION ###################
FROM base as dev

RUN apk add mysql-client

COPY ./src/entrypoint.sh /work/entrypoint.sh

CMD flask run -h 0.0.0.0 -p 5000
