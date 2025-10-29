from modules.grafo import Grafo
from modules.algoritmo_prim import prim, distanciaTotal

#funcion para leer el archivo de aldeas:
def leer_aldeas(ruta="data/aldeas.txt"):
    ad={} #lista de adyacencias del grafo, aldeas conectadas entre si
    nodos=set()
    with open(ruta, "r") as archi:
        for linea in archi:
            linea=linea.strip()
            if not linea:
                continue
            partes=[p.strip() for p in linea.split(",") if p.strip() != '']

            #caso 1: solo nombre de aldea sin conexiones
            if len(partes)==1:
                nodo=partes[0]
                nodos.add(nodo)
                if nodo not in ad:
                    ad[nodo]=[]
                continue

            #caso 2: aldea con conexiones arista(origen, destino [, distancia])
            origen=partes[0]
            destino=partes[1]
            nodos.add(origen)
            nodos.add(destino)

            if origen not in ad:
                ad[origen]=[]
            if destino not in ad:
                ad[destino]=[]


            if len(partes)>=3:
                s=partes[2].replace(',','.')
                try:
                    distancia=int(s)
                except ValueError:
                    try:
                        distancia=int(round(float(s)))
                    except ValueError:
                            raise ValueError(f"La distancia no valida en la linea: {linea}")
            else:
                distancia= 0 #distancia por defecto si no se especifica 

            #grafo no dirigido agrego las aristas en ambos sentidos y evito duplicados
            if (destino, distancia) not in ad[origen]:
                ad[origen].append((destino, distancia))
            if (origen, distancia) not in ad[destino]:
                ad[destino].append((origen, distancia))
    for n in nodos:
        if n not in ad:
            ad[n]=[]
    return ad, nodos

#funcion para crear el grafo:
def crear_grafo(ad):
    g=Grafo()
    #crear vertices
    for v in ad.keys():
        if g.obtenerVertice (v) is None:
            g.agregarVertice(v) 
    #crear aristas
    for origen, vecinos in ad.items():
        for destino, distancia in vecinos:
            if origen== '' or destino=='':
                continue
            g.agregarArista(origen, destino, distancia)
    return g






