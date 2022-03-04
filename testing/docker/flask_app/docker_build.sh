#!/bin/bash

docker build -t maorpaz/flask_app:1.0.0 .
docker tag maorpaz/flask_app:1.0.0 maorpaz/flask_app:latest
