#!/bin/bash

sudo apt-get update && sudo apt-get install -y \
     vim \
     curl \
     ca-certificate \
     apt-transport-https \
     software-properties-common
     
sudo hostnamectl set-hostname "${region}-${environment}-${app_name}"

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -  
add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
   
sudo apt-get update && apt-get install -y \
     docker-ce
     
sudo usermod -aG docker ubuntu
sudo usermod -aG docker $whoami


curl -L https://github.com/docker/compose/releases/download/1.21.0/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

docker run --name=flask_app -p5000:5000 -d maorpaz/flask_app:latest