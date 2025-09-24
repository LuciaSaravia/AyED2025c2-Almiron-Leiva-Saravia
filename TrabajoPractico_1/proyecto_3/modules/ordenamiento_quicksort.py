from random import randint

def quickSort(lista):
   pequenio_ayudante(lista,0,len(lista)-1)
   return lista

def pequenio_ayudante(lista,primero,ultimo):
   if primero<ultimo:

       punto_separacion = particion(lista,primero,ultimo)

       pequenio_ayudante(lista,primero,punto_separacion-1)
       pequenio_ayudante(lista,punto_separacion+1,ultimo)

def particion(lista,primero,ultimo):
   valor_pivote = lista[primero]
   marca_izq = primero+1
   marca_der = ultimo

   done = False
   while not done:

       while marca_izq <= marca_der and lista[marca_izq] <= valor_pivote:
           marca_izq = marca_izq + 1

       while lista[marca_der] >= valor_pivote and marca_der >= marca_izq:
           marca_der = marca_der -1

       if marca_der < marca_izq:
           done = True
       else:
           temp = lista[marca_izq]
           lista[marca_izq] = lista[marca_der]
           lista[marca_der] = temp

   temp = lista[primero]
   lista[primero] = lista[marca_der]
   lista[marca_der] = temp
   return marca_der

if __name__=='__main__':
    valores = []
    for i in range(500):
        valor = randint(10000, 50000)
        valores.append(valor)
    lista_ord_sorted = sorted(valores)
    lista_ordenada= quickSort(valores)
    comprobar = 0
    for i in range(500):
        if lista_ord_sorted[i] == lista_ordenada[i]:
            comprobar+=1
    print (comprobar)
    #print(f"La lista ordenada: {orden}")
    
    # print(f'lista ordenada: {lista_ordenada}')

