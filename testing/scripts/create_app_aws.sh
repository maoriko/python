#!/bin/bash

#set -x

function die() {
  echo $*
  exit 1
}

function validate_region() {
local profile=$1
local region=$2
  region_list=$(aws ec2 describe-regions --all-regions --query "Regions[].{Name:RegionName}" --output text --profile "$aws_profile")
  if [[ ! $(echo $region_list | grep -w "$region") ]]; then
    printf "Region: $region not valid,\n\nOptions available:\n\n$region_list" && die
  fi
}

# ---------- Display instructions ----------
function app_creation_usage() {
  cat <<EOF
Usage: $0
   [--app_name] [--region] [--environment] [--aws_profile] [--instance_ami] 

Arguments:
  --app_name                        The app name to deploy.
  --region                          The region you want to perform the operation on.
  --environment                     The environment staging/production.
  --aws_profile                     The AWS profile to use.

Optional:
  --public_key_name                 The name of public key on AWS
  --instance_ami                    The AMI of AWS, Note, this based region, default for eu-west-3 is: ami-0c0f763628afa7f8b refer from here: https://cloud-images.ubuntu.com/locator/
EOF
  exit 1
}

# ---------- get inputs from user ----------
function app_creation_handel_parameters() {
  app_name="perem-test"
  region="eu-west-3"
  environment="dev"
  aws_profile="perem"
  public_key_name=""
  instance_ami=""

  until [ -z "$1" ]; do
    case "$1" in
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
      shift
      ;;
    --instance_ami )
      instance_ami=$2
      shift 
      ;;
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
  fi
}

app_creation_handel_parameters "$@"

# ---------- optional arguments ----------
if [[ ${instance_ami} == "" ]]; then
  instance_ami="ami-0c0f763628afa7f8b"
  printf "No instance_ami chosen, using default.\nami-id: $instance_ami\n\n"
fi

if [[ "${public_key_name}" == "" ]]; then
  public_key_name="maor_pop"
  printf "No public key chosen, using default.\nPublic key name: $public_key_name\n\n"
fi

# ---------- Validate region ----------
validate_region "$aws_profile" "$region"

# ---------- Validate AMI ----------
if [ $(echo "${instance_ami}" == "ami-0c0f763628afa7f8b") ] && [ $(echo "${region}" != "eu-west-3") ]; then
  echo "The AMI only suits to eu-west-3!"
fi

# ---------- Apply Terraform ----------
dir_path="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"
pushd "${dir_path}/../terraform/environments/$environment" || die "failed to pushd to ${dir_path}/../environments/$environment"

terraform init
terraform apply \
  -var app_name="${app_name}" \
  -var region="${region}" \
  -var environment="${environment}" \
  -var aws_profile="${aws_profile}" \
  -var public_key_name="${public_key_name}" \
  -var instance_ami="${instance_ami}"
popd
