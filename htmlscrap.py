import requests
import lxml.html as lh


url='http://pokemondb.net/pokedex/all'
#Create a handle, page, to handle the contents of the website
page = requests.get(url)
#Store the contents of the website under doc
doc = lh.fromstring(page.content)
print(doc)
import pdb 
pdb.set_trace()
#Parse data that are stored between <tr>..</tr> of HTML
tr_elements = doc.xpath('//tr')
print(tr_elements)
#Create empty list
col=[]
i=0
#For each row, store each first element (header) and an empty list
for t in tr_elements[0]:
    i+=1
    name=t.text_content()
    # print '%d:"%s"' %(i,name)
    print(i,name)
    col.append((name,[]))
