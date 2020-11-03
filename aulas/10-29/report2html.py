from re import *
info={
"Title":"TPC1", 
"Date":"29/10/2020", 
"Team":'''<li>Beatriz Cepa<br>83813<br>cepabeatriz@gmail.com</li>
<li>Paulo Jorge<br>84480<br>paulojorgealves18@gmail.com</li>''',
"Description":"Descrição do TPC1"}

def extract():
    with open("reportxml.xml") as f:
        report=f.read()
    info={}
    v=search(r'<title>(.*)</title>',report)
    if v:
        info["Title"]=v[1] #v[0] dá a correspondencia toda para o search. v[1] dá só o match do (.*)
    v=search(r'<date>(.*)</date>',report)
    if v:
        info["Date"]=v[1] 

def subst(file,d):
    with open(file) as f:
        template=f.read()
    for key,value in d.items():
        template=sub(rf'#{key}',rf'{value}',template)
    return(template)

def main():
    #print(subst("template.html", info))
    extract()
main()




