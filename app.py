from flask import Flask, request, render_template, url_for
from markupsafe import escape
from tp3Objetos import *

app = Flask(__name__)


def cargar_sucursales():
    lista = []
    lis = cargar_todos(modulo='tp3Objetos').values()
    for suc in lis:
        for producto in suc.productos:
            lista.append(producto)
    return lista

@app.get("/")
def raiz():
    return render_template("home.html")

@app.get("/lista_productos")
def lista_de_productos():     
    return render_template("lista_productos.html", lista = cargar_sucursales())



@app.get("/detalles")
def detalles():
    return render_template("detalles.html")

@app.get("/lista_ventas")
def ventas():
    return render_template("lista_ventas.html")


@app.get("/detalles")
def busqueda():
    return render_template("detalles.html", productos = busqueda_por_nombre(request.args.get("por_nombre", "remera blanca")), busqueda = request.args.get("por_nombre"))

def busqueda_por_nombre(input):
    return [producto for producto in cargar_sucursales() if PorNombre(input).corresponde_al_producto(producto)]

def saludo():
    return render_template("detalles.html", nombre = busqueda_por_nombre())


