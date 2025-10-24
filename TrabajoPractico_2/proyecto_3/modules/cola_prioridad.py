from modules.grafo import Vertice

class ColaPrioridad:
    def __init__(self):
        self.listaMonticulo = [None]
        self.__tamanoActual = 0    
    
    @property
    def tamanoActual(self):
        return self.__tamanoActual
    
    @tamanoActual.setter
    def tamanoActual(self, tamano_nuevo):
        self.__tamanoActual = tamano_nuevo

    def estaVacia(self):
        return self.tamanoActual == 0

    def tamanio(self):
        return self.tamanoActual

    def construirMonticulo(self, distancias):
        i = len(distancias) // 2
        self.tamanoActual = len(distancias)
        self.listaMonticulo = [None] + distacias[:]
        while (i > 0):
            self.infiltAbajo(i)
            i = i - 1

    def eliminarMin(self):
        '''Devuelve la raiz del monticulo y selecciona una nueva raiz'''
        valorSacado = self.listaMonticulo[1]
        self.listaMonticulo[1] = self.listaMonticulo[self.tamanoActual]
        self.tamanoActual = self.tamanoActual - 1
        self.listaMonticulo.pop()
        self.infiltAbajo(1)
        return valorSacado

    def infiltArriba(self, valor):
            while valor // 2 > 0:
                if self.listaMonticulo[valor] < self.listaMonticulo[valor // 2]:
                    tmp = self.listaMonticulo[valor // 2]
                    self.listaMonticulo[valor // 2] = self.listaMonticulo[valor]
                    self.listaMonticulo[valor] = tmp
                elif self.listaMonticulo[valor] < self.listaMonticulo[(valor //2) + 1]:
                    tmp = self.listaMonticulo[(valor//2)+1]
                    self.listaMonticulo[(valor//2)+1] = self.listaMonticulo[valor]
                    self.listaMonticulo[valor] = tmp
            valor = valor // 2

    def infiltAbajo(self,i):
            while (i * 2) <= self.tamanoActual:
                hm = self.hijoMin(i)
                if self.listaMonticulo[i] > self.listaMonticulo[hm]:
                    tmp = self.listaMonticulo[i]
                    self.listaMonticulo[i] = self.listaMonticulo[hm]
                    self.listaMonticulo[hm] = tmp
                i = hm

    def hijoMin(self,i):
          if i * 2 + 1 > self.tamanoActual:
              return i * 2
          else:
              if self.listaMonticulo[i*2] < self.listaMonticulo[i*2+1]:
                  return i * 2
              else:
                  return i * 2 + 1
              
    def decrementarClave(self, vertice: Vertice, nueva_ponderacion): 
        if vertice is None:
            return
        vertice.asignarDistancia(nueva_ponderacion) 
        for i in range(1, self.tamanoActual + 1):
            dist, v = self.listaMonticuloMonticulo[i]
            if v is vertice:
                self.listaMonticuloMonticulo[i] = (nueva_ponderacion, v)
                self.infiltArriba(i)
                break
        
if __name__=='__main__':
    listaMonticulo = [1, 5, 6, 14, 9, 27, 31, 2]
    cp = ColaPrioridad()
    cp.construirMonticulo(listaMonticulo)
    print(cp.tamanoActual)
    print(cp.eliminarMin())
    print(cp.listaMonticulo)