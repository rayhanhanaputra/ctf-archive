FROM node:slim

RUN apt-get update && apt-get install curl gnupg -y \
    && curl --location --silent https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list' \
    && apt-get update \
    && apt-get install google-chrome-stable -y --no-install-recommends \
    && apt-get install -y supervisor \
    && rm -rf /var/lib/apt/lists/*
    
RUN mkdir -p /app

WORKDIR /app
COPY challenge .

RUN npm install

COPY config/supervisord.conf /etc/supervisord.conf

EXPOSE 55213

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]



