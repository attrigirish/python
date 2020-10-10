#Adding Record on Server using Web-API

import requests
import json

#API-Endpoint
url="https://web-rest-api.herokuapp.com/student/create"

#Post Data
postdata={}
postdata["name"]=input("Enter Name : ")
postdata["course"]=input("Enter Course : ")
postdata["fees"]=input("Enter Fees : ")

#Send Request
response=requests.post(url,json.dumps(postdata))

#Fetch Result
data=response.json()

#Process Result
print(data)
