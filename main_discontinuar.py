from tp3Objetos import *
from datetime import datetime
from persistencia import *

def main():
    sucursales = cargar_todos()
    for nombre in sucursales:
      print(datetime.now(), "Discontinuando productos de la sucursal", nombre)
      sucursal1 = sucursales[nombre]
      sucursal1.discontinuar_producto()
      guardar("sucursal1", sucursal1)
    
if __name__ == "__main__":
  print(datetime.now(), "Discontinuando productos")
  main()