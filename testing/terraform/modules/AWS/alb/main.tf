terraform {
  required_version = ">= 1.1.3"
  aws = {
    source  = "hashicorp/aws"
    version = "4.3.0"
  }
}

data "aws_region" "current" {}

data "template_file" "user-data" {
  template = file("${path.module}/../../../templates/instance-user-data.sh")
  vars = {
    environment = var.environment
    region      = data.aws_region.current.name
  }
}

resource "aws_security_group" "instance-sg" {
  description = "Security group for ${var.app_name}"
  vpc_id      = var.vpc_id
  tags = {
    Name = "${data.aws_region.current.name}-${var.environment}-${var.app_name}-security-group"
    Environment = var.environment
    Region = data.aws_region.current.name
  }
}

resource "aws_launch_configuration" "instance-launch-configuration" {
  name_prefix                 = "${data.aws_region.current.name}-${var.environment}-${var.app_name}-launch-configuration-${formatdate("YYYY-MM-DD-HH-mm", timeadd(timestamp(), "24h"))}"
  key_name                    = var.key_name
  image_id                    = var.instance_ami
  instance_type               = var.instance_instance_type
  user_data                   = data.template_file.user-data.rendered
  security_groups = [
    aws_security_group.instance-sg.id
  ]

#  connection {
#
#  }
  root_block_device {
    delete_on_termination = true
    volume_size           = 30
    volume_type           = "gp2"
  }
  lifecycle {
    create_before_destroy = true
  }
}
resource "aws_autoscaling_group" "instance-auto-scaling-group" {
  name                      = "${data.aws_region.current.name}-${var.environment}-${var.app_name}"
  min_size                  = 1
  desired_capacity          = 1
  max_size                  = 1
#  health_check_type         = "ELB"
#  health_check_grace_period = 600
  launch_configuration      = aws_launch_configuration.instance-launch-configuration.name
  vpc_zone_identifier = [for k, subnet in var.public_subnet : subnet.id]
  tags = [
    {
      key                 = "Environment"
      value               = var.environment
      propagate_at_launch = true
    },
    {
      key                 = "Region"
      value               = data.aws_region.current.name
      propagate_at_launch = true
    }
  ]
  lifecycle {
    ignore_changes = [load_balancers]
  }
}

#resource "aws_lb" "test" {
#  name               = "${data.aws_region.current.name}-${var.environment}-${var.app_name}-alb"
#  internal           = false
#  load_balancer_type = "application"
#  security_groups    = [aws_security_group.lb_sg.id]
#  subnets            = [for subnet in var.public_subnet : subnet.id]
#  enable_deletion_protection = false
#  tags = {
#    Environment = var.environment
#  }
#}