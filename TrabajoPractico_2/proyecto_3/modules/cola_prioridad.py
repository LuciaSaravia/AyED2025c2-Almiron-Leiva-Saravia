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

    def construirMonticulo(self, distancias): #distancias puede ser una lista de tuplas o una lista simple
        #Poreso aca, si el item en distancias es una tupla, lo agrego tal cual, sino lo convierto en tupla (item, None)
        lista_preparada = []
        for item in distancias:
            if isinstance(item, tuple):
                lista_preparada.append(item)
            else:
                lista_preparada.append((item, None))
                
        self.tamanoActual = len(lista_preparada)
        self.listaMonticulo = [None] + lista_preparada
        i = len(lista_preparada) // 2
        while (i > 0):
            self.infiltAbajo(i)
            i = i - 1

    def eliminarMin(self):
        '''Devuelve la raiz del monticulo y selecciona una nueva raiz'''
        if self.tamanoActual == 0:
            return None
        valorSacado = self.listaMonticulo[1]
        self.listaMonticulo[1] = self.listaMonticulo[self.tamanoActual]
        self.tamanoActual = self.tamanoActual - 1
        self.listaMonticulo.pop()
        if self.tamanoActual > 0:
            self.infiltAbajo(1)
        return valorSacado

    def infiltArriba(self, valor):
        while valor // 2 > 0:
            if self.listaMonticulo[valor][0] < self.listaMonticulo[valor // 2][0]:
                tmp = self.listaMonticulo[valor // 2]
                self.listaMonticulo[valor // 2] = self.listaMonticulo[valor]
                self.listaMonticulo[valor] = tmp
            elif self.listaMonticulo[valor][0] < self.listaMonticulo[(valor //2) + 1][0]:
                tmp = self.listaMonticulo[(valor//2)+1]
                self.listaMonticulo[(valor//2)+1] = self.listaMonticulo[valor]
                self.listaMonticulo[valor] = tmp
            valor = valor // 2

    def infiltAbajo(self,i):
            while (i * 2) <= self.tamanoActual:
                hm = self.hijoMin(i)
                if self.listaMonticulo[i] is not None and self.listaMonticulo[hm] is not None:
                    if self.listaMonticulo[i][0] > self.listaMonticulo[hm][0]: 
                        tmp = self.listaMonticulo[i]
                        self.listaMonticulo[i] = self.listaMonticulo[hm]
                        self.listaMonticulo[hm] = tmp
                i = hm

    def hijoMin(self,i):
          if i * 2 + 1 > self.tamanoActual:
              return i * 2
          else:
              if self.listaMonticulo[i*2][0] < self.listaMonticulo[i*2+1][0]:
                  return i * 2
              else:
                  return i * 2 + 1
              
    def decrementarClave(self, vertice: Vertice, nueva_ponderacion): 
        if vertice is None:
            return
        vertice.distancia = nueva_ponderacion
        for i in range(1, self.tamanoActual + 1):
            dist, v = self.listaMonticulo[i]
            if v is vertice:
                self.listaMonticulo[i] = (nueva_ponderacion, v)
                self.infiltArriba(i)
                break
            
    def __contains__(self, vertice: Vertice):
        for i in range(1, self.tamanoActual + 1):
            dist, v = self.listaMonticulo[i]
            if v is vertice:
                return True
        return False
    
    def __iter__(self):
        return iter(self.listaMonticulo[1:]) 
    
if __name__=='__main__':
    listaMonticulo = [1, 5, 6, 14, 9, 27, 31, 2]
    cp = ColaPrioridad()
    cp.construirMonticulo(listaMonticulo)
    print("tamaño actual", cp.tamanoActual)
    print("mínimo eliminado", cp.eliminarMin())
    print("estado de la lista de montículo", cp.listaMonticulo)   
    
    # Prueba con vértices
    from modules.grafo import Grafo
    g = Grafo()
    g.agregarArista(1, 2, 1)
    g.agregarArista(2, 3, 2)
    g.agregarArista(3, 4, 3)
    g.agregarArista(4, 1, 4)
    g.agregarArista(5, 3, 5)
    vertices = [(float('inf'), v) for v in g]
    cp2 = ColaPrioridad()
    cp2.construirMonticulo(vertices)
    print("\nPrueba con vértices")
    print("tamaño actual", cp2.tamanoActual)