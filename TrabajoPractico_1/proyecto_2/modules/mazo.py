from modules.LDE import ListaDobleEnlazada  

class DequeEmptyError(Exception):
    pass

class Mazo:
    def __init__(self):
        self.__LDE = ListaDobleEnlazada()
     
    def poner_carta_arriba(self, carta):
        self.__LDE.agregar_al_inicio(carta)

    def sacar_carta_arriba(self, mostrar= False):
        if self.__LDE.esta_vacia():
                return DequeEmptyError('No hay mas cartas')
        
        if mostrar == True:
            carta = self.__LDE.cabeza
            carta.visible = True
            return carta
        else:
            carta = self.__LDE.cabeza 
            return carta

    def poner_carta_abajo(self, carta):
        self.__LDE.agregar_al_final(carta)