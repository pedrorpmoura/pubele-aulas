from flask import Flask, render_template
import json
import requests

import random

from bd import proverbios, pessoas

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/proverbios')
def proverbios_api():
    return json.dumps(proverbios)

@app.route('/proverbios')
def proverbios_view():
    res = requests.get('http://localhost:5000/api/proverbios')
    ps = json.loads(res.content)
    return render_template('proverbios_view.html', title='Proverbios', proverbios=ps)


@app.route('/proverbios/proverbio/<id_>')
def proverbio_view(id_):
    return render_template('proverbio_view.html', p = proverbios[int(id_)])


@app.route('/proverbios/semana')
def semana():
    p = random.choice(proverbios)
    return render_template('proverbio_semana_view.html', proverbio=p)


@app.route('/pessoas')
def pessoas_view():
    return render_template('pessoas_view.html', title='Pessoas', pessoas=pessoas)








