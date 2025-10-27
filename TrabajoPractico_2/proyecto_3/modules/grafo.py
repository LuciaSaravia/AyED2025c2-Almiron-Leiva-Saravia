class Vertice:
    def __init__(self, nombre_aldea: str):
        self.__id = nombre_aldea
        self.__ponderacion = 0
        self.__distancia = 0
        self.__predecesor = None
        self.conectadoA = {}
    
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id_nuevo):
        self.__id = id_nuevo
    
    @property
    def ponderacion (self):
        return self.__ponderacion
    
    @ponderacion.setter
    def ponderacion(self, nueva_ponderacion):
        self.__ponderacion = nueva_ponderacion

    @property
    def distancia (self):
        return self.__distancia
    
    @distancia.setter
    def distancia(self, d):
        self.__distancia = d
    
    @property
    def predecesor (self):
        return self.__predecesor
    
    @predecesor.setter
    def predecesor(self, predecesor):
        self.__predecesor = predecesor

    def agregar_vecino(self,vecino,ponderacion):
        self.conectadoA[vecino] = ponderacion 

    def __str__(self):
        return str(self.id) + ' conectadoA: ' + str([x.id for x in self.conectadoA])

    def obtener_vecinos(self):
        return self.conectadoA.keys()

    def obtener(self):
        return self.id

    def obtener_ponderacion(self,vecino): 
        return self.conectadoA[vecino]
    
    #No son necesarias las funciones ya que utilizamos getter y setter
    # def obtener_distancia(self):
    #     return self.distancia
    
    # def asignar_distancia(self, distancia):
    #     self.distancia = distancia 
    
    # def asignar_vecino_predecesor(self, vecinoAnterior):
    #     self.predecesor = vecinoAnterior

    
class Grafo:
    def __init__(self):
        self.listaVertices = {}
        self.__numVertices = 0

    @property
    def numVertices(self):
        return self.__numVertices
    
    @numVertices.setter
    def numVertices(self, valor):
        self.__numVertices += valor

    def agregarVertice(self,nombre_Aldea):
        self.numVertices = self.numVertices + 1
        nuevoVertice = Vertice(nombre_Aldea)
        self.listaVertices[nombre_Aldea] = nuevoVertice
        return nuevoVertice

    def obtenerVertice(self,n):
        if n in self.listaVertices:
            return self.listaVertices[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.listaVertices

    def agregarArista(self, origen, destino, costo = 0): #costo = ponderacion
        if origen not in self.listaVertices:
            nuevo_vertice = self.agregarVertice(origen)
        if destino not in self.listaVertices:
            nuevo_vertice = self.agregarVertice(destino)
        self.listaVertices[origen].agregar_vecino(self.listaVertices[destino], costo)

    def obtenerVertices(self):
        return self.listaVertices.keys()

    def __iter__(self):
        return iter(self.listaVertices.values())
    
    def __len__(self):
        return len(self.numVertices)
