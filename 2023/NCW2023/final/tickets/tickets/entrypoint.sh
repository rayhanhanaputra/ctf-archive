#!/bin/bash
apache2ctl start & 2>/dev/null
running=false

health_check() {
    local url="http://localhost:80"
    local response=$(curl -s -o /dev/null -w "%{http_code}" "$url")
    if [ "$response" != "000" ]; then
        echo "Host is up. Configuring wordpress..."
        running=true
    else
        echo "Host is down. Restarting in 2 second..."
        sleep 2;
    fi
}

while ! $running; do
    health_check
done

wp core download --path=/var/www/html/
wp config create --dbhost=$WORDPRESS_DB_HOST --dbname=$WORDPRESS_DB_NAME --dbuser=$WORDPRESS_DB_USER --dbpass=$WORDPRESS_DB_PASSWORD
wp core install --url=$WP_HOST --title="National Cyber Week 2023" --admin_user=$WP_ADM_USER --admin_password=$WP_ADM_PASSWORD --admin_email=$WP_ADM_EMAIL
wp plugin install https://downloads.wordpress.org/plugin/support-genix-lite.1.1.9.zip
wp plugin activate support-genix-lite

apache2ctl stop

chown -R www-data /var/www/html

apache2-foreground