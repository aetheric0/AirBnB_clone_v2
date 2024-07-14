#!/usr/bin/env bash
# Configures a new nginx server on Linux
if [command] then;
apt-get update
apt-get install nginx -y
mkdir -p /data/web_static/releases/test
mkdir /data/web_static/shared
cat << EOF > /data/web_static/releases/test/index.html
<html>
  <head></head>
  <body> Holberton School</body>
</html>
EOF
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
cat << EOF > /etc/nginx/sites-available/chrixeledu.tech
server {
    listen 80;
    server_name localhost;

    location /hbnb_static/ {
    alias /data/web_static/current/;
    }
}

EOF
ln -sf /etc/nginx/sites-available/chrixeledu.tech /etc/nginx/sites-enabled/
service nginx restart
