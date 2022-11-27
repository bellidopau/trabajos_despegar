from tp3Objetos import *
from datetime import datetime
from persistencia import *

import subprocess

#subprocess.call(["zenity", "--info",  '--title=La oprecion se realizo con exito', "--text=Sucursal con productos stockeados", "--display=:0"])
#ejemplo_1 = "sucursales"

def main():
    guardar("sucursal_1", sucursal_rosario)
    sucursal_rosario = cargar_todos()
    
    
if __name__ == "__main__":
  for x in sucursal_rosario:
     sucursal_rosario.discontinuar_producto()
     print(datetime.now(), "eliminando productos sin stock")