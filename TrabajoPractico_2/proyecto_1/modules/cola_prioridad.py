from modules.monticulo_min import MonticuloMin
from modules.paciente import Paciente
class ColaPrioridad:
    def __init__(self):
        self.__monticulo = MonticuloMin()
    

    def agregar_nuevo_paciente(self, paciente_nuevo):
        if not isinstance(paciente_nuevo, Paciente):
            raise ValueError('El paciente tiene que ser un numero entero')
        self.__monticulo.insertar(paciente_nuevo)

    def atender_paciente(self):
        self.__monticulo.eliminarMin()

    