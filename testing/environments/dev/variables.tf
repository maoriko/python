variable "app_name" {
  description = "The application name to create"
  type = string
}

variable "environment" {
  description = "The environment's name"
  type = string
}

variable "region" {
  description = "The region to create the resources"
  type = string
}

variable "aws_profile" {
  description = "The aws profile to use"
  type = string
}

variable "public_key_name" {
  description = "The public key to use to connect the ec2 instance"
  type = string
}

variable "instance_ami" {
  description = "The AMI of the instance"
  type = string
}