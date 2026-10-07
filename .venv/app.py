from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def Inicio():
    return render_template('encuesta.html')    

@app.route("/resultado-encuesta")
def resultadoEncuesta():
    return render_template("resultado-encuesta.html")

@app.route("/encuesta")
def encuesta():
    return render_template("encuesta.html")