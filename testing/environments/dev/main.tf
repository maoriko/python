terraform {
  required_version = ">= 1.1.3"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "4.3.0"
    }
  }
}

locals {
  availability_zones = [
    "${var.region}a",
    "${var.region}b"
  ]
}

provider "aws" {
  profile = var.aws_profile
  region = var.region
}

module "vpc" {
  source = "../../terraform/modules/AWS/vpc"
  availability_zones = local.availability_zones
  environment        = var.environment
  providers = {
    aws=aws
  }
}

#module "alb" {
#  source = "../../terraform/modules/AWS/alb"
#  environment   = var.environment
#  public_subnet = module.vpc.public_subnets
#  vpc_id        = module.vpc.vpc_id
#providers = {
#  aws=aws
#}
#}





