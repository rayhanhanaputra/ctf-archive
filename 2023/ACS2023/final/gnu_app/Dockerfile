FROM ubuntu:20.04
ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y wget curl apache2 php-gd php-mysql php

COPY gnuboard5.5.8.2.5.tar.gz /tmp/gnuboard5.5.8.2.5.tar.gz
RUN tar -xvf /tmp/gnuboard5.5.8.2.5.tar.gz -C /var/www/html
RUN rm /tmp/gnuboard5.5.8.2.5.tar.gz

RUN sed -i 's/AllowOverride None/AllowOverride All/g' /etc/apache2/apache2.conf

WORKDIR /var/www/html

RUN mkdir data
RUN chmod 777 data



ADD entrypoint.sh /
RUN chmod +x /entrypoint.sh
CMD /entrypoint.sh