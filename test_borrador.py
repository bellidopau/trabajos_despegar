from tp3Objetos import PorCategoria, PorPrecio, Prenda, Sucursal, SucursalFisica


sucursal_1 = SucursalFisica(3)
camisa = Prenda(101, "camisa x", "casual", 2000)
def test_actualizar_el_precio_segun_una_categoria_dada():
    sucursal_1.limpiar_lista()
    sucursal_1.registrar_producto(camisa)

    sucursal_1.actualizar_precio_segun(PorCategoria("casual"), 10)

    assert camisa.precio == 2200 


def test_actualizar_el_precio_que_no_es_de_una_categoria():
    sucursal_1.limpiar_lista()
    sucursal_1.registrar_producto(camisa)

    sucursal_1.actualizar_precio_segun(
        
        NoPorCategoria("casual")
        
        
        , 10)

    assert camisa.precio == 2000 

def test_actualizar_el_precio_que_no_es_de_un_nombre():
    sucursal_1.limpiar_lista()
    sucursal_1.registrar_producto(camisa)

    sucursal_1.actualizar_precio_segun(
        
        NoPorNombre("casual")
        
        
        , 10)

    assert camisa.precio == 2000 



def test_actualizar_el_precio_que_no_es_de_un_precio():
    sucursal_1.limpiar_lista()
    sucursal_1.registrar_producto(camisa)

    sucursal_1.actualizar_precio_segun(
        
        NoPorPrecio(1000)
        
        
        , 10)

    assert camisa.precio == 2000 

