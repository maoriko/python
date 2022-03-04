output "instance_security_group_id" {
  value = aws_security_group.instance-sg.id
}

output "instance_security_group_name" {
  value = aws_security_group.instance-sg.tags.Name
}

output "alb_security_group_id" {
  value = aws_security_group.alb-sg.id
}

output "alb_security_group_name" {
  value = aws_security_group.alb-sg.tags.Name
}

output "instance_launch_configuration_id" {
  value = aws_launch_configuration.instance-launch-configuration.id
}

output "instance_launch_configuration_name" {
  value = aws_launch_configuration.instance-launch-configuration.name
}

output "instance_auto_scaling_group_id" {
  value = aws_autoscaling_group.instance-auto-scaling-group.id
}

output "instance_auto_scaling_group_name" {
  value = aws_autoscaling_group.instance-auto-scaling-group.name
}

output "alb_name" {
  value = aws_lb.app-alb.name
}

output "alb_address" {
  value = aws_lb.app-alb.dns_name
}

output "instance_target_group_name" {
  value = aws_lb_target_group.app-alb-target-group.name
}

