#!/bin/sh

hostname=$(ifconfig | grep -oE "\b([0-9]{1,3}\.){3}[0-9]{1,3}\b" | head -n1)
#hostnamectl set-hostname "$hostname"
export my_ip="$hostname"
export environment=$ENV

