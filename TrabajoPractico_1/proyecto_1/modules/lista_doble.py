from modules.nodo import Nodo
class ListaDobleEnlazada:
    def __init__(self):
        self.__cabeza = None
        self.__cola = None
        self.__tamanio = 0
    
    @property
    def cabeza (self):
        return self.__cabeza
    @cabeza.setter
    def cabeza(self, dato):
        self.__cabeza = dato
    @property
    def cola(self):
        return self.__cola
    @cola.setter
    def cola(self, dato):
        self.__cola = dato
    @property
    def tamanio(self):
        return self.__tamanio
    @tamanio.setter
    def tamanio(self, dato):
        self.__tamanio = dato
        
    def agregar_al_inicio(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo
        self.tamanio += 1
            
    def agregar_al_final(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.anterior = self.cola
        self.cola.siguiente = nuevo_nodo
        self.cola = nuevo_nodo
        
    def insertar(self,dato,posicion):
        if posicion<0 or posicion>self.tamanio:
            raise Exception ("Posición invalida")
        if posicion==0:
            self.agregar_al_inicio(dato)
        elif posicion==self.tamanio:
            self.agregar_al_final(dato)
        else:
            nuevo_nodo=Nodo(dato)
            actual=self.cabeza
            for __ in range (posicion): #hay que cambiar __
                actual=actual.siguiente
            nuevo_nodo.anterior=actual.anterior
            nuevo_nodo.siguiente=actual
            actual.anterior.siguinte=nuevo_nodo
            actual.anterior=nuevo_nodo
    
    def copiar (self):
        copia=ListaDobleEnlazada()
        actual=self.cabeza
        while actual is not None:
            copia.agregar_al_final(actual.dato)
            actual=actual.siguiente
        return copia

    def esta_vacia(self):
        if self.tamanio==0:
            return True
        else:
            return False
        
    def extraer(self, posicion=None):
        actual = self.cola
        previo = None
        encontrado = False
        while not encontrado:
            if posicion is None:
                previo = self.cola.anterior
                
                
            
        
    
    def __len__(self):
        return self.tamanio
    def __iter__(self):
        pass
if __name__ == '__main__':
    lista= ListaDobleEnlazada()
    lista.agregar_al_inicio(3)
    lista.agregar_al_final(6)
    lista.agregar_al_inicio(8)
    lista.agregar_al_inicio(17)
    lista.extraer()    