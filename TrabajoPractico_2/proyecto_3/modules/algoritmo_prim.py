import sys
from modules.cola_prioridad import ColaPrioridad


def prim(G,inicio):
    cp = ColaPrioridad()
    for v in G:
        v.asignarDistancia(sys.maxsize)
        v.asignarVecinoPredecesor(None)
    inicio.asignarDistancia(0)
    cp.construirMonticulo([(v.obtenerDistancia(),v) for v in G])
    while not cp.estaVacia():
        verticeActual = cp.eliminarMin()
        for verticeSiguiente in verticeActual.obtenerVecinos():
            nuevoCosto = verticeActual.obtenerDistancia(verticeSiguiente)
            if verticeSiguiente in cp and nuevoCosto<verticeSiguiente.obtenerDistancia():
                verticeSiguiente.asignarVecinoPredecesor(verticeActual)
                verticeSiguiente.asignarDistancia(nuevoCosto)
                cp.decrementarClave(verticeSiguiente, nuevoCosto)