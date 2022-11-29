import pickle, glob

import pickle
import importlib

class CustomUnpickler(pickle.Unpickler):
  def __init__(self, modulo, **args) -> None:
    super().__init__(**args)
    self.modulo = modulo

  def find_class(self, module, name):
    try:
      return getattr(importlib.import_module(self.modulo), name)
    except AttributeError:
      return super().find_class(module, name)

def guardar(nombre, elemento):
  with open(f"{nombre}.pickle", "wb") as f:
    pickle.dump(elemento, f)

def cargar(nombre, modulo=None):
  with open(f"{nombre}.pickle", "rb") as f:
    if modulo is not None:
      return CustomUnpickler(file=f, modulo=modulo).load()
    else:
      return pickle.load(f)

def cargar_todos(modulo=None):
  elementos = {}
  for path in glob.glob("*.pickle"):
    nombre = path.replace(".pickle", "")
    elementos[nombre] = cargar(nombre, modulo=modulo)

  return elementos