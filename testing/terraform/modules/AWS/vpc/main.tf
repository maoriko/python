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

locals {
  vpc_name  = "${data.aws_region.current.name}-${var.environment}-vpc"
  subnets_cidrs = {
    (var.availability_zones[0]) : {
      "public_subnet" : "10.0.0.0/24"
    },
    (var.availability_zones[1]) : {
      "public_subnet" : "10.0.1.0/24"
    }
  }
}

# ---------------- VPC ----------------------
resource "aws_vpc" "vpc" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_support   = true
  enable_dns_hostnames = true
  tags = {
    Name     = local.vpc_name
    Environment = var.environment
    Region = data.aws_region.current.name
  }
}

# --------------- IGW -----------------------
resource "aws_internet_gateway" "vpc-gw" {
  vpc_id = aws_vpc.vpc.id
  tags = {
    Name = "${local.vpc_name}-igw"
    Environment = var.environment
    Region = data.aws_region.current.name
  }
}

# ----------- Elastic IPs -------------------
resource "aws_eip" "ngw-eips" {
  for_each   = local.subnets_cidrs
  vpc        = true
  depends_on = [aws_internet_gateway.vpc-gw]
  tags = {
    Name = "${data.aws_region.current.name}-${var.environment}-ngw-${each.key}-eip"
    Environment = var.environment
    Region = data.aws_region.current.name
  }
}

# ------------- Subnets ---------------------
resource "aws_subnet" "public-subnets" {
  for_each          = local.subnets_cidrs
  availability_zone = each.key
  cidr_block        = each.value.public_subnet
  vpc_id            = aws_vpc.vpc.id
  map_public_ip_on_launch = true
  tags = {
    Name  = "${data.aws_region.current.name}-${var.environment}-public-subnet-${each.key}"
    Environment = var.environment
    Region = data.aws_region.current.name
  }
}

# ------------ NAT Gateways -----------------
resource "aws_nat_gateway" "nat-gateways" {
  for_each      = local.subnets_cidrs
  allocation_id = aws_eip.ngw-eips[each.key].id
  subnet_id     = aws_subnet.public-subnets[each.key].id
  tags = {
    Name = "${data.aws_region.current.name}-${var.environment}-nat-gateway-${each.key}"
    Environment = var.environment
    Region = data.aws_region.current.name
  }
}

# ------------ Route Tables -----------------
resource "aws_route_table" "public-route-table" {
  vpc_id = aws_vpc.vpc.id
  tags = {
    Name    = "${data.aws_region.current.name}-${var.environment}-public-route-table"
    Network = "Public"
    Environment = var.environment
    Region = data.aws_region.current.name
  }
}

resource "aws_route" "public-route" {
  route_table_id         = aws_route_table.public-route-table.id
  gateway_id             = aws_internet_gateway.vpc-gw.id
  destination_cidr_block = "0.0.0.0/0"
}