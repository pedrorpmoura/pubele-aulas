from flask import Flask, render_template, request
import json
import requests

import random

import shelve

from bd import proverbios, pessoas

app = Flask(__name__)


s = shelve.open('proverbios.db')


@app.route('/')
def index():
    return render_template('index.html')



@app.route('/api/proverbios')
def api_proverbios():
    ps = list(s.keys())
    return json.dumps(ps)


@app.route('/proverbios')
def proverbios_view():

    res = requests.get('http://localhost:5000/api/proverbios')
    ps = json.loads(res.content)

    return render_template('proverbios_view.html', title='Proverbios', proverbios=ps)


@app.route('/proverbios/novo', methods=['POST'])
def proverbios_novo():

    title = request.form.get('title')
    signi = request.form.get('significado')

    s[title] = signi
    s.sync()
    ps = list(s.keys())

    return render_template('proverbios_view.html', title='Proverbios', proverbios=ps)



@app.route('/proverbios/proverbio/<id_>')
def proverbio_view(id_):
    significado = s[id_]
    return render_template('proverbio_view.html', p = {'title': id_, 'significado': significado})


@app.route('/proverbios/semana')
def semana():

    p = random.choice(s.keys())
    return render_template('proverbio_semana_view.html', proverbio=p)


@app.route('/pessoas')
def pessoas_view():
    return render_template('pessoas_view.html', title='Pessoas', pessoas=pessoas)




