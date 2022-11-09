from tp3Objetos import *
from datetime import datetime
from persistencia import *

import subprocess

#subprocess.call(["zenity", "--info",  '--title=La oprecion se realizo con exito', "--text=Sucursal con productos stockeados", "--display=:0"])


def main():
    print(datetime.now(), "eliminando productos sin stock")
    retiro = cargar("retiro")
    retiro.discontinuar_producto()
    retiro.cargar_todos()
    retiro.guardar("retiro", retiro)
    print(datetime.now(), "los productos sin stock se eliminaron")

if __name__ == "__main__":
  main()