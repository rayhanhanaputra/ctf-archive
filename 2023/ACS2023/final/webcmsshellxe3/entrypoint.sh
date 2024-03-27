#!/bin/bash

# password="$(head -100 /dev/urandom | sha256sum | cut -d' ' -f1)"

password="admin"

echo 'Require ip 127.0.0.1' >> /var/www/html/.htaccess

service apache2 start

while :; do
  if curl 'http://localhost/install/post' -X POST --data-raw "locale=ko&database_driver=mysql&database_host=db&database_port=&database_name=xe3&database_user_name=xe3&database_password=xe3&database_charset=&database_prefix=&web_url=http%3A%2F%2Flocalhost&web_timezone=Asia%2FSeoul&admin_email=admin%40admin.com&admin_login_id=admin&admin_display_name=admin&admin_password=$password&admin_password_confirmation=$password" 2>/dev/null | grep -q 'xeBaseURL'; then
    break
  fi
done

sed -i '$ d' /var/www/html/.htaccess

sleep inf
