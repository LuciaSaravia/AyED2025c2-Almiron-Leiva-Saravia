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
        self.conectadoA[vecino] = distancia

    def __str__(self):
        return str(self.id) 

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
            self.listaVertices[nombre_Aldea] = nuevoVertice #el diccionario listaVertices su clave es el nombre de la aldea y su valor es el vertice de tipo Vertice
            return nuevoVertice
        return self.listaVertices[nombre_Aldea]

    def obtenerVertice(self,nombre_aldea):
        if nombre_aldea in self.listaVertices:
            return self.listaVertices[nombre_aldea] # devuelve el vertice que corresponde a esa clave
        else:
            return None

    def __contains__(self,n):
        return n in self.listaVertices

    def agregarArista(self, origen, destino, costo = 0):
        if origen not in self.listaVertices:
            self.agregarVertice(origen)
        if destino not in self.listaVertices:
            self.agregarVertice(destino)
        self.listaVertices[origen].agregarVecino(self.listaVertices[destino], costo) #conecta el origen con el destino
        

    def obtenerVertices(self):
        return self.listaVertices.keys() #devuelve el nombre de los vertices

    def __iter__(self):
        return iter(self.listaVertices.values())
    
    def __len__(self):
        return len(self.listaVertices)
