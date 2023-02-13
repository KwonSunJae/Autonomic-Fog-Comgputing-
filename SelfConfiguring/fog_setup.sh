#!/bin/bash
sudo apt-get remove -y docker docker-engine docker.io containerd runc
sudo snap install -y docker

curl -sfL https://get.k3s.io | sh -

sudo apt install -y nginx
sudo rm /etc/nginx/sites-enabled/default
sudo service nginx restart
sudo systemctl stop/start/enable nginx.service
sudo groupadd prometheus
sudo useradd -s /sbin/nologin --system -g prometheus prometheus
sudo mkdir /var/lib/prometheus
sudo for i in rules rules.d files_sd; do sudo mkdir -p /etc/prometheus/${i}; done
sudo apt install -y curl
sudo mkdir -p /tmp/prometheus
sudo cd /tmp/prometheus
sudo curl -s https://api.github.com/re
pos/prometheus/prometheus/releases/latest | grep browser_download_url | grep linux-amd64 | cut -d '"' -f 4 | wget -qi –
sudo tar xvf prometheus*.tar.gz
sudo cd /tmp/prometheus/prometheus-2.38.0.linux-amd64
sudo mv prometheus promtool /usr/local/bin/
sudo mv prometheus.yml /etc/prometheus/prometheus.yml
sudo mv consoles/ console_libraries/ /etc/prometheus/
sudo nano /etc/prometheus/prometheus.yml
sudo cat  >> /etc/systemd/system/prometheus.service << EOF
[Unit]
Description=Prometheus #Description
Documentation=https://prometheus.io/docs/introduction/overview/ #reference to documentation
Wants=network-online.target
After=network-online.target
[Service]
Type=simple
User=prometheus #user
Group=prometheus #group
ExecReload=/bin/kill -HUP \$MAINPID
ExecStart=/usr/local/bin/prometheus \
--config.file=/etc/prometheus/prometheus.yml \ #main config
--storage.tsdb.path=/var/lib/prometheus \ #database
--web.console.templates=/etc/prometheus/consoles \
--web.console.libraries=/etc/prometheus/console_libraries \
--web.listen-address=0.0.0.0:9090 \
--web.external-url=
SyslogIdentifier=prometheus #name of log file
Restart=always #enable restart
[Install]
WantedBy=multi-user.target
EOF
for i in rules rules.d files_sd; do sudo chown -R prometheus:prometheus /etc/prometheus/${i}; done
for i in rules rules.d files_sd; do sudo chmod -R 775 /etc/prometheus/${i}; done
sudo chown -R prometheus:prometheus /var/lib/prometheus/
systemctl daemon-reload
systemctl start/enable prometheus

sudo ufw allow in "Nginx Full"
sudo ufw allow 9090/tcp