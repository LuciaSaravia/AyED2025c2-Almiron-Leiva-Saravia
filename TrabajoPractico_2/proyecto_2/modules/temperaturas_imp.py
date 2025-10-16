from modules.arbol_VL import AVL
from datetime import datetime

class Temperatura_DB():
    def __init__(self):
        self.arbol = AVL()


    def guardar_temperatura(self,temperatura, fecha): #probada
        '''Guarda la medida de temperatura asociada a la fecha.'''
        self.arbol.agregar(fecha, temperatura)

    def devolver_temperatura(self, fecha): #probada
        '''devuelve la medida de temperatura en la fecha determinada.'''
        if not isinstance(fecha, datetime):
            raise TypeError('La fecha tiene que ser de tipo datetime')
        return self.arbol.obtener(fecha)

    def max_temp_rango(self, fecha1, fecha2): #probada
        '''devuelve la temperatura máxima entre los rangos fecha1 y fecha2 inclusive (fecha1 < fecha2)'''
        lista = self.arbol.obtener_rango(fecha1, fecha2)
        return  max(lista)

    def min_temp_rango(self, fecha1, fecha2 ): #probada
        '''devuelve la temperatura mínima entre los rangos fecha1 y fecha2 inclusive (fecha1 < fecha2)'''
        lista = self.arbol.obtener_rango(fecha1, fecha2)
        return min(lista)

    def temp_extremos_rangos(self, fecha1, fecha2): #probada
        '''devuelve la temperatura mínima y máxima entre los rangos fecha1 y fecha2 inclusive (fecha1 < fecha2)'''
        lista = self.arbol.obtener_rango(fecha1, fecha2)
        return (min(lista), max(lista))

    def borrar_temperatura(self, fecha): 
        '''recibe una fecha y elimina del árbol la medición correspondiente a esa fecha'''
        return self.arbol.eliminar()

    def devolver_temperaturas(self, fecha1, fecha2): #probada
        '''devuelve un listado de las mediciones de temperatura en el rango recibido'''
        return self.arbol.obtener_rango(fecha1, fecha2)

    def cantidad_muestras(self): #probada
        '''devuelve la cantidad de muestras de la base de datos'''
        return len(self.arbol)