from abc import ABC, abstractmethod
class NodoArbol:
    def __init__(self,clave,valor,izquierdo=None,derecho=None,
                                       padre=None):
        self.__clave = clave
        self.__cargaUtil = valor
        self.__hijoIzquierdo = izquierdo
        self.__hijoDerecho = derecho
        self.__padre = padre
        self.__factorEquilibrio = 0

    @property
    def clave(self):
        return self.__clave
    
    @property
    def cargaUtil(self):
        return self.__cargaUtil
    
    @property
    def hijoIzquierdo(self):
        return self.__hijoIzquierdo
    
    @hijoIzquierdo.setter
    def hijoIzquierdo(self, nuevo):
        self.__hijoIzquierdo = nuevo

    @property
    def hijoDerecho(self):
        return self.__hijoDerecho
    
    @hijoDerecho.setter
    def hijoDerecho(self, nuevo):
        self.__hijoDerecho = nuevo

    @property
    def padre(self):
        return self.__padre
    
    @ padre.setter
    def padre(self, nuevo_padre):
        self.__padre = nuevo_padre

    @property
    def factorEquilibrio(self):
        return self.__factorEquilibrio
    
    @factorEquilibrio.setter
    def factorEquilibrio(self, nuevo_factor):
        self.__factorEquilibrio = nuevo_factor
    
    def tieneHijoIzquierdo(self):
        return self.hijoIzquierdo

    def tieneHijoDerecho(self):
        return self.hijoDerecho

    def esHijoIzquierdo(self):
        return self.padre and self.padre.hijoIzquierdo == self

    def esHijoDerecho(self):
        return self.padre and self.padre.hijoDerecho == self

    def esRaiz(self):
        return not self.padre

    def esHoja(self):
        return not (self.hijoDerecho or self.hijoIzquierdo)

    def tieneAlgunHijo(self):
        return self.hijoDerecho or self.hijoIzquierdo

    def tieneAmbosHijos(self):
        return self.hijoDerecho and self.hijoIzquierdo

    def reemplazarDatoDeNodo(self,clave,valor,hizq,hder):
        self.clave = clave
        self.cargaUtil = valor
        self.hijoIzquierdo = hizq
        self.hijoDerecho = hder
        if self.tieneHijoIzquierdo():
            self.hijoIzquierdo.padre = self
        if self.tieneHijoDerecho():
            self.hijoDerecho.padre = self
        

class ArbolBinarioBusqueda(ABC):
    @abstractmethod
    def longitud(self):
        raise NotImplementedError
    
    @abstractmethod
    def __len__(self):
        raise NotImplementedError
    
    @abstractmethod
    def __iter__(self):
        raise NotImplementedError

    @abstractmethod
    def _agregar(self, clave, valor, nodoActual):
        raise NotImplementedError
