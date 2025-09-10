from random import randint

def obtener_digito(numero, posicion_digito, base = 10):

    return (numero // (base ** posicion_digito)) % base

def ordenamiento_radix(lista):
    max_num = max(lista)
    exp = 1  
    lista_aux = [[] for _ in range(10)]  
    posi = 0  
    while max_num // exp > 0:
        for num in lista:
            digit = obtener_digito(num, posi)  
            lista_aux[digit].append(num)

        sig_pos = 0 
        for sublist in lista_aux:
            for num in sublist:
                lista[sig_pos] = num  
                sig_pos += 1    
                
        lista_aux = [[] for _ in range(10)]
        exp *= 10
        posi += 1
    return lista

if __name__=="__main__":
    valores = []
    for i in range(500):
            valor = randint(10000, 50000)
            valores.append(valor)
    print(f"Lista orginal: {valores}")
    lista_ordenada = ordenamiento_radix(valores)
    print("\n")
    print(f"Lista ordenanda: {lista_ordenada}")
    
    lista_ord_sorted = sorted(valores)
    #Para comprobar que el algoritmo de ordenamiento radixsort funciona utilizamos la funcion sorted (la cual ya esta incorporada en Python) y luego comparamos elemento a elemento
    comprobar = 0
    for i in range(500):
        if lista_ord_sorted[i] == lista_ordenada[i]:
            comprobar+=1
        
    print(comprobar)