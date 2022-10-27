import time
class Prenda:
  def __init__(self,codigo,nombre, categoria, precio, stock):
    self.codigo = codigo
    self.nombre = nombre
    self.categoria = [categoria]
    self.precio_base = precio
    self.estado = Nueva()
    self.stock = stock
    self.lista = {"codigo": self.codigo, "nombre": self.nombre, "categoria": self.categoria, "precio": self.precio_base, "stock": self.stock}


  def precio(self):
    return self.estado.precio_final(self.precio_base)
  
  def cambiar_estado(self, nuevo_estado):
    self.estado = nuevo_estado

  def calcular_precio(self):
    return self.estado.precio_final(self.precio)

  def multiples_categorias(self, nueva_categoria):
    self.categoria.append(nueva_categoria)

  def categorias_nuevas(self, categoria):
    return categoria in self.categoria

         
      
class Nueva:
    def precio_final(self,precio_base):
      return precio_base

class Promocion:
  def __init__(self, valor_fijo):
    self.valor_fijo = valor_fijo

  def precio_final(self, precio_base):
    return precio_base - self.valor_fijo

class Liquidacion:
  def precio_final(self, precio_base):
    return precio_base/2 
    

class Sucursal:
  def __init__(self):
    self.productos = []
    self.ventas = []
    self.gastos_por_dia = 5000
    
  def registrar_producto(self, producto_nuevo):
    self.productos.append(producto_nuevo)

  def ver_producto(self):
    lista= []
    for producto in self.productos:
      lista.append(producto)
    return lista
      

  def recargar_stock(self, codigo, valor_a_agregar):
    existe = False
    for producto in self.productos:
      if producto.codigo == codigo:
        existe = True
        producto.stock += valor_a_agregar
    if not existe :
      raise ValueError("no reconoce el codigo")

  def hay_stock(self,codigo_producto):
    for producto in self.productos: 
      if codigo_producto == producto.codigo:
        return producto.stock > 0 
    return False

  def calcular_precio_final(self,es_extranjero,producto):
    precio_final = 0
    for producto in self.productos:
      if es_extranjero and producto.precio>70:
        precio_final = producto.precio
        return precio_final
      else:
        precio_final = producto.precio * 1.21
      return precio_final

  def contar_categoria(self):
    cantidad_categorias = []
    for producto in self.productos:
      if producto["categoria"] not in cantidad_categorias:
          cantidad_categorias.append(producto["categoria"])
      return len(cantidad_categorias)

  def realizar_compra(self,codigo_producto,cantidad_a_comprar):
    codigo_valido= False
    for producto in self.productos:
      if codigo_producto == producto.codigo:
        codigo_valido= True
        if self.hay_stock(codigo_producto) and producto.stock > cantidad_a_comprar:
          producto.stock -= cantidad_a_comprar
          self.ventas.append({"producto":producto.nombre,"cantidad_vendida":cantidad_a_comprar,"monto":producto.precio, "fecha":time.strftime("%d/%m/%y"),"anio":time.strftime("%Y")})
        else:
          raise ValueError("sin stock para comprar")

  def discontinuar_producto(self):
    for producto in self.productos:
      if producto.stock <= 0:
          self.productos.remove(producto)


  def valor_ventas_del_dia(self):
    valor_ventas = 0
    for venta in self.ventas:
      if time.strftime("%d/%m/%y") == self.ventas["fecha"]:
        valor_ventas += self.ventas["precio"]
    return valor_ventas


  def valor_ventas_anio(self):
    valor_ventas_del_anio = 0
    for venta in self.ventas:
      if time.strftime("%Y") == venta["anio"]:
        valor_ventas_del_anio += venta["precio"]
    return valor_ventas_del_anio


  def actualizar_precio(self, codigo, porcentaje):
    if producto in self.productos:
      if codigo == producto.codigo:
        producto.precio += porcentaje

  def ganancia_diaria(self):
    self.ventas - gastos_por_dia
    return self.gastos_del_dia


class SucursalVirtual(Sucursal):
  def __init__(self):
    self.gasto_en_el_dia = 1000
    self.gasto_variable = 1

    def gastos_del_dia(self):
      if self.ventas >100:
        return self.ventas * self.gasto_variable
      else:
        return self.gasto_por_dia

    

class SucursalFisica(self):
  def gastos_del_dia(self):
    return self.gastos_en_el_dia





camisa = Prenda(101, "camisa rosa", "ropa hombre", 2000, 10)
gorra = Prenda(102, "gorra azul", "accesorio", 700, 10)
pulsera = Prenda(103, "pulsera", "accesorio", 900, 50)
sucursal_abasto= Sucursal()


