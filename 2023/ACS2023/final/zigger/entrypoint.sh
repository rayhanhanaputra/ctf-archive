#!/bin/bash

password="$(head -100 /dev/urandom | sha256sum | cut -d' ' -f1|cut -c 1-20)"

service apache2 start

while :; do
  if curl 'http://192.168.8.131:22030/install/step4.php' -X POST --data-raw "engine=mysql&host=db&name=zigger&user=zigger&pwd=zigger&pfx=ph_" 2>/dev/null | grep -q 'Installation'; then
  if curl 'http://192.168.8.131:22030/install/finish.php' -X POST --data-raw "name=admin&id=admin&pwd=$password&pwd2=$password" 2>/dev/null | grep -q 'finish'; then
    break
  fi
  fi
done

sleep inf
