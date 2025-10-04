from modules.monticulo_min import MonticuloMin
from modules.paciente import Paciente
class ColaPrioridad:
    def __init__(self):
        self.__monticulo = MonticuloMin()

    @property
    def monticulo(self):
        return self.__monticulo
    
    def agregar_nuevo_paciente(self, paciente_nuevo):
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
    