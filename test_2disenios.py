from Disenios_para_MacoWins import *

def test_si_registra_un_producto_se_agrega_a_la_lista():
    limpiar_lista()
    registrar_producto(medias)
    assert medias in productos

def test_la_tienda_esta_vacia():
    limpiar_lista()
    assert medias not in productos



