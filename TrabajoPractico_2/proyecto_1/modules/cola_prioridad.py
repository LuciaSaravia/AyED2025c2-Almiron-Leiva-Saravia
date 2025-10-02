from modules.monticulo_min import MonticuloMin
from modules.paciente import Paciente
class ColaPrioridad:
    def __init__(self):
        self.__monticulo = MonticuloMin()
        self.__contador_llegadas = 0

    def agregar_nuevo_paciente(self, paciente_nuevo):
        if not isinstance(paciente_nuevo, Paciente):
            raise ValueError('El objeto debe ser tipo Paciente')
        paciente_nuevo._Paciente__tiempo = self.__contador_llegadas #asignamos un orden de llegada
        self.__contador_llegadas += 1
        self.__monticulo.insertar(paciente_nuevo)

    def atender_paciente(self):
        if self.__monticulo.tamanoActual==0:
            return None
        
        return self.__monticulo.eliminarMin()
    
    def hay_pacientes(self):
        return self.__monticulo.tamanoActual > 0

    