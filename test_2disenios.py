from Disenios_para_MacoWins import *

def test_si_registra_un_producto_se_agrega_a_la_lista():
    limpiar_lista()
    registrar_producto(medias)
    assert medias in productos

def test_la_tienda_esta_vacia():
    limpiar_lista()
    assert medias not in productos

def test_recarga_10_blusas_a_la_lista():
    limpiar_lista()
    registrar_producto({"codigo":300,
    "nombre":"blusa",
    "categoria":"remera","precio":2900})
    recargar_stock(300, 10)
    assert hay_stock(300)

def test_si_los_2_prod_registrados_tienen_stock():
    limpiar_lista()
    registrar_producto(blusa)
    registrar_producto(short)
    recargar_stock(400, 25)
    assert not hay_stock(300)

#def test_calcular_precio_final_impuestos():
    #assert calcular_precio_final(blusa, True)==(2900)

#def test_calcular_precio_final_sin_impuestos():
    #assert calcular_precio_final(short, False) ==(2800)

def test_se_agrego_compra_a_lista_ventas():
    limpiar_lista()
    registrar_producto({"codigo":300,
    "nombre":"blusa",
    "categoria":"remera","precio":2900})
    recargar_stock(300,10)
    realizar_compra(300,3)
    assert [{'anio': '2022', 'cantidad_vendida': 3, 'monto': 8700, 'producto':'blusa de seda' }] in ventas

    #assert {'cantidad': 3, 'codigo_producto': 300, 'fecha': -2020, 'precio': 8700} in ventas

def test_se_agrego_un_producto_a_la_lista():
    limpiar_lista()
    registrar_producto(collar)
    assert collar in productos

def test_si_cuenta_categorias_unicas():
    limpiar_lista()
    registrar_producto(wideleg)
    assert contar_categorias(productos)==1

def test_si_cuenta_categorias_diferentes():
    limpiar_lista()
    registrar_producto(blazer)
    registrar_producto(medias)
    registrar_producto(corbata)
    assert contar_categorias(productos)==2

def test_realiza_compra_de_un_producto_con_stock_en_100_disminuye_a_50():
    limpiar_lista()
    registrar_producto(blazer)
    recargar_stock(80, 100)
    realizar_compra(80, 50)
    assert blazer["stock"]== 50 

def test_realiza_compra_de_1_producto():
    limpiar_lista()
    registrar_producto(corbata)
    recargar_stock(500, 100)
    realizar_compra(500, 1)
    assert (ventas)==1

def test_elimina_un_producto_en_la_lista_sin_stock():
    limpiar_lista()
    registrar_producto(blusa)
    registrar_producto(collar)
    recargar_stock(300, 41)
    assert discontinuar_producto

def test_las_ventas_de_hoy():
    limpiar_lista()
    registrar_producto(camisa)
    registrar_producto(campera)
    recargar_stock(600, 98)
    recargar_stock(110, 60)
    realizar_compra(600, 3)
    realizar_compra(110, 3)
    assert valor_ventas_del_dia()


def test_ventas_de_otro_dia():
    limpiar_lista()
    registrar_producto(camisa)
    registrar_producto(campera)
    recargar_stock(600, 98)
    recargar_stock(110, 60)
    realizar_compra(600, 3)
    realizar_compra(110, 3)
    assert not valor_ventas_del_dia()



def test_a_producto_short_se_le_actualiza_precio():
    limpiar_lista()
    registrar_producto(short)
    registrar_producto(medias)
    assert actualizar_precios_por_categoria
