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

resource "aws_launch_configuration" "bastion-launch-configuration" {
  name_prefix                 = "${var.cluster_name}-bastion-launch-configuration-"
  associate_public_ip_address = true
  key_name                    = var.key_name
  image_id                    = var.bastion_ami
  instance_type               = var.bastion_instance_type
  user_data                   = data.template_file.user-data.rendered
  iam_instance_profile        = aws_iam_instance_profile.bastion-instance-profile.name
  security_groups = [
    aws_security_group.bastion-sg.id
  ]

  root_block_device {
    delete_on_termination = true
    volume_size           = 30
    volume_type           = "gp2"

  }
  lifecycle {
    create_before_destroy = true
  }
}
resource "aws_autoscaling_group" "bastion" {
  name                      = "${data.aws_region.current.name}-${var.environment}-${var.app_name}"
  min_size                  = 1
  desired_capacity          = 1
  max_size                  = 1
  health_check_type         = "ELB"
  health_check_grace_period = 600
  launch_configuration      = aws_launch_configuration.bastion-launch-configuration.name
  vpc_zone_identifier = [
  for k, subnet in
  var.public_subet : subnet.id
  ]
  tags = [
    {
      key                 = "environment"
      value               = var.environment
      propagate_at_launch = true
    },
    {
      key                 = "region"
      value               = data.aws_region.current.name
      propagate_at_launch = true
    }
  ]
  lifecycle {
    ignore_changes = [load_balancers]
  }
}

resource "aws_lb" "test" {
  name               = "test-lb-tf"
  internal           = false
  load_balancer_type = "application"
  security_groups    = [aws_security_group.lb_sg.id]
  subnets            = [for subnet in var.public_subnet : subnet.id]
  enable_deletion_protection = false
  tags = {
    Environment = var.environment
  }
}