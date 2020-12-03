from flask import Flask, render_template

import random

app = Flask(__name__)


proverbios = [
    'Mais vale tarde do que nunca.',
    'Mês de abril, arroz de caril.',
    'Quem vai à guerra dá e leva'
]


pessoas = [
    'Pedro',
    'Beatriz',
    'Paulo'
] 


@app.route('/')
def index():
    return render_template('proverbios_view.html', title='Proverbios', proverbios=proverbios)


@app.route('/semana')
def semana():
    p = random.choice(proverbios)
    return render_template('proverbio_semana_view.html', proverbio=p)


@app.route('/pessoas')
def pessoas_view():
    return render_template('pessoas_view.html', title='Pessoas', pessoas=pessoas)








