from modules.monticulo_min import MonticuloMin

class ABB:
    def __init__(self):
        self.__raiz = None
        self.__tamano = 0

    @property
    def raiz (self):
        return self.__raiz
    @raiz.setter
    def raiz(self, raiz):
        self.__raiz = raiz
    @property
    def tamano(self):
        return self.__tamano
    @tamano.setter
    def tamano(self, tamano):
        self.__tamano = tamano

    def longitud(self):
        return self.tamano

    def __len__(self):
        return self.tamano

    def __iter__(self):
        return self.raiz.__iter__()
    
class TreeNode:
    def __init__(self,clave,valor,izquierda=None,derecha=None,
                                       padre=None):
        self.clave = clave
        self.carga_util = valor
        self.hijo_izquierdo = izquierda
        self.hijo_derecho= derecha
        self.padre = padre

    def tiene_hijo_izquierdo(self):
        return self.hijo_izquierdo

    def tiene_hijo_derecho(self):
        return self.hijo_derecho

    def es_hijo_izquierdo(self):
        return self.padre and self.padre.hijo_izquierdo == self

    def es_hijo_derecho(self):
        return self.padre and self.padre.hijo_derecho == self

    def raiz(self):
        return not self.padre

    def hoja(self):
        return not (self.hijo_derecho or self.hijo_izquierdo)

    def tiene_hijo(self):
        return self.hijo_derecho or self.hijo_izquierdo

    def tiene_2_hijos(self):
        return self.hijo_derecho and self.hijo_izquierdo

    def cambiar_nodo_por_info(self,clave,value,lc,rc):
        self.clave = clave
        self.payload = value
        self.hijo_izquierdo = lc
        self.hijo_derecho = rc
        if self.es_hijo_izquierdo():
            self.hijo_izquierdo.padre = self
        if self.es_hijo_derecho():
            self.hijo_derecho.padre = self

