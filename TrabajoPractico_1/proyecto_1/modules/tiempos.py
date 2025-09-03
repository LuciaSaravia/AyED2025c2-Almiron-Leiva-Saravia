from modules.ListaDobleEnlazada import ListaDobleEnlazada
from matplotlib import pyplot as plt
import time
from random import randint

def medir_tiempo_len(tamanios):
    tiempos_len = []
    for n in tamanios:
        lista = ListaDobleEnlazada()
        for i in range(n):
            lista.agregar_al_final(randint(1, 1000))
        inicio = time.perf_counter()
        lista.__len__()
        fin = time.perf_counter()
        tiempos_len.append(fin - inicio)
    return tiempos_len
    
def medir_tiempo_copiar(tamanios):
    tiempos_copiar = []
    for n in tamanios:
        lista = ListaDobleEnlazada()
        for i in range(n):
            lista.agregar_al_final(randint(1, 1000))
        inicio = time.perf_counter()
        lista.copiar()
        fin = time.perf_counter()
        tiempos_copiar.append(fin - inicio)
    return tiempos_copiar

def medir_tiempo_invertir(tamanios):
    tiempos_invertir = []
    
    for n in tamanios:
        lista = ListaDobleEnlazada()
        for i in range(n):
            lista.agregar_al_final(randint(1, 1000))
        inicio = time.perf_counter()
        lista.invertir()
        fin = time.perf_counter()
        tiempos_invertir.append(fin - inicio)
    return tiempos_invertir



#Graficacion
tamanios = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
tiempos_len = medir_tiempo_len(tamanios)
tiempos_copiar = medir_tiempo_copiar(tamanios)
tiiempos_invertir = medir_tiempo_invertir(tamanios)
plt.figure(figsize=(10, 6))
plt.plot(tamanios, tiempos_len, marker='o', label='funcion len')
plt.plot(tamanios, tiempos_copiar, marker= 'o', label ='funcion copiar')
plt.plot(tamanios, tiiempos_invertir, marker = 'o', label = 'funcion invertir')
plt.xlabel('Tamaño de la lista')
plt.ylabel('Tiempo (segundos)')
plt.title('N (cantidad de elementos) vs tiempo de ejecución métodos: len, copiar e invertir')
plt.legend() # para mostrar el nombre del método de ordenamiento. Es el "label" del metodo plot
plt.grid() # cuadriculado
plt.show()