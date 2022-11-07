import time



class Sucursal:
    def __init__(self):
        self.productos = []
        self.ventas = []


    def registrar_producto(self, producto):
        if producto in self.productos:
            raise ValueError("el producto ya existe")
        else:
            self.productos.append(producto)


    def limpiar_lista(self):
        self.productos.clear()
    def limpiar_lista_ventas(self):
        self.ventas.clear()    

    def ver_productos(self):
        return self.productos()

    def cantidad_productos(self):
        return len(self.productos)  

    def recargar_stock(self, codigo, stock_a_agregar):
        existe = False
        for producto in self.productos:
            if producto.codigo == codigo:
                producto.stock += stock_a_agregar
                existe = True
        if not existe:
            raise ValueError ("el codigo ya existe")


    def hay_stock(self, codigo_producto):
        for producto in self.productos:
            if codigo_producto == producto.codigo:
                return producto.stock > 0
            return False

    def calcular_precio_final(self, producto, es_extranjero):
        precio_final=0
        for producto in self.productos:
            if es_extranjero and producto.precio >70:
                precio_final = producto.precio
                return precio_final
            else:
                precio_final = producto.precio * 1.21
            return precio_final


    def contar_categorias(self):
        cantidad_categorias = []
        for producto in self.productos:
            if producto.categoria not in cantidad_categorias:
                cantidad_categorias.append(producto.categoria)
        return len(cantidad_categorias)


    def realizar_compra(self, codigo, cantidad_a_comprar):
        existe = False
        for producto in self.productos:
            if codigo == producto.codigo:
                existe = True
                if producto.stock >= cantidad_a_comprar:
                    monto_total = producto.precio * cantidad_a_comprar
                    self.ventas.append({"producto": producto.nombre, "cantidad_vendida": cantidad_a_comprar, "monto": monto_total, "fecha": time.strftime("%d/%m"), "anio": time.strftime("%Y") })
        if not existe:
            raise ValueError ("Producto sin stock")



    def discontinuar_producto(self):
        self.productos = [producto for producto in self.productos if producto.stock >0]


    def ventas_del_dia(self):
        cantidad_de_ventas = 0
        for venta in self.ventas:
            if time.strftime("%d/%m") == venta["fecha"]:
                cantidad_de_ventas += 1
        return cantidad_de_ventas


    def valor_ventas_del_dia(self):
        total_vendido = 0
        for venta in self.ventas:
            if time.strftime("%d/%m") == venta["fecha"]:
                total_vendido += venta["monto"]
        return total_vendido



    def ventas_del_anio(self):
        cantidad_de_ventas_anio = 0
        for venta in self.ventas:
            if time.strftime("%Y") == venta["anio"]:
                cantidad_de_ventas_anio += 1
        return cantidad_de_ventas_anio


    def valor_ventas_del_anio(self):
        cantidad_de_ventas_anio = 0
        for venta in self.ventas:
            if time.strftime("%Y") == venta["anio"]:
                cantidad_de_ventas_anio += venta["monto"]
        return cantidad_de_ventas_anio

    
    
    def actualizar_precio_por_categoria(self, categoria, porcentaje):
        self.actualizar_precios_segun(PorCategoria(categoria), porcentaje)

    def actualizar_precio_por_nombre(self, nombre, porcentaje):
        self.actualizar_precios_segun(PorNombre(nombre), porcentaje)

    def actualizar_precio_segun(self, criterio, porcentaje):
        for producto in self.productos:
            if criterio.corresponde_al_producto(producto):
                producto.precio += (producto.precio*porcentaje)/100


class SucursalFisica(Sucursal):
    def __init__(self, gasto):
        super().__init__() #TODO hacer lo mismo en sucursal virtual
        self.gasto_por_dia = gasto

    def gastos_del_dia(self):
        return self.gasto_por_dia
    


class SucursalVirtual(Sucursal):
    def __init__(self, gasto_variable):
        self.productos = []
        self.ventas = []
        self.gasto_variable = gasto_variable


    def gastos_del_dia(self):
        if self.ventas_del_dia() >100:
            return self.ventas_del_dia() * self.gasto_variable
        else:
            return 0
        
    def ganancia_del_dia(self):
        return self.valor_ventas_del_dia - self.gasto_variable()

    def gasto_configurable(self, gasto_x):
        self.gasto_variable = gasto_x



class Prenda:
    def __init__(self, codigo, nombre, categoria, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.categoria = [categoria]
        self.precio = precio
        self.estado = Nueva()
        self.stock = 0


    def precio_(self):
        return self.estado.precio_final(self.precio)
  
    def cambiar_estado(self, nuevo_estado):
        self.estado = nuevo_estado

    def calcular_precio(self):
        return self.estado.precio_final(self.precio)

    def agregar_multiples_categorias(self, nueva_categoria):
        self.categoria.append(nueva_categoria)

    def categoria_nueva(self, categoria):
        return categoria in self.categoria

    def es_de_categoria(self,una_categoria):
        for categoria in self.categoria:
            if categoria.lower() == una_categoria.lower():
                return True
        return False

    def es_de_nombre(self, nombre):
        return nombre == self.nombre

    def es_de_precio(self, precio):
        return precio == self.precio

         
class Nueva:
    def precio_final(self,precio):
      return precio

class Promocion:
    def __init__(self, valor_fijo):
        self.valor_fijo = valor_fijo

    def precio_final(self, precio_base):
        return precio_base - self.valor_fijo

class Liquidacion:
    def precio_final(self, precio_base):
        return precio_base/2

class PorPrecio:
    def __init__(self, un_precio):
        self.precio = un_precio

    def corresponde_al_producto(self, producto):
        return producto.es_de_precio(self.precio)

#TODO modificar los criterios para que sean polimorficos y testearlos
class PorStock:
    def __init__(self, un_stock):
        self.stock = un_stock

    def actualizar_precios_por_stock(self, producto):
        if producto.stock > 0:
            producto.stock += 1
#TODO modoficar Oposicion para que cualquiera de los criterior generados sean negados y no sin repetir logica
class PorPosicion:

    def actualizar_precios(self,un_valor, producto):
        for producto in self.productos:
            if producto.precio > un_valor:
                producto.precio = un_valor
            if producto.stock < 0:
                producto.stock +=1



class PorNombre:
    def __init__(self, nombre):
        self.expresion_del_nombre = nombre

    def corresponde_al_producto(self, producto):
        return producto.es_de_nombre(self.expresion_del_nombre)
        
class PorCategoria:
    def __init__(self, una_categoria):
        self.categoria = una_categoria

    def corresponde_al_producto(self, producto):
        return producto.es_de_categoria (self.categoria)


#TODO implemetar una busqueda generica en busquedapor

"""retiro = Sucursal()

camisa = Prenda(100, "camisa m", "casual", 3000)
pantalon = Prenda(101, "pantalon xl", "formal", 4000)"""
