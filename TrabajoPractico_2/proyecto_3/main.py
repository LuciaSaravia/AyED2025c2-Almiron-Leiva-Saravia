def leer_aldeas(ruta="data/aldeas.txt"):
    ad={} #lista de adyacencias del grafo, aldeas conectadas entre si
    nodos=set()
    with open(ruta, "r") as archi:
        for linea in archi:
            linea=linea.strip()
            if not linea:
                continue
            partes=[p.strip() for p in linea.split(",") if p.strip() != '']

            #caso 1: hay una sola aldea en la linea
            if len(partes)==1:
                nodos.add(partes[0])
                if partes[0] not in ad:
                    ad[partes[0]]=[]
            elif len(partes)>=2:
                origen=partes[0]
                destino=partes[1]


                if len(partes)>=3:
                    s=partes[2].replace(" ,",".")
                    try:
                        distancia=int(s)
                    except ValueError:
                        try:
                            distancia=int(round(float(s)))
                        except ValueError:
                            raise ValueError(f"La distancia no valida en la linea: {linea}")
                else:
                    distancia= 0 #distancia por defecto si no se especifica 
                    #agr}ego los nodos
                    nodos.add(origen)
                    nodos.add(destino)
                    #listas d}e adyacencias
                    if origen not in ad:
                        ad[origen]=[]
                    if destino not in ad:
                        ad[destino]=[]
                    #grafo no dirigido agrego las aristas en ambos sentidos y }evito duplicados
                    if (destino, distancia) not in ad[origen]:
                        ad[origen].append((destino, distancia))
                    if (origen, distancia) not in ad[destino]:
                        ad[destino].append((origen, distancia))
            else:
                continue
    for n in nodos:
        if n not in ad:
            ad[n]=[]
    return ad, nodos






