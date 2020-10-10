#Deleting Records from Web Server using Web API

import requests

id=input("Enter Id to Delete Record : ")

#API-Endpoint
url="https://web-rest-api.herokuapp.com/student/delete/" + id

#Send Request
response=requests.delete(url)

#Fetch Data
data=response.text

#Process Result
print(data)

