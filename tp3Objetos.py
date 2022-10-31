import time


class Sucursal:

    def registrar_producto(self, producto):
        if producto in self.productos:
            raise ValueError("el producto ya existe")
        else:
            self.productos.append(producto)


    def recargar_stock(self, codigo, stock_a_agregar):
        existe = False
        for producto in self.productos:
            if producto["codigo"] == codigo:
                existe = True
                producto["stock"] += stock_a_agregar
                if not existe :
                    raise ValueError("no reconoce el codigo")


    def hay_stock(self, codigo_producto):
        for producto in self.productos:
            if codigo_producto == producto["codigo"]:
                return producto["stock"] > 0
            return False


    def contar_categorias(self):
        cantidad_categorias = []
        for producto in self.productos:
            if producto["categoria"] not in cantidad_categorias:
                cantidad_categorias.append(producto["categoria"])
                return len(cantidad_categorias)


    def realizar_compra(self, codigo, cantidad_a_comprar):
        existe = False
        for producto in self.productos:
            if codigo == producto["codigo"]:
                existe = True
                if producto["stock"] > cantidad_a_comprar:
                    monto_total = producto["precio"] * cantidad_a_comprar
                    self.ventas.append({"producto": producto["nombre"], "cantidad_vendida": cantidad_a_comprar, "monto": monto_total, "fecha": time.strftime("%d/%m"), "anio": time.strftime("%Y") })
                else:
                    raise ValueError ("Producto sin stock")



    def discontinuar_producto(self):
        for producto in self.productos:
            if producto["stock"] <= 0:
                self.productos.remove(producto)


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



class PorNombre:
    def __init__(self, nombre):
        self.expresion_del_nombre = nombre

    def corresponde_al_producto(self, producto):
        pass

class PorCategoria:
    def __init__(self, una_categoria):
        self.categoria = una_categoria

    def corresponde_al_producto(self, producto):
        return producto in self.categoria



class SucursalFisica(Sucursal):
    def __init__(self, gasto):
        self.productos = []
        self.gasto_por_dia = gasto

    def gastos_del_dia(self):
        return self.gasto_por_dia
    
    #def ganancia_diaria(self):
        #return self.va


class SucursalVirtual(Sucursal):
    def __init__(self, gasto_variable):
        self.productos = []
        self.gasto_variable = gasto_variable
        #self.gasto_dia = 0


    def gastos_del_dia(self):
        if self.ventas_del_dia() >100:
            return self.valor_ventas_del_dia() * self.gasto_variable
        else:
            return 0
        
        

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

    def es_categoria_nueva(self, categoria):
        return categoria in self.categoria

         
      
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




camisa = {"codigo": 101, "nombre": "camisa rosa", "categoria":"ropa formal", "precio":3000, "stock": 0}
pantalon = {"codigo": 102, "nombre": "pantalon oxford", "categoria":"casual", "precio":5000, "stock": 0}
remera = {"codigo": 103, "nombre": "remera roja", "categoria":"ropa formal", "precio":3000, "stock": 0}


