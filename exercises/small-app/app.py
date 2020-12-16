from flask import Flask, render_template, request, redirect
import requests
import json

import db

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')



@app.route('/proverbios', methods=['GET'])
def get_proverbios():
    res = requests.get('http://localhost:5000/api/proverbios')
    ps = json.loads(res.content)

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
    ps = db.find_all()
    return json.dumps(ps)


@app.route('/api/proverbios', methods=['POST'])
def api_post_proverbio():
    
    data = dict(request.form)
    db.insert(data)

    return json.dumps(db.find_all())


@app.route('/api/proverbios/<proverbio>', methods=['GET'])
def api_get_proverbio(proverbio):
    p = db.find_one(proverbio)
    return json.dumps(p)


