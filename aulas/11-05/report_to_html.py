from re import *
import jinja2  as j2




def extract(): # extrai a informação do relatório em XML

	with open("report.xml") as f:
		report=f.read()
	
	info=[]

	labels = findall(r'<.*>',report)

	for label in labels:
		chave=search(r'</(.*)>',label)
		v=search(r'>(.*)<',label)
		if v:
			#info[chave[1]] = v[1]
			info.append((chave[1],v[1]))

	print(info)


def extract2():

	with open("report.xml") as f:
		report=f.read()

	info = []

	for tag,miolo in findall(r'<(.*?)>(.*?)</\1>',report):
		info.append((tag,miolo))


	print(info)



# recebe uma lista com title,date,team e description e devolve um dicionário com a info xml dessas tags

def refile(filename): # devolve texto

	with open(filename) as f:
		report=f.read()

	return report


def extract_dict(l,report): # devolve dicionário

	info = {}
	for elem in l:
		v=search(rf"<{elem}>((?:.|\n)*?)</{elem}>",report)
		if v:
			info[elem]=v[1]

	return info


def extrai_listaH(xml,tag):

	info = []

	for miolo in findall(rf'<{tag}>((?:.|\n)*?)</{tag}>',xml):
		info.append(miolo)

	return info


def preenche2(info):

	t = j2.Template( """
<html>
<head>
  <title> {{title}} </title>
  <meta charset="UTF-8"/>
</head>
<body>
 <h1> {{title}} </h1>
 <p> {{date}} </p>
 <h2>Autores</h2>
 <hr/>
 <ol>
    {% for el in team  %}
      <li> {{el['name']}} : {{el['email']}} </li>
    {% endfor %}
 </ol>
 <hr/>
 <h2> Descrição </h2>
 <p> {{description}} </p>
</body>
</html>

""")

	print(t.render(info))


def main():
	
	#info = extract()
	f = refile('report.xml') 
	dic = extract_dict(['title','team','date','description'],f) 
	aux = extrai_listaH(dic['team'],'element')
	


	'''nova_lista = []
	for el in aux:
		res = extract_dict(['name','email'],el)
		nova_lista.append(res)
	dic['team'] = nova_lista'''
	
	# as últimas 5 linhas fazem o mesmo que esta linha seguinte
	
	dic['team'] = [extract_dict(['name','email'],el) for el in aux]
	preenche2(dic)
	

main()