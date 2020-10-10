#Web Scrapping using Beautiful Soupt

import requests
from bs4 import BeautifulSoup

#URL
url="https://easykart.herokuapp.com"

#Send Request
response=requests.get(url)

#Fetch Data
data=response.content

#Parse Data
soup=BeautifulSoup(data,'html.parser')

#Fetch Content by Class Name
navbar_brand = soup.find(class_="navbar-brand")
print(navbar_brand)

#Fetch Content by Id
login=soup.find(id="login")
print(login)

#Fetch Content by Tag Name
images=soup.find_all('img')
print(images)

#Fetch Element Text
product_names=soup.find_all(class_='card-title')
for product_name in product_names:
    print(product_name.text)
