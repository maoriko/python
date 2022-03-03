output "vpc_id" {
  description = "The VPC id"
  value       = aws_vpc.vpc.id
}

output "vpc_name" {
  description = "The VPC name"
  value = aws_vpc.vpc.tags.Name
}

output "public_subnets" {
  description = "The public subnets"
  value       = aws_subnet.public-subnets
}

output "nat_gateway_public_ip_address" {
  value = values(aws_nat_gateway.nat-gateways)[*].public_ip
}

output "nat_gateway_private_ip_address" {
  value = values(aws_nat_gateway.nat-gateways)[*].private_ip
}