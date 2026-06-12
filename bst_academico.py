from dataclasses import dataclass
from collections import deque

@dataclass
class Estudiante:
    codigo:int
    nombre:str
    ppa:float

class NodoBST:
    def __init__(self,dato):
        self.dato=dato
        self.izquierdo=None
        self.derecho=None

class ArbolAcademico:
    def __init__(self):
        self.raiz=None

    def insertar(self,e):
        self.raiz=self._insertar(self.raiz,e)

    def _insertar(self,n,e):
        if n is None:
            return NodoBST(e)
        if e.codigo<n.dato.codigo:
            n.izquierdo=self._insertar(n.izquierdo,e)
        elif e.codigo>n.dato.codigo:
            n.derecho=self._insertar(n.derecho,e)
        return n

    def buscar(self,codigo):
        n=self.raiz
        while n:
            if codigo==n.dato.codigo: return n.dato
            n=n.izquierdo if codigo<n.dato.codigo else n.derecho
        return None

if __name__=="__main__":
    arbol=ArbolAcademico()
    arbol.insertar(Estudiante(20210500,"Juan",15.8))
    arbol.insertar(Estudiante(20210300,"Maria",14.2))
    print(arbol.buscar(20210300))
