from modules.monticulo_min import MonticuloMin
from modules.paciente import Paciente
#Cola de prioridad: cada elemento tiene una prioridad asociada, y los elementos con mayor prioridad se atienden/eliminan antes 
class ColaPrioridad:
    def __init__(self):
        self.__monticulo = MonticuloMin() #para implementar eficientemente la cola de prioridad usamos un monticulo de minimo

#Monticulo de minimo: estructura de datos en forma de arbol binario completo donde el valor de cada nodo es menor o igual que el de sus hijos. El elemento mínimo de todo el montículo siempre se encuentra en la raíz. Permite insertar y eliminar el mínimo en un tiempo muy eficiente, generalmente O(log n)

    @property
    def monticulo(self):
        return self.__monticulo
    
    def agregar_nuevo_paciente(self, paciente_nuevo): #para que sea generico deberia ser: (self, elemento) o algo asi, que no necesariamente sea un paciente asi podemos usar la cola de prioridad para otros fines
        '''Se agregar un nuevo paciente del tipo Paciente en el monticulo'''
        if not isinstance(paciente_nuevo, Paciente):
            raise ValueError('El objeto debe ser tipo Paciente')
        self.monticulo.insertar(paciente_nuevo)

    def atender_paciente(self):
        '''Devuelve la raiz del monticulo de minimo, que seria el siguiente paciente ha atender'''
        if self.monticulo.tamanoActual==0:
            return None
        return self.monticulo.eliminarMin()
    
    def __len__(self):
        return self.monticulo.tamanoActual
    
    def __iter__(self):
        for i in range(1, self.monticulo.tamanoActual + 1):
            yield self.monticulo.lista[i]
    