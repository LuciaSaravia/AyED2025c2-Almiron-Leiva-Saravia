# -*- coding: utf-8 -*-

from random import randint, choices

nombres = ['Leandro', 'Mariela', 'Gastón', 'Andrea', 'Antonio', 'Estela', 'Jorge', 'Agustina']
apellidos = ['Perez', 'Colman', 'Rodriguez', 'Juarez', 'García', 'Belgrano', 'Mendez', 'Lopez']

niveles_de_riesgo = [1, 2, 3]
descripciones_de_riesgo = ['crítico', 'moderado', 'bajo']
# probabilidades de aparición de cada tipo de paciente
probabilidades = [0.1, 0.3, 0.6] 

class Paciente:
    def __init__(self, orden):
        n = len(nombres)
        self.__nombre = nombres[randint(0, n-1)]
        self.__apellido = apellidos[randint(0, n-1)]
        self.__riesgo = choices(niveles_de_riesgo, probabilidades)[0]
        self.__descripcion = descripciones_de_riesgo[self.__riesgo-1]
        self.__orden = orden

    @property
    def nombre(self):
        return self.__nombre
    @property
    def apellido(self):
        return self.__apellido
    @property
    def riesgo(self):
        return self.__riesgo
    @property
    def descripcion(self):
        return self.__descripcion
    @property
    def orden(self):
        return self.__orden
    
    def __str__(self):
        cad = self.__nombre + ' '
        cad += self.__apellido + '\t -> '
        cad += str(self.__riesgo) + '-' + self.__descripcion
        return cad
    
    def __lt__(self, otro_paciente):
        '''Permite aplicar el segundo criterio para la cola de prioridad'''
        if self.riesgo != otro_paciente.riesgo: #si los riesgos son distintos va a pasar el menor (1)
            return self.riesgo < otro_paciente.riesgo
        return self.orden < otro_paciente.orden #si tienen el mismo riesgo gana el menor (llego primero)

        
        