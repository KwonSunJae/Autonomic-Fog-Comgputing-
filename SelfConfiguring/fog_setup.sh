#!/bin/bash
sudo apt-get remove -y docker docker-engine docker.io containerd runc
sudo snap install -y docker
sudo apt-get install -y prometheus prometheus-node-exporter
curl -sfL https://get.k3s.io | sh -
sudo apt install -y nginx
sudo ufw allow in "Nginx Full"
sudo ufw allow 9090/tcp