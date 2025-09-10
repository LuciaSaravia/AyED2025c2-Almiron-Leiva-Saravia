from modules.LDE import ListaDobleEnlazada  
from modules.carta import Carta
class DequeEmptyError(Exception):
    pass

class Mazo:
    def __init__(self):
        self.__LDE = ListaDobleEnlazada()
     
    def poner_carta_arriba(self, carta):
        self.__LDE.agregar_al_inicio(carta)

    def sacar_carta_arriba(self, mostrar= False):
        if self.__LDE.esta_vacia():
                raise DequeEmptyError('No hay mas cartas')
        
        if mostrar == True:
            carta = self.__LDE.cabeza
            carta.visible = True
        
        carta_guardada=self.__LDE.cabeza.dato
        self.__LDE.extraer(0)
        return carta_guardada

    def poner_carta_abajo(self, carta):
        self.__LDE.agregar_al_final(carta)

    def __len__(self):
        return self.__LDE.__len__()

if __name__ == '__main__':
    mazo= Mazo()
    carta_1 = Carta("5", "trebol")
    carta_2 = Carta('3', 'corazon')
    mazo.poner_carta_arriba(carta_1)
    mazo.poner_carta_arriba(carta_2)
    carta_control = mazo.sacar_carta_arriba()
    print(f'{carta_control} es igual a {carta_2}')