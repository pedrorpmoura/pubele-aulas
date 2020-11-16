import lxml
from bs4 import BeautifulSoup as bs

file = "catalogo.xml"
with open(file) as f:
    d=f.read()

ad = bs(d, "xml")

for i in ad.find_all("relations"):
    i.name = "ul"
    for j in i.find_all("rel"):
        j.name = "li"
        j.contents.append("batatas")
print(ad)
    

