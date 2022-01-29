import requests
import pprintpp
from bs4 import BeautifulSoup

html = requests.get("https://mcdonalds.com.pk/our-menu/").text

soup = BeautifulSoup(html, 'html.parser')
print(soup.findAll('div', {"class": "content-title"})) 
#print(soup.prettify())
#print(html.text)