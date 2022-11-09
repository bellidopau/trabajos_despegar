from tp3Objetos import *

pantalon = None
camisa = None
sucursal_abasto = None
corbata = None

def setup_function():
    global pantalon
    global camisa
    global corbata
    global sucursal_abasto
    pantalon = Prenda(100,"pantalon azul","sastrero",3000)
    camisa = Prenda(101, "camisa rosa", "ropa formal", 1700 )
    corbata = Prenda(102, "corbata blanca", "accesorio", 1200)
    sucursal_abasto = SucursalFisica(1000)

#Test de Sucursal

#1 registrar_producto
def test_se_registro_el_producto_remera():
    sucursal_abasto.limpiar_lista()
    sucursal_abasto.registrar_producto(pantalon)
    assert len(sucursal_abasto.productos)== 1 

#2 recargar_stock
def test_recarga_10_camisa_a_la_lista():
    sucursal_abasto.limpiar_lista()
    sucursal_abasto.registrar_producto(camisa)
    sucursal_abasto.recargar_stock(101, 10)
    assert sucursal_abasto.hay_stock(101) == True

# hay stock
def test_no_hay_stock_de_camisa_si_de_pantalon():
    sucursal_abasto.limpiar_lista()
    sucursal_abasto.registrar_producto(camisa)
    sucursal_abasto.registrar_producto(pantalon)
    sucursal_abasto.recargar_stock(100, 25)
    assert sucursal_abasto.hay_stock(101) == False


def test_hay_stock_de_camisa():
    sucursal_abasto.limpiar_lista()
    sucursal_abasto.registrar_producto(pantalon)
    sucursal_abasto.recargar_stock(100, 25)
    assert sucursal_abasto.hay_stock(100)

#calcular_precio_final
def test_calcula_precio_de_camisa():
    sucursal_abasto.limpiar_lista()
    sucursal_abasto.registrar_producto(pantalon)
    assert sucursal_abasto.calcular_precio_final(100, True) == 3000

def test_calcula_precio_camisa_con_impuesto():
    sucursal_abasto.limpiar_lista()
    sucursal_abasto.registrar_producto(pantalon)
    assert sucursal_abasto.calcular_precio_final(100, False) == 3630

#contar_categorias
def test_si_cuenta_categorias_unicas():
    sucursal_abasto.limpiar_lista()
    sucursal_abasto.registrar_producto(camisa)
    assert sucursal_abasto.contar_categorias() == 1

def test_cuenta_categorias_distintas():
    sucursal_abasto.limpiar_lista()
    sucursal_abasto.limpiar_lista_ventas()
    sucursal_abasto.registrar_producto(camisa)
    sucursal_abasto.registrar_producto(pantalon)
    assert sucursal_abasto.contar_categorias() == 2

#realizar_compra
def test_realiza_compra_de_un_producto_con_stock():
    sucursal_abasto.limpiar_lista()
    sucursal_abasto.limpiar_lista_ventas()
    sucursal_abasto.registrar_producto(camisa)
    sucursal_abasto.recargar_stock(101,50)
    sucursal_abasto.realizar_compra(101,50)
    assert len(sucursal_abasto.ventas) == 1

"""def test_compra_producto_sin_stock():
    sucursal_abasto.limpiar_lista()
    sucursal_abasto.registrar_producto(pantalon)
    assert sucursal_abasto.realizar_compra(101, 1) == ValueError ("Producto sin stock")"""

def test_se_agregar_producto_comprado_a_ventas():
    sucursal_abasto.limpiar_lista()
    sucursal_abasto.limpiar_lista_ventas()
    sucursal_abasto.registrar_producto(camisa)
    sucursal_abasto.recargar_stock(101,100)
    sucursal_abasto.realizar_compra(101,20)
    assert sucursal_abasto.ventas[0]["producto"]== "camisa rosa"

#discontinuar_producto
def test_elimina_un_producto_en_la_lista_sin_stock():
    sucursal_belgrano = SucursalFisica(1300)
    sucursal_belgrano.limpiar_lista()
    sucursal_belgrano.registrar_producto(corbata)
    sucursal_belgrano.registrar_producto(camisa)
    sucursal_belgrano.discontinuar_producto()
    assert len(sucursal_belgrano.productos) ==0

    
def test_elimina_producto_sin_stock():
    sucursal_abasto.limpiar_lista()
    sucursal_abasto.registrar_producto(pantalon)
    sucursal_abasto.registrar_producto(camisa)
    sucursal_abasto.registrar_producto(corbata)
    sucursal_abasto.recargar_stock(100, 10)
    sucursal_abasto.recargar_stock(101, 10)
    sucursal_abasto.discontinuar_producto()
    assert len(sucursal_abasto.productos) ==2

#valor_ventas_del_dia
def test_retorna_el_valor_de_3_compras_hechas():
    sucursal_abasto.limpiar_lista()
    sucursal_abasto.registrar_producto(pantalon)
    sucursal_abasto.registrar_producto(camisa)
    sucursal_abasto.registrar_producto(corbata)
    sucursal_abasto.recargar_stock(100, 10)
    sucursal_abasto.recargar_stock(101, 10)
    sucursal_abasto.recargar_stock(102, 10)
    sucursal_abasto.realizar_compra(100, 1)
    sucursal_abasto.realizar_compra(101, 1)
    sucursal_abasto.realizar_compra(102, 1)
    assert sucursal_abasto.valor_ventas_del_dia() == 5900

def test_retorna_la_cantidad_de_ventas_del_dia():
    sucursal_abasto.limpiar_lista()
    sucursal_abasto.limpiar_lista_ventas()
    sucursal_abasto.registrar_producto(pantalon)
    sucursal_abasto.registrar_producto(camisa)
    sucursal_abasto.recargar_stock(100, 10)
    sucursal_abasto.recargar_stock(101, 10)
    sucursal_abasto.realizar_compra(100, 1)
    sucursal_abasto.realizar_compra(101, 1)
    assert sucursal_abasto.ventas_del_dia() == 2

#valor_ventas_del_anio
def test_devuelve_cuanto_se_vendio_en_un_anio_por_unidad():
    sucursal_abasto.limpiar_lista()
    sucursal_abasto.limpiar_lista_ventas()
    sucursal_abasto.registrar_producto(pantalon)
    sucursal_abasto.registrar_producto(camisa)
    sucursal_abasto.registrar_producto(corbata)
    sucursal_abasto.recargar_stock(100, 10)
    sucursal_abasto.recargar_stock(101, 10)
    sucursal_abasto.recargar_stock(102, 10)
    sucursal_abasto.realizar_compra(100, 10)
    sucursal_abasto.realizar_compra(101, 1)
    sucursal_abasto.realizar_compra(102, 3)
    assert sucursal_abasto.ventas_del_anio() == 3

def test_el_total_de_lo_vendido_en_un_anio_es():
    sucursal_abasto.limpiar_lista()
    sucursal_abasto.registrar_producto(pantalon)
    sucursal_abasto.registrar_producto(camisa)
    sucursal_abasto.registrar_producto(corbata)
    sucursal_abasto.recargar_stock(100, 10)
    sucursal_abasto.recargar_stock(101, 10)
    sucursal_abasto.recargar_stock(102, 10)
    sucursal_abasto.realizar_compra(100, 10)
    sucursal_abasto.realizar_compra(101, 9)
    sucursal_abasto.realizar_compra(102, 5)
    sucursal_abasto.realizar_compra(101, 8)
    assert sucursal_abasto.valor_ventas_del_anio() == 64900

#actualizar_precios_segun
def test_actualizar_precio_a_categoria_camisa_mal_escrita_en_un_50_porciento_debe_actualizar_el_precio_a_6750():
    sucursal_abasto.limpiar_lista()
    sucursal_abasto.registrar_producto(camisa)
    sucursal_abasto.actualizar_precio_segun(PorNombre(" caMisa "),50)
    assert len(sucursal_abasto.productos) == 1



#Tests de clase Prenda
def test_se_cambia_el_precio_de_la_prenda_si_esta_en_promocion():
    camisa.cambiar_estado(Promocion(100))
    assert camisa.precio_total() == 1600

def test_se_cambia_el_precio_de_la_prenda_si_esta_en_liquidacion():
    camisa.cambiar_estado(Liquidacion())
    assert camisa.precio_total() == 850.0

def test_la_categoria_es_de_la_prenda():
    assert camisa.es_de_categoria("ropa formal") == True

def test_a_categoria_ropaformal_se_agrega_una_adicional():
    camisa.agregar_multiples_categorias("ropa verano")
    assert len(camisa.categoria) ==2

def test_categoria_ropaformal_corresponde_a_esa_prenda():
    assert camisa.es_de_nombre("caMisa") == False


def test_actualizar_el_precio_segun_el_nombre():
    sucursal_abasto.limpiar_lista()
    sucursal_abasto.registrar_producto(camisa)

    sucursal_abasto.actualizar_precio_segun(PorNombre("camisa rosa"), 100)

    assert camisa.precio == 3400.0

def test_actualizar_el_precio_segun_el_precio():
    sucursal_abasto.limpiar_lista()
    sucursal_abasto.registrar_producto(camisa)

    sucursal_abasto.actualizar_precio_segun(PorPrecio(1700), 10)

    assert camisa.precio == 1870.0 

def test_actualizar_el_precio_segun_una_categoria_dada():
    sucursal_abasto.limpiar_lista()
    sucursal_abasto.registrar_producto(camisa)

    sucursal_abasto.actualizar_precio_segun(PorCategoria("ropa formal"), 10)

    assert camisa.precio == 1870.0 


def test_actualizar_el_precio_segun_stock():
    sucursal_abasto.limpiar_lista()
    sucursal_abasto.registrar_producto(camisa)
    sucursal_abasto.recargar_stock(101, 10)
    sucursal_abasto.actualizar_precio_segun(PorStock(), 50)
    assert camisa.precio == 2550.0


def test_actualizar_el_precio_que_no_es_de_un_nombre():
    sucursal_abasto.limpiar_lista()
    sucursal_abasto.registrar_producto(camisa)
    
    sucursal_abasto.actualizar_precio_segun(PorOposicion(PorNombre("ropa casual")), 10)

    assert camisa.precio == 1870.0 