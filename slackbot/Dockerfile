FROM python:3.9.10-alpine3.15 as base

ENV SLACK_BOT_TOKEN=""
ENV GITHUB_REPO_TOKEN=""

ARG PORT
ENV PORT=${PORT}
ARG ENVIRONMENT
ENV ENVIRONMENT=${ENVIRONMENT}

# Flask environment variables
#ENV FLASK_APP=flask_web_server.py
#ENV FLASK_ENV=${FLASK_ENV}

RUN python -m pip install --upgrade pip

RUN mkdir /app/
WORKDIR /app/

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY slack_bot_app/slackbot/slackbot.py /app/

#For Logs
VOLUME /var/log/flask

#For ConfigMap
VOLUME /etc/flask

################### START NEW IMAGE: PRODUCTION ###################
FROM base as prod

#RUN apk update
#RUN apk add busybox-extras
#RUN apk add curl


CMD ["slackbot.py"]
ENTRYPOINT ["python3"]

# docker run -it -v ${PWD}:app -w app  slackbot:1.0.0 /bin/sh