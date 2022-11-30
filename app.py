from flask import Flask, request, render_template, url_for
from markupsafe import escape
from tp3Objetos import *

app = Flask(__name__)


@app.get("/")
def raiz():
    return render_template("home.html")

@app.get("/lista_productos")
def lista_de_productos():
    lista = []
    lis = cargar_todos(modulo='tp3Objetos').values()
    for suc in lis:
        for producto in suc.productos:
            lista.append(producto)        
    return render_template("lista_productos.html", lista = lista)



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


