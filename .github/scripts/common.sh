dockerhub_password="${MAORPAZ_DOCKER_HUB}"

function echo_n_quit() {
  echo "$*"
  exit 1
}

# Connect to docker-hub
function docker_login() {
  dockerhub_username=$1
  dockerhub_password=$2

  set +o history
  echo "${dockerhub_password}" | docker login --username "${dockerhub_username}" --password-stdin
  set -o history
}

function bump_image_version() {
  dockerhub_username=$1
  dockerhub_password=$2
  repo_name=$3
  image_name=$4
  major_minor_patch=$5

  # Get latest docker image version
  TOKEN=$(curl -s -H "Content-Type: application/json" -X POST -d '{"username": "'${dockerhub_username}'", "password": "'${dockerhub_password}'"}' https://hub.docker.com/v2/users/login/ | jq -r .token)
  current_version=$(curl -s -H "Authorization: JWT ${TOKEN}" "https://hub.docker.com/v2/repositories/${repo_name}/${image_name}/tags/?page_size=500" | jq -r '.results | sort_by(.last_updated) | .[-2] | .name')
  echo "Current version - v${current_version}"

  major_version=$(echo "${current_version}" | cut -d'.' -f 1)
  minor_version=$(echo "${current_version}" | cut -d'.' -f 2)
  patch_version=$(echo "${current_version}" | cut -d'.' -f 3)

  if [[ "${major_minor_patch}" == "major" ]]; then
    major_version=$((major_version+1))
    minor_version=0
    patch_version=0
  elif [[ "${major_minor_patch}" == "minor" ]]; then
    minor_version=$((minor_version+1))
    patch_version=0
  elif [[ "${major_minor_patch}" == "patch" ]]; then
    patch_version=$((patch_version+1))

  else
    echo_n_quit "Not valid, choose major|minor|patch - ${major_minor_patch}"
  fi

  echo "New version - "${major_version}.${minor_version}.${patch_version}""

  new_version="${major_version}.${minor_version}.${patch_version}"
  export new_version=${new_version}
}

bump_image_version "maorpaz" "06fd51fa-c0ab-4ee7-8b0a-6958145a218a" "maorpaz" "flask_app" "patch"