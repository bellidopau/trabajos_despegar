from flask import Flask, request, render_template, url_for
from markupsafe import escape
from tp3Objetos import *

app = Flask(__name__)


@app.get("/")
def raiz():
    return render_template("home.html")

@app.get("/lista_productos")
def lista_de_productos():
    #aqui tiene que estar el metodo q trae la lista
    lista = request.form.get("lista")
    return render_template("lista_productos.html", lista = lista)


@app.get("/detalle_producto")
def detalle():
    return render_template("detalle_producto.html")

@app.get("/lista_ventas")
def ventas():
    return render_template("lista_ventas.html")
