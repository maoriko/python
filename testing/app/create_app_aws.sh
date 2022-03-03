#!/bin/bash

function die() {
  echo $*
  exit 1
}

# ---------- Display instructions ----------
function app_creation_usage() {
  cat <<EOF
Usage: $0
   [--app_name] [--region] [--environment] [--aws_profile]

Arguments:
  --app_name                        The app name to deploy.
  --region                          The region you want to perform the operation on.
  --environment                     The environment staging/production.
  --aws_profile                     The AWS profile to use.

Optional:
  --public_key_name                 The name of public key on AWS
EOF
  exit 1
}

# ---------- get inputs from user ----------
function app_creation_handel_parameters() {
  app_name="perem-test"
  region="eu-west-3"
  environment="dev"
  aws_profile="perem"
  public_key_name="maor_pub"

  until [ -z "$1" ]; do
    case $1 in
    --app_name )
      app_name=$2
      shift
      ;;
    --region )
      region=$2
      shift
      ;;
    --environment )
      environment=$2
      shift
      ;;
    --aws_profile )
      aws_profile=$2
      shift
      ;;
    --public_key_name )
      public_key_name=$2
    esac
    shift
  done

  if [ -z "${app_name}" ]; then
    echo "app_name must be supplied"
    app_creation_usage
  elif [ -z "${region}" ]; then
    echo "Region must be supplied"
    app_creation_usage
  elif [[ ! "${environment}" =~ (dev|staging|production) ]]; then
    echo "environment must be dev / staging / production"
    app_creation_usage
  elif [ -z "${aws_profile}" ]; then
    echo "aws_profile must be supplied"
    app_creation_usage
  elif [ -z "${public_key_name}" ]; then
    public_key_name="maor_pub"
    echo "No public key chosen, using default $public_key_name"
  fi
}

app_creation_handel_parameters "$@"

# ---------- Validate region ----------
region_list=$(aws ec2 describe-regions --all-regions --query "Regions[].{Name:RegionName}" --output text --profile "$aws_profile")
if [[ ! $(echo $region_list | grep -w "$region") ]]; then
  printf "Region: $region not valid,\n\nOptions available:\n\n$region_list" && die
fi

# ---------- Apply Terraform ----------
dir_path="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"
pushd "${dir_path}/../environments/$environment" || die "failed to pushd to ${dir_path}/../environments/$environment"

terraform init
terraform destroy \
  -var app_name="${app_name}" \
  -var region="${region}" \
  -var environment="${environment}" \
  -var aws_profile="${aws_profile}" \
  -var public_key="${public_key_name}"
popd
