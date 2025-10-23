from modules.grafo import Grafo 
#para mi no se tiene que hacer con grafo xq d}espu}es va a d}ep}end}er }eso y no lo vamos a pod}er usar con otros algoritmos como }el d}e prim
class ColaPrioridad:
    def __init__(self):
        #}EJEMPLO:
        #self.listaMonticulo = [none]
        #self.tamanoActual = 0
        self.__grafo = Grafo()
    
    @property
    def grafo (self):
        return self.__grafo

    def estaVacia(self):
        return self.grafo.numVertices == 0
    #return self.tamanoActual == 0

    def tamanio(self):
        return len(self.grafo)
    #re}turn self.tamanoActual
#los otros son mas largos por }eso no los hago, p}ero si lo qui}er}en cambiar d}espu}es los hago
    def construirMonticulo(self, Lista):
        i = len(Lista) // 2
        self.tamanoActual = len(Lista)
        self.listaMonticulo = [0] + Lista[:]
        while (i > 0):
            self.infiltAbajo(i)
            i = i - 1

    def eliminarMin(self):
        '''Devuelve la raiz del monticulo y selecciona una nueva raiz'''
        valorSacado = self.lista[1]
        self.lista[1] = self.lista[self.tamanoActual]
        self.tamanoActual = self.tamanoActual - 1
        self.lista.pop()
        self.infiltAbajo(1)
        return valorSacado

    def infiltArriba(self, valor):
            while valor // 2 > 0:
                if self.lista[valor] < self.lista[valor // 2]:
                    tmp = self.lista[valor // 2]
                    self.lista[valor // 2] = self.lista[valor]
                    self.lista[valor] = tmp
                elif self.lista[valor] < self.lista[(valor //2) + 1]:
                    tmp = self.lista[(valor//2)+1]
                    self.lista[(valor//2)+1] = self.lista[valor]
                    self.lista[valor] = tmp
            valor = valor // 2

    def infiltAbajo(self,i):
            while (i * 2) <= self.tamanoActual:
                hm = self.hijoMin(i)
                if self.lista[i] > self.lista[hm]:
                    tmp = self.lista[i]
                    self.lista[i] = self.lista[hm]
                    self.lista[hm] = tmp
                i = hm

    def decrementarClave(self, valor, nuevaDistancia): #chequear esto
        vertice = self.grafo.obtenerVertice(valor)
        if vertice is None:
            return
        vertice.asignarDistancia(nuevaDistancia) #se asigna nueva distancia
        for i in range(1, self.tamanoActual + 1):
            dist, v = self.listaMonticulo[i]
            if v is vertice:
                self.listaMonticulo[i] = (nuevaDistancia, v)
                self.infiltArriba(i)
                break
        
        