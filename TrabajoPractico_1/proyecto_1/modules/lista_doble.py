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

    def esta_vacia(self):
        if self.tamanio == 0:
            return True
        else:
            return False

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
        if self.cola is None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            self.cola.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.cola
            self.cola = nuevo_nodo
        self.tamanio += 1

    def insertar(self,dato,posicion):
        if posicion < 0 or posicion  > self.tamanio:
            raise Exception ("Posición invalida")
        if posicion == 0:
            self.agregar_al_inicio(dato)
        elif posicion == self.tamanio:
            self.agregar_al_final(dato)
        else:
            nuevo_nodo = Nodo(dato)
            actual = self.cabeza
            for _ in range (posicion):
                actual = actual.siguiente
            nuevo_nodo.anterior = actual.anterior
            nuevo_nodo.siguiente = actual
            actual.anterior.siguiente = nuevo_nodo
            actual.anterior = nuevo_nodo
            self.tamanio += 1

    def extraer(self, posicion=None):
        if self.esta_vacia():
            raise Exception("La lista está vacía")
        if posicion < 0 or posicion >= self.tamanio:
            raise Exception("Posición inválida")
        # if posicion is None:
        #     posicion = self.tamanio - 1 #saca el último si no le da posicion
        if posicion == 0:  # saca la cabeza
            dato = self.cabeza.dato
            self.cabeza = self.cabeza.siguiente
            if self.cabeza is not None:
                self.cabeza.anterior = None
            else:
                self.cola = None
            self.tamanio -= 1
            return dato
        elif posicion == self.tamanio or posicion is None: #saca la cola
            dato = self.cola.dato
            self.cola = self.cola.anterior
            if self.cola is not None:
                self.cola.siguiente = None
            else:
                self.cabeza = None
            self.tamanio -= 1
            return dato
        else: #saca medio
            actual = self.cabeza
            for _ in range(posicion):
                actual = actual.siguiente
            dato = actual.dato
            actual.anterior.siguiente = actual.siguiente
            actual.siguiente.anterior = actual.anterior
            self.tamanio -= 1
            return dato

    def copiar(self):
        copia = ListaDobleEnlazada()
        actual = self.cabeza
        while actual is not None:
            copia.agregar_al_final(actual.dato)
            actual = actual.siguiente
        return copia

    def invertir(self):
        actual = self.cabeza
        cabeza = self.cabeza
        while actual is not None:
            temp = actual.siguiente
            actual.siguiente = actual.anterior
            actual.anterior = temp
            actual = temp
        self.cabeza = self.cola
        self.cola = cabeza

    #def concatenar(self, otra_lista):
        
   

    def __len__(self):
        return self.tamanio
    
    def __add__(self, otra_lista):
        nueva=self.copiar()
        nueva.concatenar(otra_lista) #usando la funcion de concatenar pero todavia no la tenemos
        return nueva
#si no usamos concatenar, capaz podemos usar el de agregar al final pero me parece que queda mas largo
    def __iter__(self):
        actual = self.cabeza


        
if __name__ == '__main__':
    lista= ListaDobleEnlazada()
    lista.agregar_al_inicio(3)
    lista.agregar_al_final(8)
    lista.agregar_al_final(6)
    lista.agregar_al_inicio(17)
    lista.invertir()