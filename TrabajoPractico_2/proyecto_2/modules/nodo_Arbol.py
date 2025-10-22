
class NodoArbol:
    def __init__(self,clave,valor,izquierdo=None,derecho=None,
                                       padre=None):
        self.__clave = clave #fecha
        self.__valor = valor #temperatura
        self.__hijoIzquierdo = izquierdo
        self.__hijoDerecho = derecho
        self.__padre = padre
        self.__factorEquilibrio = 0

    @property
    def clave(self):
        return self.__clave
    
    @property
    def valor(self):
        return self.__valor
    
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
    
    @clave.setter
    def clave(self, nueva_clave):
        self.__clave = nueva_clave
    
    @valor.setter
    def valor(self, nuevo_valor):
        self.__valor = nuevo_valor
    
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
        self.valor = valor
        self.hijoIzquierdo = hizq
        self.hijoDerecho = hder
        if self.tieneHijoIzquierdo():
            self.hijoIzquierdo.padre = self
        if self.tieneHijoDerecho():
            self.hijoDerecho.padre = self

    def encontrarSucesor(self):
        return self.hijoDerecho.encontrarMin()
        return suc
    
    def encontrarMin(self):
        actual = self
        while actual.tieneHijoIzquierdo():
            actual = actual.hijoIzquierdo
        return actual
    
    def empalmar(self):
        if self.esHoja():
            if self.esHijoIzquierdo():
                self.padre.hijoIzquierdo = None
            else:
                self.padre.hijoDerecho = None
        elif self.tieneAlgunHijo():
            if self.tieneHijoIzquierdo():
                if self.esHijoIzquierdo():
                    self.padre.hijoIzquierdo = self.hijoIzquierdo
                else:
                    self.padre.hijoDerecho = self.hijoIzquierdo
                    self.hijoIzquierdo.padre = self.padre
            else:
                if self.esHijoIzquierdo():
                    self.padre.hijoIzquierdo = self.hijoDerecho
                else:
                    self.padre.hijoDerecho = self.hijoDerecho
                    self.hijoDerecho.padre = self.padre
    
    def __iter__(self):
        if self:
            if self.tieneHijoIzquierdo():
                    for elem in self.hijoIzquierdo:
                        yield elem
            yield self
            if self.tieneHijoDerecho():
                    for elem in self.hijoDerecho:
                        yield elem