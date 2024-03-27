FROM ubuntu:20.04
ARG DEBIAN_FRONTEND=noninteractive


WORKDIR /var/www/html

RUN apt-get update

RUN apt-get upgrade -y
RUN apt-get install git wget curl unzip apache2 php php-fpm php-mysql php-curl php-gd php-json php-xml php-mbstring php-zip composer -y

RUN wget http://start.xpressengine.io/download/3.0.14.zip
RUN unzip 3.0.14.zip && chmod -R 707 storage/ bootstrap/ config/ vendor/ plugins/ index.php composer.phar


RUN rm -rf /var/www/html/3.0.14.zip /var/www/html/index.html

RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf
RUN sed -i 's/AllowOverride None/AllowOverride All/g' /etc/apache2/apache2.conf
RUN a2enmod rewrite
RUN service apache2 restart

ADD entrypoint.sh /
RUN chmod +x /entrypoint.sh
CMD /entrypoint.sh