variable "environment" {
  description = "The environment name"
}

variable "vpc_id" {
  description = "The VPC of the network"
}

variable "public_subnet" {
  description = "The public subnets of the vpc"
  type = map(object({
    id = string
  }))
}

variable "app_name" {
  description = "The name of the app you want to create"
}

variable "key_name" {
  description = "The public key SSH, make sure you have the private key"
}

variable "instance_ami" {
  description = "The ami of of the image on AWS, check the region official AMI's"
}

variable "instance_instance_type" {
  description = "The type of the instance, t2.micro, t2.medium..."
  default     = "t3.medium"

}

variable "cidr_source_ip" {
  description = "Which ip can ssh to the machine app"
}