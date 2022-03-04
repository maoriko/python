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
  cidr_source_ip = "0.0.0.0/0"
  availability_zones = [
    "${var.region}a",
    "${var.region}b"
  ]
}

provider "aws" {
  profile = var.aws_profile
  region  = var.region
}

module "vpc" {
  source             = "../../modules/AWS/vpc"
  environment        = var.environment
  availability_zones = local.availability_zones
  providers = {
    aws = aws
  }
}

module "alb" {
  source        = "../../modules/AWS/alb"
  vpc_id        = module.vpc.vpc_id
  app_name      = var.app_name
  key_name      = var.public_key_name
  instance_ami  = var.instance_ami
  environment   = var.environment
  public_subnet = module.vpc.public_subnets
  cidr_source_ip = local.cidr_source_ip
  providers = {
    aws = aws
  }
}