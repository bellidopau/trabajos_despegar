from tp3Objetos import *
from datetime import datetime
from persistencia import *

import subprocess

#subprocess.call(["zenity", "--info",  '--title=La oprecion se realizo con exito', "--text=Sucursal con productos stockeados", "--display=:0"])
ejemplo_1 = "TAREA"

def main():
    guardar("ejemplo_1", ejemplo_1)
    
    print(datetime.now(), "eliminando productos sin stock")
    
    retiro = cargar("ejemplo_1")
    #retiro = cargar("retiro")
    print(retiro)
"""
    retiro.guardar("retiro", retiro)
    retiro.discontinuar_producto()
    retiro.cargar_todos()
    
    print(datetime.now(), "los productos sin stock se eliminaron")
"""

if __name__ == "__main__":
  main()