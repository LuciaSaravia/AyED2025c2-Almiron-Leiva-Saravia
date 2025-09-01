from matplotlib import pyplot as plt
from modules.tiempos import medir_tiempo_copiar, medir_tiempo_invertir, medir_tiempo_len

def graficar_tiempos_len():
    tamanios = [1, 10, 100, 200, 500, 700,1000]

    plt.figure(figsize=(10, 6))
    tiempos = medir_tiempo_len(tamanios)
    plt.plot(tamanios, tiempos, marker='o', label='funcion len')

    plt.xlabel('Tamaño de la lista')
    plt.ylabel('Tiempo (segundos)')
    plt.title('N (cantidad de elementos) vs tiempo de ejecucion metodo len')
    plt.legend() # para mostrar el nombre del método de ordenamiento. Es el "label" del metodo plot
    plt.grid() # cuadriculado
    plt.show()