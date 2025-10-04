
class Nodo:
    def __init__(self, dato):
        self.__dato = dato
        self.__siguiente = None
        self.__anterior = None

    @property
    def siguiente(self):
        return self.__siguiente
    
    @siguiente.setter
    def siguiente(self, dato):
        self.__siguiente = dato