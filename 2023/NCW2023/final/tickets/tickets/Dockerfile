FROM wordpress:latest

COPY flag /flag
RUN chmod 400 /flag
COPY readflag /readflag
RUN chmod u+s /readflag

WORKDIR /var/www/html

COPY .htaccess /var/www/html/.htaccess

RUN curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar && \
    chmod +x wp-cli.phar && \
    mv wp-cli.phar /usr/local/bin/wp

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

VOLUME /var/www/html

EXPOSE 80

ENV WORDPRESS_DB_HOST=db
ENV WORDPRESS_DB_USER=wordpress
ENV WORDPRESS_DB_PASSWORD=redacted
ENV WORDPRESS_DB_NAME=wordpress

ENV WP_ADM_USER=admin
ENV WP_ADM_PASSWORD=redacted
ENV WP_ADM_EMAIL=admin@ncw2k23.com
ENV WP_HOST=localhost

USER www-data

ENTRYPOINT [ "/bin/bash", "/entrypoint.sh" ]
