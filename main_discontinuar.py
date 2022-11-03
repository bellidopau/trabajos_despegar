from tp3Objetos import *
from datetime import datetime
from persistencia import cargar_todos

import subprocess

subprocess.call(["zenity", "--info",  '--title=Hola', "--text=¡Hola mundo!", "--display=:0"])


def main():
    print(datetime.now(), "eliminando productos sin stock")
Sucursal.discontinuar_producto()
print(datetime.now(), "los productos sin stock se eliminaron")

if __name__ == "__main__":
  main()