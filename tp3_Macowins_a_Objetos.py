class Prenda:
  def __init__(self,codigo,nombre, categoria, precio, stock):
    self.codigo = codigo
    self.nombre = nombre
    self.categoria = [categoria]
    self.precio_base = precio
    self.estado = Nueva()
    self.stock = stock

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
    
  def registrar_producto(self, producto_nuevo):
    self.productos.append(producto_nuevo)

  def ver_producto(self):
    for producto in range(len(self.productos)):
      return self.productos

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

  def calcular_precio_final(self,producto,es_extranjero):
    precio_final= 0
  if es_extranjero and producto.precio >70:
    precio_final = producto.precio
    return precio_final
  else:
    precio_final = producto.precio *1.21
  return precio_final

  
