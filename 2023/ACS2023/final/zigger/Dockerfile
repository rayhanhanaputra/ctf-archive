FROM ubuntu:20.04
ARG DEBIAN_FRONTEND=noninteractive


WORKDIR /var/www/html

RUN apt-get update

RUN apt-get upgrade -y
RUN apt-get install git wget curl unzip apache2 php php-fpm php-mysql php-curl php-gd php-json php-xml php-mbstring php-zip composer -y


RUN wget https://website-attach.cdn-server.zigger.net/zigger-core-download/zigger-source-ver.2.4.3.tar.gz --no-check-certificate
RUN tar -xvf zigger-source-ver.2.4.3.tar.gz && chmod 707 data/ robots.txt


RUN rm -rf /var/www/html/zigger-source-ver.2.4.3.tar.gz
RUN rm -rf /var/www/html/index.html

# RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf
RUN sed -i 's/AllowOverride None/AllowOverride All/g' /etc/apache2/apache2.conf
RUN sed -i 's/short_open_tag = Off/short_open_tag = On/g' /etc/php/7.4/apache2/php.ini
RUN a2enmod rewrite
RUN service apache2 restart

ADD entrypoint.sh /
RUN chmod +x /entrypoint.sh
CMD /entrypoint.sh