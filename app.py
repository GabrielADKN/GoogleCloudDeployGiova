# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, jsonify, make_response
from flask_cors import CORS
from chat import get_response
from traduction import traduire
from langdetect import detect

app = Flask(__name__)
CORS(app, origins=["*"])

@app.route('/')
def index_get():
    return render_template("base.html")


@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    response = get_response(text)
    if detect(response) != 'fr':
        response = traduire(response,"en","fr")
    message = {"answer" : response}
    res = make_response(jsonify(message))
    #res.headers['Access-Control-Allow-Origin'] = '*'
    return res

@app.post("/predictEng")
def predictEng():
    text = request.get_json().get("message")
    if (text != "aucun son"):
        text = traduire(text,"en","fr")
    response = get_response(text)
    response = traduire(response,"fr","en")
    message = {"answer" : response}
    res = make_response(jsonify(message))
    #res.headers['Access-Control-Allow-Origin'] = '*'
    return res

@app.post("/predictEsp")
def predictEsp():
    text = request.get_json().get("message")
    if (text != "aucun son"):
        text = traduire(text,"es","fr")
    response = get_response(text)
    response = traduire(response,"fr","es")
    message = {"answer" : response}
    res = make_response(jsonify(message))
    #res.headers['Access-Control-Allow-Origin'] = '*'
    return res

@app.post("/predictDeu")
def predictDeu():
    text = request.get_json().get("message")
    if (text != "aucun son"):
        text = traduire(text,"de","fr")
    response = get_response(text)
    response = traduire(response,"fr","de")
    message = {"answer" : response}
    res = make_response(jsonify(message))
    #res.headers['Access-Control-Allow-Origin'] = '*'
    return res

@app.post("/predictChn")
def predictChn():
    text = request.get_json().get("message")
    if (text != "aucun son"):
        text = traduire(text,"zh-cn","fr")
    response = get_response(text)
    response = traduire(response,"fr","zh-cn")
    message = {"answer" : response}
    res = make_response(jsonify(message))
    #res.headers['Access-Control-Allow-Origin'] = '*'
    return res

@app.post("/predictHau")
def predictHau():
    text = request.get_json().get("message")
    if (text != "aucun son"):
        text = traduire(text,"ha","fr")
    response = get_response(text)
    response = traduire(response,"fr","ha")
    message = {"answer" : response}
    res = make_response(jsonify(message))
    #res.headers['Access-Control-Allow-Origin'] = '*'
    return res

@app.post("/predictIgb")
def predictIgb():
    text = request.get_json().get("message")
    if (text != "aucun son"):
        text = traduire(text,"ig","fr")
    response = get_response(text)
    response = traduire(response,"fr","ig")
    message = {"answer" : response}
    res = make_response(jsonify(message))
    #res.headers['Access-Control-Allow-Origin'] = '*'
    return res

@app.post("/predictYor")
def predictYor():
    text = request.get_json().get("message")
    if (text != "aucun son"):
        text = traduire(text,"yo","fr")
    response = get_response(text)
    response = traduire(response,"fr","yo")
    message = {"answer" : response}
    res = make_response(jsonify(message))
    #res.headers['Access-Control-Allow-Origin'] = '*'
    return res

@app.post("/predictAra")
def predictAra():
    text = request.get_json().get("message")
    if (text != "aucun son"):
        text = traduire(text,"ar","fr")
    response = get_response(text)
    response = traduire(response,"fr","ar")
    message = {"answer" : response}
    res = make_response(jsonify(message))
    #res.headers['Access-Control-Allow-Origin'] = '*'
    return res

@app.post("/predictZul")
def predictZul():
    text = request.get_json().get("message")
    if (text != "aucun son"):
        text = traduire(text,"zu","fr")
    response = get_response(text)
    response = traduire(response,"fr","zu")
    message = {"answer" : response}
    res = make_response(jsonify(message))
    #res.headers['Access-Control-Allow-Origin'] = '*'
    return res

@app.post("/predictRus")
def predictRus():
    text = request.get_json().get("message")
    if (text != "aucun son"):
        text = traduire(text,"ru","fr")
    response = get_response(text)
    response = traduire(response,"fr","ru")
    message = {"answer" : response}
    res = make_response(jsonify(message))
    #res.headers['Access-Control-Allow-Origin'] = '*'
    return res

@app.post("/predictNya")
def predictNya():
    text = request.get_json().get("message")
    if (text != "aucun son"):
        text = traduire(text,"ny","fr")
    response = get_response(text)
    response = traduire(response,"fr","ny")
    message = {"answer" : response}
    res = make_response(jsonify(message))
    #res.headers['Access-Control-Allow-Origin'] = '*'
    return res

@app.post("/predictIta")
def predictIta():
    text = request.get_json().get("message")
    if (text != "aucun son"):
        text = traduire(text,"it","fr")
    response = get_response(text)
    response = traduire(response,"fr","it")
    message = {"answer" : response}
    res = make_response(jsonify(message))
    #res.headers['Access-Control-Allow-Origin'] = '*'
    return res

@app.post("/predictCre")
def predictCre():
    text = request.get_json().get("message")
    if (text != "aucun son"):
        text = traduire(text,"ht","fr")
    response = get_response(text)
    response = traduire(response,"fr","ht")
    message = {"answer" : response}
    res = make_response(jsonify(message))
    #res.headers['Access-Control-Allow-Origin'] = '*'
    return res

@app.post("/predictHeb")
def predictHeb():
    text = request.get_json().get("message")
    if (text != "aucun son"):
        text = traduire(text,"he","fr")
    response = get_response(text)
    response = traduire(response,"fr","he")
    message = {"answer" : response}
    res = make_response(jsonify(message))
    #res.headers['Access-Control-Allow-Origin'] = '*'
    return res

@app.post("/predictJap")
def predictJap():
    text = request.get_json().get("message")
    if (text != "aucun son"):
        text = traduire(text,"ja","fr")
    response = get_response(text)
    response = traduire(response,"fr","ja")
    message = {"answer" : response}
    res = make_response(jsonify(message))
    #res.headers['Access-Control-Allow-Origin'] = '*'
    return res

@app.post("/predictMal")
def predictMal():
    text = request.get_json().get("message")
    if (text != "aucun son"):
        text = traduire(text,"mg","fr")
    response = get_response(text)
    response = traduire(response,"fr","mg")
    message = {"answer" : response}
    res = make_response(jsonify(message))
    #res.headers['Access-Control-Allow-Origin'] = '*'
    return res

@app.post("/predictSoo")
def predictSoo():
    text = request.get_json().get("message")
    if (text != "aucun son"):
        text = traduire(text,"so","fr")
    response = get_response(text)
    response = traduire(response,"fr","so")
    message = {"answer" : response}
    res = make_response(jsonify(message))
    #res.headers['Access-Control-Allow-Origin'] = '*'
    return res

@app.post("/predictKis")
def predictKis():
    text = request.get_json().get("message")
    if (text != "aucun son"):
        text = traduire(text,"sw","fr")
    response = get_response(text)
    response = traduire(response,"fr","sw")
    message = {"answer" : response}
    res = make_response(jsonify(message))
    #res.headers['Access-Control-Allow-Origin'] = '*'
    return res

@app.post("/predictAmh")
def predictAmh():
    text = request.get_json().get("message")
    if (text != "aucun son"):
        text = traduire(text,"am","fr")
    response = get_response(text)
    response = traduire(response,"fr","am")
    message = {"answer" : response}
    res = make_response(jsonify(message))
    #res.headers['Access-Control-Allow-Origin'] = '*'
    return res

@app.post("/predictHid")
def predictHid():
    text = request.get_json().get("message")
    if (text != "aucun son"):
        text = traduire(text,"hi","fr")
    response = get_response(text)
    response = traduire(response,"fr","hi")
    message = {"answer" : response}
    res = make_response(jsonify(message))
    #res.headers['Access-Control-Allow-Origin'] = '*'
    return res

@app.post("/predictPor")
def predictPor():
    text = request.get_json().get("message")
    if (text != "aucun son"):
        text = traduire(text,"pt","fr")
    response = get_response(text)
    response = traduire(response,"fr","pt")
    message = {"answer" : response}
    res = make_response(jsonify(message))
    #res.headers['Access-Control-Allow-Origin'] = '*'
    return res

@app.post("/start")
def start():
    response = "Bienvenue sur AGRIDIGITALE, la référence économique agricole en Afrique.<br>Je suis Giova, votre assistant virtuel. Que désirez-vous savoir sur l'agriculture en Afrique ?"
    message = {"answer" : response}
    res = make_response(jsonify(message))
    #res.headers['Access-Control-Allow-Origin'] = '*'
    return res

if __name__ == "__main__":
    app.run(debug = True)