import sys
from modules.cola_prioridad import ColaPrioridad
from modules.grafo import Grafo, Vertice


def prim(G: Grafo,inicio):
    cp = ColaPrioridad()
    print(f'Iniciando')
    for v in G:
        v.distancia = sys.maxsize #el maxsize hace que sea hasta el infinito la distancia entre as aldeas
        v.predecesor = None
    inicio.distancia = 0
    cp.construirMonticulo([(v.distancia,v) for v in G]) #se crea la cp con las distancias de cada vertice, es una tupla
    
    while not cp.estaVacia():
        verticeActual = cp.eliminarMin()[1] #al verticeActual se le asigan el minimo de la cp, guarda el indice por eso [1]
        print(f'Procesando vertices {verticeActual.obtener()}')
        for verticeSiguiente in verticeActual.obtener_vecinos(): #recorre las conexiones del verticeActual
            nuevoCosto = verticeActual.obtener_ponderacion(verticeSiguiente) #ponderacion entre el actual y el siguiente
            print(f'evaluando vecinos con costo {nuevoCosto}')
            if verticeSiguiente in cp and nuevoCosto < verticeSiguiente.distancia:
                #relajacion del algoritmo de prim y algortimo de dijkstra
                verticeSiguiente.predecesor = verticeActual # se actualiza el predecesor que es el actual
                verticeSiguiente.distancia = nuevoCosto #se ajusta la distancia del verticeSiguiente
                cp.decrementar_clave(verticeSiguiente, nuevoCosto) #se decrementa la clave del siguiente vertice en la cp
                print(f"    Actualizado: {verticeActual.obtenerId()} -> {verticeSiguiente.obtenerId()} con costo {nuevoCosto}")
                #hay que reconstruir para eso nos fijamos en los predecesores y calcular el costo minimo que es la suma de las distancias

def distanciatotal(grafo: Grafo): # Suma las distancias del árbol de expansión mínima
    total = 0
    for v in grafo:
        if v.predecesor is not None:
            total += v.distancia
    return total

if __name__=='__main__':
    listaMonticulo = [('a', 1),('b', 5),('c', 6)]
    inicio = Vertice ('a')
    g = Grafo ()
    # g.agregarArista(3,5,1)
    # g.agregarArista(5,3,1)
    # g.agregarArista(3,7,6)
    # g.agregarArista(7,3,6)

    # prim(g, g.obtenerVertice(3))
    # print("Árbol de expansión mínima:")
    # for v in g:
    #     if v.predecesor is not None:
    #         print(f"{v.predecesor.obtenerId()} - {v.obtenerId()} con costo {v.distancia}")

    # print(f"La distancia total es: {distanciatotal(g)}")
    # grafo.agregarVertice('a')
    # grafo.agregarVertice('b')
    # grafo.agregarVertice('c')
    # grafo.agregarArista('a', 'b', 2)
    # grafo.agregarArista("b", "c", 5)
    # grafo.agregarArista('a', 'c', 3)
    
    # prim(grafo, inicio)
    # print(distanciatotal(grafo))