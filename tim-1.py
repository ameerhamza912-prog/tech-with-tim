import requests
from bs4 import BeautifulSoup
import csv


print(result.status_code)
#print(result.headers)
sourcs = result.content
soup = BeautifulSoup(sourcs,'lxml') 
prices = []
#price  = []
for li_tag in soup.find_all('li'): 
    a_tag = li_tag.find('a')
    prices.append(a_tag.attrs['title'])
    prices.append(a_tag.attrs['href'])
    prices.append(a_tag.attrs['span'])
    #b_tag = li_tag.find_all('span')
    #prices.append(b_tag.attrs['class'])
    
for i in range (len(prices)):
    print ("".format (i+1,prices[i]))    


print(prices)
prices.csv

