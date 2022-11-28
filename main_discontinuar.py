from tp3Objetos import *
from datetime import datetime
from persistencia import *

import subprocess

#subprocess.call(["zenity", "--info",  '--title=La operacion se realizo con exito', "--text=Sucursal con productos stockeados", "--display=:0"])
#ejemplo_1 = "sucursales"

def main():
    sucursales = cargar_todos()
    for nombre in sucursales:
      sucursal1 = sucursales[nombre]
      sucursal1.discontinuar_productos()
      guardar("sucursal1", sucursal1)
    
    #guardar("sucursal_1", sucursal_rosario)
    
    
    
if __name__ == "__main__":
  main()

"""for x in sucursal_rosario:
     
     sucursal_rosario.discontinuar_producto()
     print(datetime.now(), "eliminando productos sin stock")"""