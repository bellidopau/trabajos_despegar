from tp3Objetos import *
remera = Prenda(100,"remera1","remera",1500)
sucursal_abasto = SucursalFisica(1000)


def test_se_registro_el_producto_remera():
    sucursal_abasto.registrar_producto(remera)
    assert len(sucursal_abasto.productos)== 1 