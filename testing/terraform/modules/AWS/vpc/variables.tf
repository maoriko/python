variable "environment" {
  description = "The environment's name"
}

variable "availability_zones" {
  description = "AZs"
  type        = list(string)
}