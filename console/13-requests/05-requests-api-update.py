#Updating Record on Server using Web-API

import requests
import json

id=input("Enter Id to Update Record : ")

#API-Endpoint
url="https://web-rest-api.herokuapp.com/student/update/"+id

#Post Data
postdata={}
postdata["course"]=input("Enter Course : ")

#Send Request
response=requests.put(url,json.dumps(postdata))

#Fetch Result
data=response.json()

#Process Result
print(data)
