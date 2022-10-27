## README
En el presente trabajo practico implementamos los siguientes diagramas de clase:


*Prenda

/Atributos/
codigo
nombre
categoria
precio_base
estado
stock
lista

/Metodos/
__init__(self, codigo, nombre, categoria, precio, stock)
precio(self)
cambiar_estado(self)
calcular_precio(self)
multiples_categorias(self)
categorias_nuevas(self)


Aplicamos polimorfismo a las siguientes clases:

 clase Nueva
 
 /Metodos/
 precio_final(self, precio_base)
 
 clase Promocion
 
 __init__(self,valor_fijo)
 
 /Metodos/
 precio_final(self)
 
 clase Liquidacion
 
 /Metodos/
 precio_final(self, precio_base)
 
 
 clase Sucursal
 
 /Atributos/
 self.productos
 self.ventas
 self.gastos_por_dia
 
 /Metodos/
 __init__(self)
 registrar_producto(self, producto_nuevo)
 ver_producto(self)
 recargar_stock(self, codigo, valor_a_agregar)
 hay_stock(self, codigo_producto)
 calcular_precio_final(self, producto, es_extranjero)
 contar_categorias(self)
 realizar_compra(self, codigo_producto, cantidad_a_comprar)
 discontinuar_productos(self)
 valor_ventas_del_dia(self)
 valor_ventas_del_anio(self)
 actualizar_precio(self, codigo, porcentaje)
 ganancia_diaria(self)
 
 
Se aplico herencia de la Superclase Sucursal en:

SucursalVirtual(Sucursal)
/Atributos/
self.gasto_en_el_dia
self.gasto_variable

/Metodos/
__init__(self)
gastos_del_dia(self)

SucursalFisica(Sucursal)

/Metodos/
gastos_del_dia(self)
 
