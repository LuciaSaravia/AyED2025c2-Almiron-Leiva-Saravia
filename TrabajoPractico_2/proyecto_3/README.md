# 🐍Proyecto 3 - "Palomas Mensajeras"
En este proyecto se nos solicitó hallar la manera más eficiente (la menor suma total de distancias) de llevar un mensaje desde la aldea "Peligros" hasta el resto de las aldea, de manera tal que cada una de ellas reciba el mensaje solo una vez y puedan enviar réplicas a aldeas vecinas. A su vez, se nos pidió exponer la menor suma de todas las distancias recorridas por todas las palomas enviadas desde cada palomar, así como, exhibir el nombre de las aldeas en orden alfabético, y por último, indicar de qué vecina debería recibir la noticia, y a qué vecinas debería enviar réplicas.


## 🏗Arquitectura General
Utilizamos la estructura "grafo" que se trata de un árbol de expasión mínima, con raíz en la aldea "Peligros". Para esto, creamos las clases "Vertice" y "Grafo" que presentan diferentes funciones, tales como: agregarVecinos, obtenerVecinos, obtenerPonderación, agregarVertice, obtenerVertices, entre otras. Esto nos permitió implementar el algoritmo "prim", el cual nos ayudo para visualizar el recorrido que hicieron las palomas desde la aldea de origen hasta las demás aldeas, teniendo en cuenta la ponderación que hay entre ellas. Asimismo, implementamos las funciones distanciaTotal y recorridoMensajes para obtener la disticia total que realizaron las palomas desde "Peligros", así como también, el orden en el que lo hicieron.


## 🙎‍♀️🙎‍♂️Autores

- Almirón Spahn, Maria Paz
- Leiva, Giuliana
- Saravia, Lucia

