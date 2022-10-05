"""Reconocida cadena de ropa formal, con tiendas en muchas ciudades de Argentina. 
Le ha pedido a 2Diseños, consultora de software, desarrollar un nuevo sistema para la gestión de sus ventas y stock."""

#Modelo
#MacoWins guarda la información de sus productos en una lista con la siguiente forma:
#esto es una lista de productos

import time
productos = [
  {
    "codigo": 100,
    "nombre": "remera talle m",
    "categoria": "remera",
    "precio": 4500,
    "stock": 35
  }
]
#Además, guarda la información de cada venta así:
ventas = [
  {
    "codigo_producto": 100,
    "cantidad": 3,
    "fecha": "2021-09-20",
    "precio": 4500
  }
]

#Requerimientos
"""Desarrollar y probar las funciones y procedimientos:
"""
#Productos de ejemplo 
# #esto es un diccionario de cada producto
camisa = {
  "codigo": 100,
  "nombre": "camisa estampada",
  "categoria": "ropa formal",
  "precio": 3500
}
collar = {
  "codigo": 200,
  "nombre": "collar de perlas",
  "categoria": "accesorios",
  "precio": 2100
}
blusa = {
  "codigo": 300,
  "nombre": "blusa de seda",
  "categoria": "remeras",
  "precio": 2900
}
short = {
  "codigo": 400,
  "nombre": "short veraniego",
  "categoria": "pantalon",
  "precio": 2800
}
corbata = {
  "codigo": 500,
  "nombre": "corbata azul",
  "categoria": "accesorios",
  "precio": 750
}
campera = {
  "codigo": 600,
  "nombre": "campera cuero",
  "categoria": "abrigo",
  "precio": 9500
}
wideleg = {
  "codigo": 540,
  "nombre": "pantalon jean",
  "categoria": "jeans",
  "precio": 3100
}
borcegos = {
  "codigo": 110,
  "nombre": "borcegos marrones",
  "categoria": "botas",
  "precio": 12000
}
blazer = {
  "codigo": 80,
  "nombre": "blazer azul",
  "categoria": "saco formal",
  "precio": 2700
}
medias = {
  "codigo": 45,
  "nombre": "medias goku",
  "categoria": "accesorios",
  "precio": 500
}

#1.
#registrar_producto: recibe un diccionario con codigo, nombre, categoria, precio y agrega un producto nuevo a la lista de productos. El stock del producto agregado debe estar inicialmente en cero.

productos = []
ventas = []

def registrar_producto(producto):
  producto["stock"] = 0
  list.append(productos, producto)

#recibe un diccionario con nombre,codigo,categoria y precio a la lista productos

#Ejemplo
"""registrar_producto(borcegos)"""



#2.
# recargar_stock: toma un código de producto y una cantidad de unidad de stock a agregar, e incrementa el stock correspondiente a ese producto. Si el código de producto indicado no existe, debe lanzar una excepción."""

def recargar_stock(codigo, valor_a_agregar):
  """recargar_stock(101, 70)"""
  existe = False
  for producto in productos:
      if producto["codigo"]== codigo:
        existe = True
        producto["stock"] += valor_a_agregar
      if not existe:
        raise ValueError("codigo no reconocido")




#3.hay_stock: recibe un código de producto y dice si hay stock (es decir, si el stock correspondiente es mayor a cero). Si el código indicado no existe en la lista de productos, debe devolver False.


def hay_stock(codigo, productos):
    respuesta = False
    for x in range(len(productos)):
        if productos[x]["codigo"] == codigo and productos[x]["stock"] > 0:
            respuesta = True
    return respuesta


#4.calcular_precio_final: toma un producto (un diccionario) y un booleano es_extranjero y calcula su valor final, según la siguiente regla: a. si quien calcula el precio es extranjero y el valor es mayor de $70, es el mismo valor sin cambios. b. en caso contrario, es el valor original más un 21%

def calcular_precio_final(producto, es_extranjero):
  if es_extranjero and producto["precio"]>70:
    precio_final = producto ["precio"]
  else:
    precio_final = producto["precio"]* 1.21
  return precio_final


#5.contar_categorias: retorna la cantidad de categorías únicas

def contar_categorias(productos):
    if len(productos) > 0:
        cantidad_categorias = 1
        for x in range(1, len(productos)):
            categoria_ya_contada = False
            for j in range(x):
                if productos[j]["categoria"] == productos[x]["categoria"]:
                    categoria_ya_contada = True
            if not categoria_ya_contada:
                cantidad_categorias += 1
    else:
        cantidad_categorias = 0
    return cantidad_categorias



#6.realizar_compra: recibe un código de producto y una cantidad de items a comprar. En base a ello, decrementa el stock del producto correspondiente y crea una nueva venta con la información correspondiente. Si no hay suficiente stock, lanzar una excepción.


def realizar_compra(codigo_producto, cantidad_a_comprar, fecha, ventas, productos):
    for x in range(len(productos)):
        if productos[x]["codigo"] == codigo_producto and productos[x]["stock"] - cantidad_a_comprar >= 0:
            productos[x]["stock"] -= cantidad_a_comprar
            nueva_venta = {"codigo_producto":codigo_producto, "cantidad":cantidad_a_comprar, "fecha":fecha, "precio":(cantidad_a_comprar*productos[x]["precio"])}
            ventas.append(nueva_venta)
        elif productos[x]["codigo"] == codigo_producto:
            raise ValueError("Producto sin stock")




#7.discontinuar_productos: elimina los productos sin stock.


def discontinuar_producto(productos):
    for producto in productos:
      if producto ["stock"]<=0:
        productos.remove(producto)
        


#8.valor_ventas_del_dia: retorna el valor total de las ventas del día de hoy.

def valor_ventas_del_dia():
    
    total_recaudado = 0
    for venta in ventas:
        if venta["fecha"] == time.strftime("%d/%m/%y"):
          total_recaudado += venta["precio"]
    return total_recaudado


#9.ventas_del_anio: retorna un listado con todas las ventas para el año actual.

def valor_ventas_del_anio(ventas):
  total_recaudado = 0
  for x in range(len(ventas)):
        fecha = time.strftime(ventas[x]["fecha"], '%d-%m-%Y')
        if fecha.date().strftime("%Y") == time.today().date().strftime("%Y"):
            total_recaudado += ventas[x]["precio"]
  return total_recaudado

def armar_ranking_ventas(ventas):
    ranking_ventas = []
    for x in range(len(ventas)):
        no_está_en_ranking = True
        for i in range(len(ranking_ventas)):
            if ranking_ventas[i]["código_producto"] == ventas[x]["código_producto"]:
                ranking_ventas[i]["cantidad"] += ventas[x]["cantidad"]
                no_está_en_ranking = False
        if no_está_en_ranking:
            ranking_ventas.append({"código_producto":ventas[x]["código_producto"], "cantidad":ventas[x]["cantidad"]})
    return ranking_ventas

def ordenar_ranking_ventas(ranking):
    for x in range(len(ranking) - 1):
        for i in range(len(ranking) - x - 1):
            if ranking[i]["cantidad"] < ranking[i + 1]["cantidad"]:
                ranking[i], ranking[i + 1] = ranking[i + 1], ranking[i]

def existeEsteProducto(código, productos):
    existe = False
    for x in range(len(productos)):
        if productos[x]["código"] == código:
            existe = True
    return existe

def buscarProducto(código, productos):
    for x in range(len(productos)):
        if productos[x]["código"] == código:
            prod = productos[x]
    return prod
    
                

#10.productos_mas_vendidos: toma una cantidad n de productos y retorna los nombres de los n productos más vendidos

"""def productos_más_vendidos(ventas, n, productos):
    ranking_ventas = armar_ranking_ventas(ventas)
    ordenar_ranking_ventas(ranking_ventas)
    x = 0
    while x < n and x < len(ranking_ventas):
        if existeEsteProducto(ranking_ventas[x]["código_producto"], productos):
            producto = buscarProducto(ranking_ventas[x]["código_producto"], productos)
            print("Nombre:",producto["nombre"])
            print("Cantidad vendida:",ranking_ventas[x]["cantidad"])
        x += 1"""


#11.actualizar_precios_por_categoria: toma una categoría y un porcentaje, y actualiza según ese porcentaje el precio de todos los productos que tengan esa categoría. La búsqueda de categoría en este procedimiento no debe ser exacta: por ejemplo tanto si se pasa como argumento "REMERA", " REMERA" o "Remera", deben actualizarse los productos de la categoría "remera".

def actualizar_precios_por_categoría(categoría, porcentaje, productos):
    for x in range(len(productos)):
        if categoría.strip(' ').lower() == productos[x]["categoría"].lower():
            productos[x]["precio"] *= 1 + porcentaje / 100