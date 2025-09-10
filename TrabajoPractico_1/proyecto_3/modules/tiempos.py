from modules.ordenamiento_burbuja import ord_burbuja
from modules.ordenamiento_quicksort import quickSort
from modules.ordenamiento_radixsort import ordenamiento_radix
from matplotlib import pyplot as plt
import time
from random import randint

def medir_tiempo_ord_burbuja(tamanios):
    tiempos_burbuja = []
    lista = []
    for i in tamanios:
        lista = [randint(1, 1000) for _ in range(i)]
        inicio = time.perf_counter()
        ord_burbuja(lista)
        fin = time.perf_counter()
        tiempos_burbuja.append(fin - inicio)
    return tiempos_burbuja
    
def medir_tiempo_quickSort(tamanios):
    tiempos_quick= []
    lista = []
    for i in tamanios:
        lista=[randint(1, 1000) for _ in range(i)]
        inicio = time.perf_counter()
        quickSort(lista)
        fin = time.perf_counter()
        tiempos_quick.append(fin - inicio)
    return tiempos_quick

def medir_tiempo_randixsort(tamanios):
    tiempos_randix = []
    lista = []
    for i in tamanios:
        lista = [randint(1, 1000) for _ in range(i)]
        inicio = time.perf_counter()
        ordenamiento_radix(lista)
        fin = time.perf_counter()
        tiempos_randix.append(fin - inicio)
    return tiempos_randix



#Graficacion
tamanios = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
tiempos_burbuja = medir_tiempo_ord_burbuja(tamanios)
tiempos_quick = medir_tiempo_quickSort(tamanios)
tiempos_randix = medir_tiempo_randixsort(tamanios)
plt.figure(figsize=(10, 6))
plt.plot(tamanios, tiempos_burbuja, marker='o', label='ordenamiento burbuja')
plt.plot(tamanios, tiempos_quick, marker= 'o', label ='ordenamiento quickSort')
plt.plot(tamanios, tiempos_randix, marker = 'o', label = 'ordenamiento radix')
plt.xlabel('Tamaño de la lista')
plt.ylabel('Tiempo (segundos)')
plt.title('N (cantidad de elementos) vs tiempo de ordenamientos: burbuja, quicksort e radix')
plt.legend() # para mostrar el nombre del método de ordenamiento. Es el "label" del metodo plot
plt.grid() # cuadriculado
plt.show()