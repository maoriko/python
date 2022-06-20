#!/bin/bash

dir_path="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"
path_to_app_folder="${dir_path}/../docker/flask_app"

pushd "$path_to_app_folder" || exit 1

tag="1.0.1"
repo="maorpaz"
image="flask_app"
tag_latest="false"

docker build -t "${repo}/${image}:v${tag}" .
docker push "${repo}/${image}:v${tag}"

if [[ "${tag_latest}" = "true" ]]; then
  docker tag "${repo}/${image}:v${tag}" "${repo}/${image}:latest"
  docker push "${repo}/${image}:latest"
fi

