import sys
from modules.cola_prioridad import ColaPrioridad
from modules.grafo import Grafo


def prim(G: Grafo,inicio):
    cp = ColaPrioridad()
    for v in G:
        v.distancia = sys.maxsize #el maxsize hace que sea hasta el infinito la distancia entre as aldeas
        v.predecesor = None
    inicio.distancia = 0
    distancias = [(v.distancia, v) for v in G] 
    cp.construirMonticulo(distancias)
    #se crea la cp con las distancias de cada vertice, es una tupla

    while not cp.estaVacia():
        verticeActual = cp.eliminarMin()[1] #al verticeActual se le asigan el minimo de la cp, guarda el indice por eso [1]
        for verticeSiguiente in verticeActual.obtenerVecinos(): #recorre las conexiones del verticeActual
            nuevoCosto = verticeActual.obtenerPonderacion(verticeSiguiente) #ponderacion entre el actual y el siguiente
            
            if verticeSiguiente in cp and nuevoCosto < verticeSiguiente.distancia:
                #relajacion del algoritmo de prim y algortimo de dijkstra
                verticeSiguiente.predecesor = verticeActual # se actualiza el predecesor que es el actual
                verticeSiguiente.distancia = nuevoCosto #se ajusta la distancia del verticeSiguiente
                cp.decrementarClave(verticeSiguiente, nuevoCosto) #se decrementa la clave del siguiente vertice en la cp
                #hay que reconstruir para eso nos fijamos en los predecesores y calcular el costo minimo que es la suma de las distancias

def distanciaTotal(grafo: Grafo): 
    '''Suma las distancias del árbol de expansión mínima'''
    total = 0
    for v in grafo: #recorre los vertices del grafo
        if v.predecesor is not None:
            total += v.distancia #se suma la distancia
    return total

def recorridoMensajes(grafo: Grafo):
    '''Devuelve una lista de lista donde se almacena el nombre de la aldea, el predecesor y los sucesores'''
    vertices = []
    for v in grafo:
        sucesores = []
        predecesor = v.predecesor #guardamos el predecesor del vertice
        for posible_s in v.obtenerVecinos(): #de los vecinos del vertice buscamos los posibles sucesores
            if posible_s.predecesor == v: #para los vecinos comparamos que su predecesor sea el vertice, si no es, no se agrega a lista de sucesores (recibe mensaje de otro vertice)
                sucesores.append(posible_s.id)
        vertices.append([v.id ,predecesor, sucesores])
    return vertices

if __name__=='__main__':
    g = Grafo ()
    #ejemplo con numeros
    g.agregarArista(3,5,1.0)
    g.agregarArista(3,7,6.0)
    g.agregarArista(5,7,2.0)
    inicio=g.obtenerVertice(3)
    prim(g, inicio)
    print(f"Distancia total: {distanciaTotal(g)}")
    # ejemplo con letras y numeros
    gl= Grafo ()
    gl.agregarVertice('a')
    gl.agregarVertice('b')
    gl.agregarVertice('c')
    gl.agregarArista('a', 'b', 2)
    gl.agregarArista("b", "c", 5)
    gl.agregarArista('a', 'c', 3)

    prim(gl, gl.obtenerVertice('a'))
    print(distanciaTotal(gl))
    vertices = recorridoMensajes(g)
    for vertice in vertices:
        print (f'Aldea: {vertice[0]}, Predecesor : {vertice[1]}, Sucesores: {vertice[2]}')