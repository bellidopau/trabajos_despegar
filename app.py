from flask import Flask, request, render_template, url_for
from markupsafe import escape
from tp3Objetos import *

app = Flask(__name__)


@app.get("/")
def raiz():
    return render_template("home.html")

@app.get("/lista_productos")
def lista_de_productos():
    lista = cargar_todos(modulo='tp3Objetos')

    return render_template("lista_productos.html", lista = lista)


def todos_los_productos():
    productos = []
    for sucursal in cargar_todos(modulo='tp3Objetos').values():
        productos += sucursal.productos
    return productos


@app.get("/detalles")
def detalles():
    return render_template("detalles.html")

@app.get("/lista_ventas")
def ventas():
    return render_template("lista_ventas.html")


@app.route("/busqueda", methods=['GET'])
def busqueda():
    busqueda = request.args.get('busqueda')
    return render_template("resultado.html")


