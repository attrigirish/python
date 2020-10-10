#Fetching Records from Server using Web-API

import requests

#API-Endpoint
url="https://web-rest-api.herokuapp.com/students"

#Send Request
response=requests.get(url)

#Fetch Data
records=response.json()

#Process Result
for record in records:
    print("ID : ", record['id'])
    print("Name : ", record['name'])
    print("Course : ", record['course'])
    print("Fees : ", record['fees'])

    print()    
