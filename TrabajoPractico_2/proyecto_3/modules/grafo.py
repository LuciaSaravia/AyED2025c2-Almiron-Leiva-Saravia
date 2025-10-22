class Vertice:
    def __init__(self, nombre_aldea: str):
        self.__id = nombre_aldea
        self.__distancia = None
        self.__predecesor = None
        self.conectadoA = {}
    
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id_nuevo):
        self.__id = id_nuevo

    @property
    def distancia (self):
        return self.__distancia
    
    @property
    def predecesor (self):
        return self.__predecesor
    
    @predecesor.setter
    def predecesor(self, predecesor):
        self.__predecesor = predecesor

    def agregarVecino(self,vecino,distancia=0):
        self.conectadoA[vecino] = distancia # distancia = ponderacion

    def __str__(self):
        return str(self.id) + ' conectadoA: ' + str([x.id for x in self.conectadoA])

    def obtenerVecinos(self):
        return self.conectadoA.keys()

    def obtener(self):
        return self.id

    def obtenerPonderacion(self,vecino): 
        return self.conectadoA[vecino]
    
    def obtenerDistancia(self, vertice = None):
        if not vertice:
            return self.distancia
        else:
            return self.conectadoA[vertice]
    
    def asignarDistancia(self, distancia):
        self.distancia = distancia 
    
    def asignarVecinoPredecesor(self, vecinoAnterior):
        self.predecesor = vecinoAnterior

    
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

    def agregarArista(self, origen, destino, costo = 0):
        if origen not in self.listaVertices:
            nuevo_vertice = self.agregarVertice(origen)
        if destino not in self.listaVertices:
            nuevo_vertice = self.agregarVertice(destino)
        self.listaVertices[origen].agregarVecino(self.listaVertices[destino], costo)

    def obtenerVertices(self):
        return self.listaVertices.keys()

    def __iter__(self):
        return iter(self.listaVertices.values())
    
    def __len__(self):
        return len(self.numVertices)
