#Reconocida cadena de ropa formal, con tiendas en muchas ciudades de Argentina le ha pedido a 2Diseños, consultora de software, desarrollar un nuevo sistema para la gestión de sus ventas y stock


import time

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

class Prenda:
  def __init__(self,producto):
    self.producto = producto

  def nueva(self):
    self.producto["precio"] = ["precio"]

  def promocion(self, valor_fijo):
    self.producto["precio"] -= valor_fijo

  def liquidacion(self):
    self.producto["precio"]/2

#1.
#registrar_producto: recibe un diccionario con codigo, nombre, categoria, precio y agrega un producto nuevo a la lista de productos.

productos = []
ventas = []

def registrar_producto(producto):
  producto["stock"] = 0
  list.append(productos, producto)

def limpiar_lista():
  productos.clear()

def cantidad_productos():
  return len(productos)  




#2.
# recargar_stock: toma un código de producto y una cantidad de unidad de stock a agregar, e incrementa el stock correspondiente a ese producto. Si el código de producto indicado no existe, lanzauna excepción."""

def recargar_stock(codigo, valor_a_agregar):
  existe = False
  for producto in productos:
      if producto["codigo"]== codigo:
        existe = True
        producto["stock"] += valor_a_agregar
  if not existe:
        raise ValueError("codigo no reconocido")




#3.hay_stock: recibe un código de producto y dice si hay stock (es decir, si el stock correspondiente es mayor a cero). Si el código indicado no existe en la lista de productos, debe devolver False.



def hay_stock(codigo_producto):
  for producto in productos:
    if codigo_producto == producto["codigo"]:
      return producto["stock"] > 0
  return False

    #respuesta = False
    #for x in range(len(productos)):
        #if productos["codigo"] == codigo_producto["stock"] > 0:
            #respuesta = True
    #return respuesta


#4.calcular_precio_final: toma un producto (un diccionario) y un booleano es_extranjero y calcula su valor final, según la siguiente regla: a. si quien calcula el precio es extranjero y el valor es mayor de $70, es el mismo valor sin cambios. b. en caso contrario, es el valor original más un 21%

def calcular_precio_final(producto, es_extranjero):
  precio_final=0
  if es_extranjero and producto["precio"]>70:
    precio_final = producto["precio"]
    return precio_final
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


#def realizar_compra(codigo_producto, cantidad_a_comprar, fecha, ventas, productos):
    #for x in range(len(productos)):
        #if productos[x]["codigo"] == codigo_producto and productos[x]["stock"] - cantidad_a_comprar >= 0:
            #productos[x]["stock"] -= cantidad_a_comprar
            #nueva_venta = {"codigo_producto":codigo_producto, "cantidad":cantidad_a_comprar, "fecha":fecha, "precio":(cantidad_a_comprar*productos[x]["precio"])}
            #ventas.append(nueva_venta)
        #elif productos[x]["codigo"] == codigo_producto:
            #raise ValueError("Producto sin stock")

def realizar_compra(codigo_producto, cantidad_a_comprar):
  codigo_valido = False
  for producto in productos:
    if codigo_producto == producto["codigo"]:
      codigo_valido=True
      if hay_stock(codigo_producto) and producto["stock"]> cantidad_a_comprar:
        producto["stock"] -= cantidad_a_comprar
        monto_total= producto["precio"]*cantidad_a_comprar
        list.append(ventas,{"producto":producto["nombre"],"cantidad_vendida":cantidad_a_comprar, "monto":monto_total,"fecha": time.strftime("%d/%m/%y"),"anio":time.strftime("%Y")})
      else:
        raise ValueError ("Sin stock para comprar")
  if not codigo_valido:
    raise ValueError ("El codigo no existe")




#7.discontinuar_productos: elimina los productos sin stock.


def discontinuar_producto():
    for producto in productos:
      if producto ["stock"]<=0:
        #productos.remove(producto)
        list.remove(productos,producto)


#8.valor_ventas_del_dia: retorna el valor total de las ventas del día de hoy.

def valor_ventas_del_dia():
  valor_total = 0
  for venta in ventas:
    if time.strftime("%d/%m/%y") == venta["fecha"]:
      valor_total+= venta["monto"]
  return valor_total
    
    #total_recaudado_dia = 0
    #for venta in ventas:
        #if venta["fecha"] == date.strftime("%d/%m/%y"):
          #total_recaudado += venta["precio"]
    #return total_recaudado_dia


#9.ventas_del_anio: retorna un listado con todas las ventas para el año actual.

def valor_ventas_del_anio():
  ventas_del_anio = 0
  for venta in ventas:
    if time.strftime("%Y") == venta["anio"]:
      ventas_del_anio += venta["monto"]
  return ventas_del_anio

#def valor_ventas_del_anio():
  #total_recaudado_anio = 0
  #for venta in ventas:
    #if date.strftime("%Y") == venta["anio"]:
      #total_ventas_anio += venta ["precio"]
  #return total_recaudado_anio


                

#10.productos_mas_vendidos: toma una cantidad n de productos y retorna los nombres de los n productos más vendidos

#def productos_más_vendidos(ventas, n, productos):
    #ranking_ventas = armar_ranking_ventas(ventas)
    #ordenar_ranking_ventas(ranking_ventas)
    #x = 0
    #while x < n and x < len(ranking_ventas):
        #if existeEsteProducto(ranking_ventas[x]["código_producto"], productos):
           # producto = buscarProducto(ranking_ventas[x]["código_producto"], productos)
            #print("Nombre:",producto["nombre"])
            #print("Cantidad vendida:",ranking_ventas[x]["cantidad"])
        #x += 1"""


def productos_mas_vendidos(cantidad_productos):
  productos_vendidos= []
  #ranking_mas_vendidos=[]
  for venta in ventas:
    list.append(productos_vendidos,venta["producto"])



#11.actualizar_precios_por_categoria: toma una categoría y un porcentaje, y actualiza según ese porcentaje el precio de todos los productos que tengan esa categoría.

def actualizar_precios_por_categoria(categoria, porcentaje, productos):
    for x in range(len(productos)):
        if categoria.strip(' ').lower() == productos[x]["categoria"].lower():
            productos[x]["precio"] *= 1 + porcentaje / 100