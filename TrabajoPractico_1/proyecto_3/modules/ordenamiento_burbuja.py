from random import randint

def ord_burbuja(lista):
    for num_siguiente in range(len(lista)-1, 0, -1):
        for i in range(num_siguiente):
            if lista[i] > lista[i+1]:
                temp = lista [i]
                lista[i] = lista[i+1]
                lista[i+1] = temp
    return lista

if __name__=='__main__':
    valores = []
    for i in range(500):
        valor = randint(10000, 50000)
        valores.append(valor)
    lista_ord_sorted = sorted(valores)
    lista_ordenada= ord_burbuja(valores)
    #Para comprobar que el algoritmos de ordenamiento burbuja funcione utilizamos la funcion sorted y comparamos elemento por elemento de ambas listas ordenadas
    comprobar = 0
    for i in range(500):
        if lista_ord_sorted[i] == lista_ordenada[i]:
            comprobar+=1
    print(comprobar)
    # print(f'lista ordenada: {lista_ordenada}')