# 🐍Temperatura-DB
En este problema se solicito crear una estructura eficiente para agregar temperaturas desde un archivo txt usando un Arbol AVL, debido a que permite mantener las claves ordenadas (fechas) y garantizar complejidad O (log n) para búsquedas, inserciones y borrados en el peor caso. A su vez, se crearon funciones para agregar, eliminar, recuperar y obtener rangos de dichas temperaturas.
## 🏗Arquitectura General
Para el Arbol AVL se implemento una clase AVL donde los atributos son raiz y tamaño. Además, tiene como principales funciones:
    -> agregar()
    -> _agregar() (tiene una llamada recursiva)
    -> actualizar_equilibrio()
    -> reequilibrar()
    -> rotar() (izquierda o derecha)
    -> obtener_rango()
Por otro lado se creo una clase NodoArbol que tiene como atributos clave (guarda la fecha), valor (guarda la temperatura),hijoIzquierdo, hijoDerecho, padre y factorEquilibrio, para acceder a ellos se utilizaron getters y setters. Asimimos tiene funciones como:
    -> tieneHijoIzquierdo()
    -> tieneHijoDerecho()
    -> esRaiz()
    -> tieneAlgunHijo()
    -> encontrarSucesor()
    -> encontrarMin()
Por ultimo, la clase Temperatura_DB tiene un objeto de la clase AVL y todos sus metodos dependen de los metodos del arbol AVL. Algunos metodos a destacar son:
    -> guardar_tempertura()
    -> devolver_temperatura()
    -> max_temp_rango()
    -> temp_extremos_rangos()
    -> cantidad de muestras()

En el [main.py] se puede observar la implementación del guardado de temperaturas como la utilizacion de las funciones pedidas para Temperatura_DB
-
El informe completo está disponible en la carpeta [docs](./docs) del proyecto.

---
## 🙎‍♀️🙎‍♂️Autores

- Almirón, Maria Paz
- Leiva, Giuliana
- Saravia, Lucia


