FROM python:3.10.6

RUN apt-get update

RUN pip install --upgrade mongoengine blacksheep uvicorn passlib pycryptodome pytz urllib3 requests
RUN useradd -rm -d /home/ctf -s /bin/bash -u 1000 ctf

COPY ./src /home/ctf/src
COPY ./flag.txt /flag.txt

USER ctf

WORKDIR /home/ctf/src

CMD [ "uvicorn", "server:app", "--host", "0.0.0.0"]