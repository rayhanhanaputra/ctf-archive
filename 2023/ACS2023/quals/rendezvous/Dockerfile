FROM ubuntu@sha256:b492494d8e0113c4ad3fe4528a4b5ff89faa5331f7d52c5c138196f69ce176a6
ARG BUILD_UID=1000
ARG BUILD_GID=1000

RUN apt-get update && apt-get install -y socat

RUN groupadd -g ${BUILD_GID} user
RUN useradd -u ${BUILD_UID} -g ${BUILD_GID} -s /sbin/nologin user
WORKDIR /home/user

COPY ./service-rendezvous/rendezvous ./rendezvous
COPY ./service-rendezvous/flag ./flag
RUN chown -R root:user /home/user
RUN chmod 550 ./rendezvous
RUN chmod 440 ./flag

CMD socat TCP-LISTEN:54321,reuseaddr,fork EXEC:"su -s /bin/sh - user -c /home/user/rendezvous"