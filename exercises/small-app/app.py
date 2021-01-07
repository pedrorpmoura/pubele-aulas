from flask import Flask, render_template, request, redirect
import requests
import json

import db_proverbios

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')



@app.route('/proverbios', methods=['GET'])
def get_proverbios():
    res = requests.get('http://localhost:5000/api/proverbios')
    ps = json.loads(res.content)
    print(ps)

    return render_template('proverbios_view.html', proverbios=ps)



@app.route('/proverbios', methods=['POST'])
def post_proverbio():
    data = dict(request.form)
    print(data)
    requests.post('http://localhost:5000/api/proverbios', data=data)


    return redirect('http://localhost:5000/proverbios')



@app.route('/proverbios/<proverbio>', methods=['GET'])
def get_proverbio(proverbio):
    res = requests.get('http://localhost:5000/api/proverbios/' + proverbio)

    p = json.loads(res.content)
    return render_template('proverbio_view.html', p=p)




# API
@app.route('/api/proverbios', methods=['GET'])
def api_get_proverbios():
    ps = db_proverbios.find_all()
    return json.dumps(ps)


@app.route('/api/proverbios', methods=['POST'])
def api_post_proverbio():
    
    data = dict(request.form)
    db_proverbios.insert(data)

    return json.dumps(db_proverbios.find_all())


@app.route('/api/proverbios/<proverbio>', methods=['GET'])
def api_get_proverbio(proverbio):
    p = db_proverbios.find_one(proverbio)
    return json.dumps(p)



"""
{numero}: {
    "nome": {nome},
    "idade": {idade},
    "sexo": {sexo},
    "curso": {curso}
}

"""




pessoas = {
    "pg41094": {
        "nome": "Pedro",
        "idade": 22,
        "sexo": "Masculino",
        "curso": "MEI"
    },
    "a88888": {
        "nome": "Sara",
        "idade": 22,
        "sexo": "Feminino",
        "curso": "Nutrição"
    }
}

# ==>

pessoasl = [
    { "numero": "pg41094", "nome": "Pedro"},
    { "numero": "a88888" , "nome": "Sara" }
]

# Pessoas
@app.route('/pessoas', methods=['GET'])
def get_pessoas():

    res = requests.get('http://localhost:5000/api/pessoas')
    ps = json.loads(res.content)
    return render_template('pessoas_view.html', title='Pessoas', pessoas=ps)


@app.route('/pessoas/<numero>', methods=['GET'])
def get_pessoa(numero):

    res = requests.get('http://localhost:5000/api/pessoas/%s' % numero)
    p = json.loads(res.content)
    return render_template('pessoa_view.html', pessoa=p)



import db_pessoas

# API
@app.route('/api/pessoas', methods=['GET'])
def api_get_pessoas():

    ps = db_pessoas.find_all()

    return json.dumps(ps)



@app.route('/api/pessoas/<numero>', methods=['GET'])
def api_get_pessoa(numero):

    d = pessoas[numero]
    d['numero'] = numero
    
    return json.dumps(d)


@app.route('/api/pessoas', methods=['POST'])
def api_post_pessoa():

    data = dict(request.form)
    db_pessoas.insert(data)

    return data








