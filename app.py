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


@app.get("/lista_ventas")
def ventas():
    return render_template("lista_ventas.html")




@app.get("/detalles")
def detalles():
    return render_template("detalles.html", productos = busqueda_por_nombre(request.args.get("por_nombre")), busqueda = request.args.get("por_nombre"))

def busqueda_por_nombre(input):
    return [producto for producto in cargar_sucursales() if PorNombre(input).corresponde_al_producto(producto)]

@app.get("/categoria")
def categoria():
    return render_template("busq_categoria.html", productos = busqueda_por_categoria(request.args.get("por_categoria")), busqueda = request.args.get("por_categoria"))

def busqueda_por_categoria(input):
    return [producto for producto in cargar_sucursales() if PorCategoria(input).corresponde_al_producto(producto)]

@app.get("/precio")
def precio():
    return render_template("busq_precio.html", productos = busqueda_por_precio(request.args.get("por_precio")), busqueda = request.args.get("por_precio"))

def busqueda_por_precio(input):
    return [producto for producto in cargar_sucursales() if PorPrecio(input).corresponde_al_producto(producto)]

