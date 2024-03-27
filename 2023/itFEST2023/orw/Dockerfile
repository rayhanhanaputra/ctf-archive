FROM ubuntu:23.10
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y libglib2.0-dev gcc gdb libc6-dbg xinetd
RUN groupadd -r ctf && useradd -r -g ctf ctf

ADD orw /home/ctf/chall

RUN echo '#!/bin/bash\nservice xinetd restart && /bin/sleep infinity' > /etc/init.sh
RUN echo 'service ctf\n\ 
{\n\ 
    disable = no\n\ 
    socket_type = stream\n\ 
    protocol = tcp\n\ 
    wait = no\n\ 
    user = ctf\n\ 
    type = UNLISTED\n\ 
    port = 11337\n\ 
    bind = 0.0.0.0\n\ 
    server = /home/ctf/run\n\ 
}' > /etc/xinetd.d/ctf
RUN echo '#!/bin/bash\ncd /home/ctf && ./chall' > /home/ctf/run

RUN echo "STS23{__jgn_disubmit_ini_cuma_pajangan__}" > /home/ctf/flag.txt
RUN chmod 444 /home/ctf/flag.txt

RUN chmod 400 /etc/xinetd.d/ctf
RUN chmod 550 /home/ctf/chall /home/ctf/run /etc/init.sh

WORKDIR /home/ctf
RUN chown -R root:ctf /home/ctf
RUN service xinetd restart
