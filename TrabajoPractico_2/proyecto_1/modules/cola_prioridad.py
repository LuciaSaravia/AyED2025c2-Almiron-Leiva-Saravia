from modules.monticulo_min import MonticuloMin
from modules.paciente import Paciente
class ColaPrioridad:
    def __init__(self):
        self.__monticulo = MonticuloMin()
    

    def agregar_nuevo_paciente(self, paciente_nuevo):
        if not isinstance(paciente_nuevo, Paciente):
            raise ValueError('El paciente tiene que ser un numero entero')
        paciente_nuevo._Paciente__tiempo = self.__contador_llegadas
        self.__contador_llegadas += 1
        self.__monticulo.insertar(paciente_nuevo)

    def atender_paciente(self):
        if self.__monticulo==0:
            return None
        
        return self.__monticulo.eliminarMin()
    
    def hay_pacientes(self):
        return self.__monticulo.tamanoActual > 0

    