class Vertice:
    def __init__(self, nombre_aldea: str):
        self.__id = nombre_aldea
        self.__distancia = 0.0
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
    
    @distancia.setter
    def distancia(self, nuevo_distancia):
        self.__distancia = nuevo_distancia
    
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

    def obtenerPonderacion(self,vecino): 
        return self.conectadoA[vecino]
   
    
class Grafo:
    def __init__(self):
        self.listaVertices = {}
        self.__numVertices = 0

    @property
    def numVertices(self):
        return self.__numVertices

    @numVertices.setter
    def numVertices(self, numVertices):
        self.__numVertices =+ numVertices

    def agregarVertice(self,nombre_Aldea):
        if nombre_Aldea not in self.listaVertices:
            self.__numVertices += 1
            nuevoVertice = Vertice(nombre_Aldea)
            self.listaVertices[nombre_Aldea] = nuevoVertice
            return nuevoVertice
        return self.listaVertices[nombre_Aldea]

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
        #tenemos que agregar la arista en ambos sentidos xq es un grafo no dirigido 
        self.listaVertices[origen].agregarVecino(self.listaVertices[destino], costo)
        # self.listaVertices[destino].agregarVecino(self.listaVertices[origen], costo) No se deberia guardar como vecino sino como predecesor

    def obtenerVertices(self):
        return self.listaVertices.keys()

    def __iter__(self):
        return iter(self.listaVertices.values())
    
    def __len__(self):
        return len(self.listaVertices)
