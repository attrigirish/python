#requests module

import requests

#URL
url="https://easykart.herokuapp.com/"

#Send Request
response=requests.get(url)

#Fetch Response Details
print("Status Code : ", response.status_code)
print("Headers : ", response.headers)
print("Connection : ", response.connection)
print("Data : ", response.text)
