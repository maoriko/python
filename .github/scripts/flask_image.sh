#!/bin/bash

dir_path="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"
source "${dir_path}/common.sh"

# Connect to Docker
docker_login maorpaz "${MAORPAZ_DOCKER_HUB}"

current_version=

# Build image

