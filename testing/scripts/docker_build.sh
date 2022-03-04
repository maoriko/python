#!/bin/bash

dir_path="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"

path_to_app_folder="${dir_path}/../docker/flask_app"

pushd $path_to_app_folder

docker build -t maorpaz/flask_app:1.0.0 .
docker tag maorpaz/flask_app:1.0.0 maorpaz/flask_app:latest