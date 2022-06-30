FROM public.ecr.aws/lambda/python:3.9

ENV ACCESS_KEY_ID=""
ENV SECRET_ACCESS_KEY=""
ENV SLACK_TOKEN=""

WORKDIR ${LAMBDA_TASK_ROOT}

COPY python/requirements.txt .
COPY python/check_subdomains_cert.py .

RUN pip3 install -r requirements.txt

CMD [ "check_subdomains_cert.lambda_handler" ]