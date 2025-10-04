# 🐍Nombre del proyecto sala de emergencia 

En este proyecto se nos pidio simular una sala de emergencia en donde nos llegaban pacientes con distintos niveles de riesgo, y en caso de que 2 pacientes tengan el mismo nivel de riesgo deberiamos aplicar un segundo criterio para ver a quien atender primero.

---
## 🏗Arquitectura General

La catedra nos proporciono la simulacion de sala de emergencia, por lo que usamos la estrucutura Monticulo de minimos para almacenar a los pacientes a medida que entraban a la sala de mayor a menor nivel de riesgo (1 a 3). Asimismo implementamos una cola de prioridad para ver el orden en que se tenian que atender los pacientes, creamos el método especial __lt__ que nos sirvio para comparar en el Monticulo los niveles de riesgo y si estos coincidian utilizar como segundo criterio el orden de llegada que se asigna en la simulacion cuando llega un nuevo paciente a la sala.

---
## 🙎‍♀️🙎‍♂️Autores

- Almirón, Maria Paz
- Leiva, Giuliana
- Saravia, Lucia

---