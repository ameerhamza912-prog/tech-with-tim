import requests
from bs4 import BeautifulSoup 
import csv
import html5lib
URL = 'http://dataquestio.github.io/web-scraping-pages/simple.html'
r = requests.get(URL)
soup = BeautifulSoup(r.content,'html.parser')
#print(soup.prettify()) 
#print(list(soup.children))

#html = list(soup.children)[2]
#print([type(item) for item in list(soup.children)])
html = list(soup.children)[2]
body = list(html.children)[3]
p = list(body.children)[1]
#print(p.get_text())
soup.find_all('p')[0].get_text()

