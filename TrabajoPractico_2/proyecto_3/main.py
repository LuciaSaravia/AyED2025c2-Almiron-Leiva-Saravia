from modules.grafo import Grafo
from modules.algoritmo_prim import prim, distanciaTotal, recorridoMensajes

#funcion para leer el archivo de aldeas:
def leer_aldeas(ruta):
    grafo = Grafo()
    with open(ruta, "r") as archi:
        for linea in archi:
            linea=linea.strip()
            if not linea:
                continue
            partes=[p.strip() for p in linea.split(",") if p.strip() != '']
            if grafo.obtenerVertice(partes[0]) is None:
                grafo.agregarVertice(partes[0])

            grafo.agregarArista(partes[0], partes[1], int(partes[2]))
    return grafo

#implementacion

grafo = leer_aldeas("data/aldeas.txt")
v_inicio = grafo.obtenerVertice('Peligros')
prim(grafo, v_inicio)
aldeas_ord = sorted(grafo.obtenerVertices())
vertices_p_s = recorridoMensajes(grafo)

print("\n --Resultados del algortimo--")
print("\n --Listas de Aldeas--")
for aldea in aldeas_ord:
    print(aldea)
print(' ')
print('\n Recorrido del mensaje en la aldea: ')
for vertice in vertices_p_s:
    print(f'Aldea: {vertice[0]} ')
    if not vertice[1]:
        print(f'Aldea origen')
    else:   
        print(f'Aldea predecesora: {vertice[1]} ')
    if not vertice[2]:
        print('No tiene sucesores')
    else:
        print(f'Aldeas sucesoras {vertice[2]}')
    print('-'*40)
    print('  '*40)
print(f'\n la suma de todas las palomas desde cada palomar es de {distanciaTotal(grafo)}')