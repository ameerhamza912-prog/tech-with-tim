import urllib3
from bs4 import BeautifulSoup
http = urllib3.PoolManager()
r = http.request('GET', 'https://www.whatmobile.com.pk/Apple_Mobiles_Prices')
soup = BeautifulSoup(r.data, 'lxml')
print (soup.title)
print (soup.title.text)
prices = []
for a_tag in soup.find_all('span'): 
    #a_tag = li_tag.find('a')
    prices.append(a_tag.attrs['class'])
    #prices.append(a_tag.attrs['span'])
    #prices.append(a_tag.attrs['href'])
    #print(prices)
print(prices[:200])