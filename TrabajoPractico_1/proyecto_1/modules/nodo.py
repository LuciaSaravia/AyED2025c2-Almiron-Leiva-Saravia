
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
    @property
    def anterior(self):
        return self.__anterior
    @anterior.setter
    def anterior(self, dato):
        self.__anterior =dato
    @property
    def dato(self):
        return self.__dato
    @dato.setter
    def dato(self, dato):
        self.__dato = dato
    
    
        