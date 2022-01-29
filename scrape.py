import requests
from bs4 import BeautifulSoup

html = requests.get("https://mcdonalds.com.pk/our-menu/")

soup = BeautifulSoup(html, 'html.parser')
#soup.findAll('div') 
print(soup.prettify())
#print(html.text)