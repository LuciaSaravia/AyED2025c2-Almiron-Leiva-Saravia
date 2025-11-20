
#Monticulo de minimo: estructura de datos en forma de arbol binario completo donde el valor de cada nodo es menor o igual que el de sus hijos. El elemento mínimo de todo el montículo siempre se encuentra en la raíz. Permite insertar y eliminar el mínimo en un tiempo muy eficiente, generalmente O(log n)
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

    def infiltArriba(self, valor): #se usa para reordenar el monticulo despues de insertar un nuevo valor, se va intercambiando el valor con su padre (INTERCAMBIO HACIA ARRIBA) hasta que quede en la posicion correcta 
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

    def infiltAbajo(self,i): #es para reordenar el monticulo despues de eliminar la raiz, se va intercambiando el valor con su hijo menor (INTERCAMBIO HACIA ABAJO) hasta que quede en la posicion correcta
          while (i * 2) <= self.tamanoActual:
              hm = self.hijoMin(i)
              if self.lista[i] > self.lista[hm]:
                  tmp = self.lista[i]
                  self.lista[i] = self.lista[hm]
                  self.lista[hm] = tmp
              i = hm

    def hijoMin(self,i): #encuentra y devuelve el hijo menor de un nodo
          if i * 2 + 1 > self.tamanoActual:
              return i * 2
          else:
              if self.lista[i*2] < self.lista[i*2+1]:
                  return i * 2
              else:
                  return i * 2 + 1

    def eliminarMin(self): #se usa para eliminar el minimo (raiz) del monticulo, para guarda la raiz, se elimina y se reemplaza por el ultimo elemento del monticulo para "llenar el hueco". Despues se reordena el monticulo (infiltrar hacia abajo)
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

