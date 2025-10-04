
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
          elif self.lista[valor] < self.lista[(valor //2) + 1]:
             tmp = self.lista[(valor//2)+1]
             self.lista[(valor//2)+1] = self.lista[valor]
             self.lista[valor] = tmp
          valor = valor // 2

    def insertar(self,nuevo_valor):
      self.lista.append(nuevo_valor)
      self.tamanoActual = self.tamanoActual + 1
      self.infiltArriba(self.tamanoActual)

    def infiltAbajo(self,i):
          while (i * 2) <= self.tamanoActual:
              hm = self.hijoMin(i)
              if self.lista[i] > self.lista[hm]:
                  tmp = self.lista[i]
                  self.lista[i] = self.lista[hm]
                  self.lista[hm] = tmp
              i = hm

    def hijoMin(self,i):
          if i * 2 + 1 > self.tamanoActual:
              return i * 2
          else:
              if self.lista[i*2] < self.lista[i*2+1]:
                  return i * 2
              else:
                  return i * 2 + 1

    def eliminarMin(self):
      '''Devuelve la raiz del monticulo y selecciona una nueva raiz'''
      valorSacado = self.lista[1]
      self.lista[1] = self.lista[self.tamanoActual]
      self.tamanoActual = self.tamanoActual - 1
      self.lista.pop()
      self.infiltAbajo(1)
      return valorSacado

       
    
if __name__ == '__main__':
   lista= [23, 4, 6, 19, 32, 5, 7, 17, 9]
   monticulo= MonticuloMin()
   monticulo.insertar(8)
   monticulo.insertar(13)
   monticulo.insertar(1)
   raiz = monticulo.eliminarMin() 
   print (raiz)
   print(monticulo.lista) 

