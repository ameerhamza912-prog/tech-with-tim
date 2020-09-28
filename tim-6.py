import requests
from bs4 import BeautifulSoup 
import csv
import html5lib
URL = 'http://lgu.edu.pk/merit_list.php/'
r = requests.get(URL)
soup = BeautifulSoup(r.content,'html.parser')
#print(soup.prettify()) 
#print(list(soup.children))
#print([type(item) for item in list(soup.children)])
html = list(soup.children)[2]
#print(html)
#body = list(html.children)[3]
#p = list(body.children)[1]
#p.get_text()
print(soup.find_all('a', class_ ='ui-title-block'))