import requests
from bs4 import BeautifulSoup 


result = requests.get('https://www.youtube.com/results?search_query=ary+news')
htmx_doc =BeautifulSoup (result.content)
#soup = BeautifulSoup(htmx_doc,'lxml')
#print(htmx_doc.prettify())
# import pdb
# print(htmx_doc)
# print(htmx_doc.title)
# pdb.set_trace()
# print(htmx_doc.title.string)
# print(htmx_doc.title.parent.name)
# print(htmx_doc.a)
# print(htmx_doc.find_all('a'))
#print(htmx_doc.find(id="link3"))

rows = htmx_doc.findAll('tr')[1]

print(rows)
