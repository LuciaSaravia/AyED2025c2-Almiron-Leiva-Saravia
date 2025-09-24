
class MonticuloMin:
    def __init__(self):
        self.__lista = [None]
        self.tamanoActual = 0 
    @property
    def lista(self):
       return self.__lista
    @lista.setter
    def lista(self, cambio):
       self.__lista = cambio


    def infiltArriba(self, valor):
        while valor // 2 > 0:
          if self.lista[valor] < self.lista[valor // 2]:
             tmp = self.lista[valor // 2]
             self.lista[valor // 2] = self.lista[valor]
             self.lista[valor] = tmp
          valor = valor // 2

    def insertar(self,nuevo_valor):
      self.lista.append(nuevo_valor)
      self.tamanoActual = self.tamanoActual + 1
      self.infiltArriba(self.tamanoActual)

    def infiltAbajo(self, valor):
      while (valor * 2) <= self.tamanoActual:
          h_min = self.hijoMin(valor)
          if self.lista[valor] > self.lista[h_min]:
              tmp = self.lista[valor]
              self.lista[valor] = self.lista[h_min]
              self.lista[h_min] = tmp
          valor = h_min

    def hijoMin(self, valor):
      if valor * 2 + 1 > self.tamanoActual:
          return valor * 2
      else:
          if self.lista[valor *2] < self.lista[valor *2+1]:
              return valor * 2
          else:
              return valor * 2 + 1

    def eliminarMin(self):
      valorSacado = self.lista[1]
      self.lista[1] = self.lista[self.tamanoActual]
      self.tamanoActual = self.tamanoActual - 1
      self.lista.pop()
      self.infiltAbajo(1)
      return valorSacado

    def construirMonticulo(self,unaLista):
      valor = len(unaLista) // 2
      self.tamanoActual = len(unaLista)
      self.lista = [None] + unaLista[:]
      while (valor > 0):
          self.infiltAbajo(valor)
          valor = valor - 1
    


if __name__ == '__main__':
   lista= [23, 4, 6, 19, 32, 5, 7, 17, 9]
   monticulo= MonticuloMin()
   monticulo.construirMonticulo(lista)
   monticulo.insertar(8)
   monticulo.insertar(13)
   monticulo.insertar(1)
   raiz = monticulo.eliminarMin() 
   print (raiz)
   print(monticulo.lista) 