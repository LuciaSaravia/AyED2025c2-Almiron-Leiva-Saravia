import sys
from modules.cola_prioridad import ColaPrioridad
from modules.grafo import Grafo


def prim(G: Grafo,inicio):
    cp = ColaPrioridad()
    print(f'Iniciando')
    for v in G:
        v.distancia = sys.maxsize #el maxsize hace que sea hasta el infinito la distancia entre as aldeas
        v.predecesor = None
    inicio.distancia = 0
    distancias = [(v.distancia, v) for v in G] 
    cp.construirMonticulo(distancias)
    #se crea la cp con las distancias de cada vertice, es una tupla

    while not cp.estaVacia():
        verticeActual = cp.eliminarMin()[1] #al verticeActual se le asigan el minimo de la cp, guarda el indice por eso [1
        for verticeSiguiente in verticeActual.obtenerVecinos(): #recorre las conexiones del verticeActual
            nuevoCosto = verticeActual.obtenerPonderacion(verticeSiguiente) #ponderacion entre el actual y el siguiente
            print(f'evaluando vecinos con costo {nuevoCosto}')
            if verticeSiguiente in cp and nuevoCosto < verticeSiguiente.distancia:
                #relajacion del algoritmo de prim y algortimo de dijkstra
                verticeSiguiente.predecesor = verticeActual # se actualiza el predecesor que es el actual
                verticeSiguiente.distancia = nuevoCosto #se ajusta la distancia del verticeSiguiente
                cp.decrementarClave(verticeSiguiente, nuevoCosto) #se decrementa la clave del siguiente vertice en la cp
                print(f"    Actualizado: {verticeActual.id} -> {verticeSiguiente.id} con costo {nuevoCosto}")
                #hay que reconstruir para eso nos fijamos en los predecesores y calcular el costo minimo que es la suma de las distancias

def distanciaTotal(grafo: Grafo): # Suma las distancias del árbol de expansión mínima
    total = 0
    for v in grafo:
        if v.predecesor is not None:
            total += v.distancia
    return total

def recorridoMensajes(grafo: Grafo):
    sucesores = []
    for v in grafo:
        predecesor = v.predecesor
        for p_sucesor in grafo:
            if p_sucesor.predecesor == v:
                sucesores.append(p_sucesor.id)

    #ver como mostrar para cada vertice
if __name__=='__main__':
    g = Grafo ()
    #ejemplo con numeros
    g.agregarArista(3,5,1.0)
    g.agregarArista(3,7,6.0)
    g.agregarArista(5,7,2.0)
    inicio=g.obtenerVertice(3)
    prim(g, inicio)
    print(f"Distancia total: {distanciaTotal(g)}")
    #ejemplo con letras y numeros
    gl= Grafo ()
    gl.agregarVertice('a')
    gl.agregarVertice('b')
    gl.agregarVertice('c')
    gl.agregarArista('a', 'b', 2)
    gl.agregarArista("b", "c", 5)
    gl.agregarArista('a', 'c', 3)

    prim(gl, gl.obtenerVertice('a'))
    print(distanciaTotal(gl))