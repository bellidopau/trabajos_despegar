from flask import Flask, request, render_template, url_for
from markupsafe import escape
from tp3Objetos import *

app = Flask(__name__)


@app.get("/")
def raiz():
    return render_template("home.html")

@app.get("/lista_productos")
def lista_de_productos():
    #lista = sucursal.ver_productos()
    #aqui tiene que estar el metodo q trae la lista
    lista = request.args.get("lista")
    return render_template("lista_productos.html", lista = lista())


@app.get("/detalles")
def detalles():
    return render_template("detalles.html")

@app.get("/lista_ventas")
def ventas():
    return render_template("lista_ventas.html")


@app.route("/busqueda", methods=['GET','POST','DELETE'])
def busqueda():
    busqueda = request.form.get('busqueda')
    return render_template("resultado.html")
