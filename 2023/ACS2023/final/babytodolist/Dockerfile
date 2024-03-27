FROM ubuntu:20.04

ARG DEBIAN_FRONTEND=noninteractive

RUN sed -i 's/archive.ubuntu.com/mirror.kakao.com/g' /etc/apt/sources.list \
    && apt-get update
	
ENV TZ=Asia/Seoul
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get upgrade -yq
RUN apt-get install -yq apache2 curl wget unzip 
RUN apt-get install -yq php7.4 php7.4-mysql libapache2-mod-php7.4

RUN a2enmod rewrite
EXPOSE 80

COPY ./flag /flag

ENTRYPOINT [ "/usr/sbin/apache2ctl", "-D", "FOREGROUND" ]