terraform {
  required_version = ">= 1.1.3"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "4.3.0"
    }
  }
}

data "aws_region" "current" {}

resource "aws_security_group" "instance-sg" {
  description = "Security group for ${var.app_name}"
  vpc_id      = var.vpc_id
  tags = {
    Name        = "${data.aws_region.current.name}-${var.environment}-${var.app_name}-instance-security-group"
    Environment = var.environment
    Region      = data.aws_region.current.name
  }
}

resource "aws_security_group" "alb-sg" {
  description = "Security group for ${var.app_name}"
  vpc_id      = var.vpc_id
  tags = {
    Name        = "${data.aws_region.current.name}-${var.environment}-${var.app_name}-alb-security-group"
    Environment = var.environment
    Region      = data.aws_region.current.name
    VPC_ID      = var.vpc_id
  }
}

resource "aws_security_group_rule" "instance-sg-rule-egress" {
  description       = "Allow bastion to communicate with the world"
  security_group_id = aws_security_group.instance-sg.id
  cidr_blocks       = ["0.0.0.0/0"]
  type              = "egress"
  from_port         = "0"
  to_port           = "65535"
  protocol          = "-1"
}

resource "aws_security_group_rule" "instance-ssh-ingress" {
  description       = "access to instance host for alb"
  security_group_id = aws_security_group.instance-sg.id
  cidr_blocks       = [var.cidr_source_ip]
  type              = "ingress"
  from_port         = "22"
  to_port           = "22"
  protocol          = "tcp"
}

resource "aws_security_group_rule" "instance-2-alb-ingress" {
  description              = "Access to instance from alb to all"
  security_group_id        = aws_security_group.instance-sg.id
  source_security_group_id = aws_security_group.alb-sg.id
  type                     = "ingress"
  from_port                = "0"
  to_port                  = "65535"
  protocol                 = "tcp"
}

resource "aws_security_group_rule" "alb-from-world" {
  description       = "Access to alb from all"
  security_group_id = aws_security_group.alb-sg.id
  cidr_blocks       = ["0.0.0.0/0"]
  type              = "ingress"
  from_port         = "0"
  to_port           = "65535"
  protocol          = "-1"
}

resource "aws_security_group_rule" "alb-2-world" {
  description       = "Access alb to all"
  security_group_id = aws_security_group.alb-sg.id
  cidr_blocks       = ["0.0.0.0/0"]
  type              = "egress"
  from_port         = "0"
  to_port           = "65535"
  protocol          = "-1"
}

data "template_file" "user-data" {
  template = file("${path.module}/../../../templates/instance_user_date.sh")
  vars = {
    region      = data.aws_region.current.name
    environment = var.environment
    app_name    = var.app_name
  }
}

resource "aws_launch_configuration" "instance-launch-configuration" {
  name                        = "${data.aws_region.current.name}-${var.environment}-${var.app_name}-launch-configuration-${formatdate("YYYY-MM-DD-HH-mm", timeadd(timestamp(), "24h"))}"
  key_name                    = var.key_name
  image_id                    = var.instance_ami
  instance_type               = var.instance_instance_type
  user_data                   = data.template_file.user-data.rendered
  associate_public_ip_address = true
  security_groups             = [aws_security_group.instance-sg.id]
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
  name                 = "${data.aws_region.current.name}-${var.environment}-${var.app_name}"
  min_size             = 1
  desired_capacity     = 1
  max_size             = 1
  launch_configuration = aws_launch_configuration.instance-launch-configuration.name
  vpc_zone_identifier  = [for k, subnet in var.public_subnet : subnet.id]
  tag {
    key                 = "Environment"
    value               = var.environment
    propagate_at_launch = true
  }
  tag {
    key                 = "Region"
    value               = data.aws_region.current.name
    propagate_at_launch = true
  }
  lifecycle {
    ignore_changes = [load_balancers]
  }
}

data "aws_instances" "instance-data" {
  instance_tags = {
    Name     = "${data.aws_region.current.name}-${var.environment}-${var.app_name}-instance"
    image_id = var.instance_ami
  }
  depends_on = [aws_autoscaling_group.instance-auto-scaling-group]
}

resource "aws_lb" "app-alb" {
  name                       = "${data.aws_region.current.name}-${var.environment}-${var.app_name}-alb"
  internal                   = false
  load_balancer_type         = "application"
  security_groups            = [aws_security_group.alb-sg.id]
  subnets                    = [for subnet in var.public_subnet : subnet.id]
  enable_deletion_protection = false
  tags = {
    Environment = var.environment
    Region      = data.aws_region.current.name
    app         = var.app_name
  }
}

resource "aws_lb_target_group" "app-alb-target-group" {
  name     = "${data.aws_region.current.name}-${var.environment}-${var.app_name}-tg"
  port     = 5000
  protocol = "HTTP"
  vpc_id   = var.vpc_id
  health_check {
    healthy_threshold   = 5
    interval            = 10
    path                = "/"
    port                = "5000"
    protocol            = "HTTP"
    unhealthy_threshold = 3
  }
}

resource "aws_autoscaling_attachment" "asg-alb-attachment" {
  autoscaling_group_name = aws_autoscaling_group.instance-auto-scaling-group.name
  lb_target_group_arn    = aws_lb_target_group.app-alb-target-group.arn
}

resource "aws_lb_listener" "app_alb_listener_http" {
  load_balancer_arn = aws_lb.app-alb.id
  port              = "5000"
  protocol          = "HTTP"

  default_action {
    target_group_arn = aws_lb_target_group.app-alb-target-group.id
    type             = "forward"
  }
}