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

#Si hubieramos usado esta estructura en lugar del monticulo de minimo, para implementar la cola de prioridad, tendriamos que recorrer toda la lista (SI ESTA DESORDENADA) para encontrar el paciente con mayor prioridad cada vez que querriamos atender a un paciente, lo cual seria ineficiente (O(n) en lugar de O(log n) con el monticulo)

#Aunque la lista este ordenada, seguiria siendo ineficiente, ya que para insertar un nuevo paciente en la posicion correcta, tendriamos que recorrer la lista hasta encontrar la posicion correcta (O(n) en lugar de O(log n) con el monticulo)