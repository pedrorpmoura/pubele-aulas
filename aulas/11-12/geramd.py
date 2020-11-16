import lxml
from bs4 import BeautifulSoup as bs

file = "catalogo.xml"
with open(file) as f:
    d=f.read()

ad = bs(d, "xml")

for i in ad.find_all("title"):
    print("##",i.text)
    aux = i.parent.description
    aux2 = i.parent.resource
    if aux2:
        print(f'[link]({aux2.text})')
    if aux:
        print(aux.text)


