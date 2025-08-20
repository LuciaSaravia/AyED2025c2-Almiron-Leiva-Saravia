from modules.nodo import Nodo
class ListaDobleEnlazada:
    def __init__(self):
        self.__cabeza = None
        self.__cola = None
        self.__taminio = 0

    def agregar_al_inicio(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.__cabeza is None:
            self.__cabeza = nuevo_nodo
            self.__cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.__cabeza