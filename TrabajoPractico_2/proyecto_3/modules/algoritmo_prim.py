import sys
from modules.cola_prioridad import ColaPrioridad
from modules.grafo import Grafo


def prim(G: Grafo,inicio):
    cp = ColaPrioridad()
    for v in G:
        v.asignar_distancia(sys.maxsize) #el maxsize hace que sea hasta el infinito la distancia entre as aldeas
        v.asignar_vecino_predecesor(None)
    inicio.asignar_distancia(0)
    cp.construirMonticulo([(v.obtener_distancia(),v) for v in G]) #se crea la cp con las distancias de cada vertice, es una tupla
    
    while not cp.estaVacia():
        verticeActual = cp.eliminarMin()[1] #al verticeActual se le asigan el minimo de la cp, guarda el indice por eso [1]
        for verticeSiguiente in verticeActual.obtener_vecinos(): #recorre las conexiones del verticeActual
            nuevoCosto = verticeActual.obtener_ponderacion(verticeSiguiente) #ponderacion entre el actual y el siguiente
            if verticeSiguiente in cp and nuevoCosto < verticeSiguiente.obtener_distancia():
                #relajacion del algoritmo de prim y algortimo de dijkstra
                verticeSiguiente.asignar_vecino_predecesor(verticeActual) # se actualiza el predecesor que es el actual
                verticeSiguiente.asignar_distancia(nuevoCosto) #se ajusta la distancia del verticeSiguiente
                cp.decrementar_clave(verticeSiguiente, nuevoCosto) #se decrementa la clave del siguiente vertice en la cp
                #hay que reconstruir para eso nos fijamos en los predecesores y calcular el costo minimo que es la suma de las distancias


if __name__=='__main__':
    listaMonticulo = [('a', 1),('b', 5),('c', 6)]
    
    grafo = Grafo ()
    grafo.agregarVertice('a')
    grafo.agregarVertice('b')
    grafo.agregarVertice('c')
    grafo.agregarArista('a', 'b', 2)
    grafo.agregarArista("b", "c", 5)
    grafo.agregarArista('a', 'c', 3)
    inicio = 'a'
    prim(grafo, inicio)