from modules.ListaDobleEnlazada import ListaDobleEnlazada
import time
from random import randint

def medir_tiempo_len(tamanio):
    tiempos_len = []
    for n in tamanio:
        lista = ListaDobleEnlazada()
        for i in range(n):
            lista.agregar_al_final(randint(1, 10000))
        inicio = time.perf_counter()
        len(lista)
        fin = time.perf_counter
        tiempos_len.append(inicio - fin)
        print(f"Tiempo de la funcion len para n={n}: {fin - inicio:.6f} segundos")
        return tiempos_len
    
def medir_tiempo_copiar(tamanio):
    tiempos_copiar = []
    for n in tamanio:
        lista = ListaDobleEnlazada()
        for i in range(n):
            lista.agregar_al_final(randint(1, 10000))
        inicio = time.perf_counter()
        lista.copiar()
        fin = time.perf_counter()
        tiempos_copiar.append(inicio - fin)
        print(f"Tiempo de la funcion copiar para n={n}: {fin - inicio:.6f} segundos")
        return tiempos_copiar

def medir_tiempo_invertir(tamanio):
    tiempos_invertir = []
    for n in tamanio:
        lista = ListaDobleEnlazada()
        for i in range(n):
            lista.agregar_al_final(randint(1, 10000))
        inicio = time.perf_counter()
        lista.invertir()
        fin = time.perf_counter()
        tiempos_invertir.append(inicio - fin)
        print(f"Tiempo de la funcion invertir para n={n}: {fin - inicio:.6f} segundos")
        return tiempos_invertir