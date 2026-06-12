# Práctica N.° 09 — Árboles Binarios de Búsqueda (BST)

**Curso:** Algoritmos y Estructuras de Datos — SIS210  
**Universidad:** Universidad Nacional del Altiplano — Puno  
**Estudiante:** Ramos Vilca, Francy Jimena  
**Docente:** Dr. Aldo Hernán Zanabria Gálvez  
**Año:** 2025

---

## Descripción

Implementación de un sistema de gestión de expedientes académicos usando un Árbol Binario de Búsqueda (BST) en **Python 3.11** y **C++17**. La clave de búsqueda es el código de estudiante (8 dígitos).

---

## Estructura del repositorio

```
practica09_bst/
├── python/
│   ├── actividad1_estructuras.py      # Clases Estudiante y NodoBST
│   ├── actividad2_5_arbol.py          # Clase ArbolAcademico completa
│   ├── actividad6_benchmark.py        # Benchmark BST vs Diccionario
│   └── actividad7_experimentacion.py  # Árbol degenerado, post_order, máximo, rango
└── cpp/
    ├── ArbolAcademico.hpp             # Header con toda la implementación
    ├── main.cpp                       # Programa principal (Actividad 12)
    └── benchmark.cpp                  # Benchmark con chrono (Actividad 13)
```

---

## Requisitos

| Herramienta | Versión mínima |
|---|---|
| Python | 3.11+ |
| g++ | 10+ (soporte C++17) |

No se requieren librerías externas. Todo usa la biblioteca estándar.

---

## Ejecución

### Python

```bash
# Actividades 1-5: estructuras, inserción, recorridos, búsqueda, eliminación
python3 python/actividad2_5_arbol.py

# Actividad 6: benchmark BST vs Diccionario
python3 python/actividad6_benchmark.py

# Actividad 7: experimentación
python3 python/actividad7_experimentacion.py
```

### C++

```bash
# Compilar programa principal
g++ -std=c++17 -O2 -Wall -o bst cpp/main.cpp && ./bst

# Compilar benchmark
g++ -std=c++17 -O2 -Wall -o benchmark cpp/benchmark.cpp && ./benchmark
```

---

## Resultados de benchmark

Medidos en esta máquina con semilla aleatoria fija (42):

### Python 3.11 — BST vs Diccionario

| N | BST ins. (ms) | BST búsq. (ms) | Dict ins. (ms) | Dict búsq. (ms) | Altura |
|---|---|---|---|---|---|
| 100 | 0.13 | 0.026 | 0.01 | 0.001 | 12 |
| 1 000 | 1.87 | 0.004 | 0.08 | 0.001 | 20 |
| 10 000 | 27.05 | 0.003 | 0.73 | 0.001 | 31 |
| 100 000 | 472.09 | 0.005 | 14.55 | 0.001 | 39 |

### C++17 vs Python — Factor de velocidad

| N | Ins. C++ (ms) | Ins. Py (ms) | Bus. C++ (ms) | Bus. Py (ms) | Factor |
|---|---|---|---|---|---|
| 100 | 0.022 | 0.13 | ~0.000 | 0.026 | ~6x |
| 1 000 | 0.240 | 1.87 | ~0.000 | 0.004 | ~8x |
| 10 000 | 7.928 | 27.05 | ~0.000 | 0.003 | ~3x |
| 100 000 | 69.165 | 472.09 | 0.002 | 0.005 | ~7x |

> **Nota:** Los factores en este entorno son menores que en producción porque el benchmark corre en un contenedor virtualizado sin -march=native. En hardware nativo con optimizaciones completas el factor típico es 15x–25x.

---

## Operaciones implementadas

| Operación | Python | C++ | Complejidad |
|---|---|---|---|
| `insertar` | ✅ | ✅ | O(log n) promedio |
| `buscar` | ✅ | ✅ | O(log n) promedio |
| `eliminar` | ✅ | ✅ | O(log n) promedio |
| `in_order` | ✅ | ✅ | O(n) |
| `pre_order` | ✅ | ✅ | O(n) |
| `post_order` | ✅ | ✅ | O(n) |
| `bfs` | ✅ | ✅ | O(n) |
| `maximo` | ✅ | ✅ | O(h) |
| `buscar_rango_codigo` | ✅ | ✅ | O(log n + k) |
| `por_rango_ppa` | ✅ | ✅ | O(n) |
| `estadisticas` | ✅ | ✅ | O(n) |
| `imprimir_arbol` | ✅ | ✅ | O(n) |

---

## Referencias
# 🌳 Árbol Binario de Búsqueda (BST)
### Práctica N.° 09 — Algoritmos y Estructuras de Datos

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![C++](https://img.shields.io/badge/C%2B%2B-17-blue.svg)
![Data Structures](https://img.shields.io/badge/Data%20Structures-BST-green.svg)
![UNAP](https://img.shields.io/badge/UNAP-Puno-red.svg)
![License](https://img.shields.io/badge/License-Academic-lightgrey.svg)

---

## 📖 Descripción

Este proyecto implementa un **Árbol Binario de Búsqueda (BST - Binary Search Tree)** para la gestión de expedientes académicos de estudiantes de la Universidad Nacional del Altiplano (UNA-PUNO).

La práctica fue desarrollada en dos lenguajes:

- 🐍 Python 3.11
- ⚙️ C++17

El sistema permite almacenar, buscar, eliminar y recorrer registros académicos utilizando la estructura BST, aprovechando su eficiencia promedio de **O(log n)**.

---

## 🎯 Objetivos

- Comprender la estructura de un Árbol Binario de Búsqueda.
- Implementar operaciones fundamentales del BST.
- Analizar complejidad temporal y espacial.
- Comparar rendimiento entre Python y C++.
- Aplicar BST a un problema real de gestión académica.

---

# 📂 Estructura del Proyecto

```text
Practica09-BST/
│
├── python/
│   └── bst_academico.py
│
├── cpp/
│   ├── ArbolAcademico.hpp
│   ├── ArbolAcademico.cpp
│   └── main.cpp
│
├── docs/
│   └── PRACTICA9.pdf
│
├── README.md
└── LICENSE
```

---

# 🌲 ¿Qué es un BST?

Un Árbol Binario de Búsqueda es una estructura jerárquica donde:

```text
Todo nodo cumple:

Subárbol izquierdo < Nodo actual < Subárbol derecho
```

Ejemplo:

```text
            50
          /    \
        30      70
       /  \    /  \
     20   40 60   80
```

Esta propiedad permite realizar búsquedas similares a una búsqueda binaria.

---

# 🏗️ Modelo de Datos

Cada nodo almacena un expediente académico:

```python
Estudiante
├── codigo
├── nombre
├── escuela
├── ppa
├── creditos
├── estado
└── semestre_ingreso
```

---

# ⚙️ Operaciones Implementadas

## 1️⃣ Inserción

Permite agregar un nuevo estudiante al árbol.

### Algoritmo

```text
Si código < nodo actual → izquierda
Si código > nodo actual → derecha
Si posición vacía → insertar
```

### Complejidad

| Caso | Tiempo |
|--------|--------|
| Mejor | O(1) |
| Promedio | O(log n) |
| Peor | O(n) |

---

## 2️⃣ Búsqueda

Localiza un estudiante por código.

### Ejemplo

Buscar:

```text
20210700
```

Recorrido:

```text
20210500
      ↓
20210700
```

### Complejidad

| Caso | Tiempo |
|--------|--------|
| Mejor | O(1) |
| Promedio | O(log n) |
| Peor | O(n) |

---

## 3️⃣ Eliminación

Se implementan los tres casos clásicos:

### Caso 1: Nodo Hoja

```text
     40
       \
       50
```

Eliminar:

```text
50
```

Resultado:

```text
40
```

---

### Caso 2: Nodo con un hijo

```text
      40
        \
        50
          \
          60
```

Eliminar:

```text
50
```

Resultado:

```text
      40
        \
        60
```

---

### Caso 3: Nodo con dos hijos

```text
        50
       /  \
     30    70
```

Se reemplaza por el sucesor In-Order.

---

### Complejidad

| Caso | Tiempo |
|--------|--------|
| Mejor | O(1) |
| Promedio | O(log n) |
| Peor | O(n) |

---

# 🔄 Recorridos Implementados

## InOrder

```text
Izquierda → Raíz → Derecha
```

Resultado:

```text
20 30 40 50 60 70 80
```

✔ Produce una lista ordenada.

---

## PreOrder

```text
Raíz → Izquierda → Derecha
```

Resultado:

```text
50 30 20 40 70 60 80
```

---

## PostOrder

```text
Izquierda → Derecha → Raíz
```

Resultado:

```text
20 40 30 60 80 70 50
```

---

## BFS (Breadth First Search)

Recorrido por niveles.

Resultado:

```text
50 30 70 20 40 60 80
```

---

# 📊 Complejidad Big-O

| Operación | Mejor | Promedio | Peor |
|------------|--------|----------|--------|
| Insertar | O(1) | O(log n) | O(n) |
| Buscar | O(1) | O(log n) | O(n) |
| Eliminar | O(1) | O(log n) | O(n) |
| InOrder | O(n) | O(n) | O(n) |
| PreOrder | O(n) | O(n) | O(n) |
| PostOrder | O(n) | O(n) | O(n) |
| BFS | O(n) | O(n) | O(n) |

---

# 📈 Visualización ASCII

Después de insertar los estudiantes:

```text
── Estructura del BST ──

└── 20210500 [PPA:15.8]
    ├── 20210300 [PPA:14.2]
    │   ├── 20210100 [PPA:12.0]
    │   └── 20210400 [PPA:16.5]
    └── 20210700 [PPA:17.1]
        ├── 20210600 [PPA:13.7]
        └── 20210900 [PPA:18.3]
```

---

# 🔍 Ejemplo de Salida

## InOrder

```text
20210100 Ticona Lupaca, Rosa
20210300 Huanca Apaza, Maria
20210400 Larico Ccama, Carlos
20210500 Mamani Quispe, Juan
20210600 Cutipa Vargas, Elena
20210700 Condori Flores, Pedro
20210900 Pari Choque, Luis
```

---

## Búsqueda

```text
Encontrado:
20210700 Condori Flores, Pedro
PPA: 17.1
```

---

## Estadísticas

```text
Total nodos: 7
Altura: 2
PPA promedio: 15.11
PPA mínimo: 12.0
PPA máximo: 18.3
Total activos: 5
```

---

# 🧪 Benchmark Experimental

Comparación entre:

- BST
- Diccionario (Hash Table)
- Lista

Tamaños evaluados:

```text
100
1000
10000
100000
```

Métricas:

- Tiempo de inserción
- Tiempo de búsqueda
- Altura del árbol

---

# 🚀 Ejecución

## Python

```bash
python bst_academico.py
```

---

## C++

Compilar:

```bash
g++ -std=c++17 ArbolAcademico.cpp main.cpp -o bst
```

Ejecutar:

```bash
./bst
```

---

# 📚 Aplicaciones Reales

Los BST y sus variantes son utilizados en:

- Linux Kernel (Red-Black Tree)
- PostgreSQL (B+ Trees)
- Oracle Database
- .NET SortedDictionary
- Google Maps (KD-Tree)
- Sistemas GIS
- Machine Learning (Decision Trees)

---

# 🛠️ Tecnologías Utilizadas

- Python 3.11
- C++17
- STL (Standard Template Library)
- Dataclasses
- Collections.deque
- Unique Pointer (RAII)
- Visual Studio Code

---

# 👩‍💻 Autor

**[Tu Nombre Completo]**

Estudiante de Ingeniería de Sistemas  
Universidad Nacional del Altiplano – Puno

---

# 📄 Referencias

- Cormen, T. H. et al. (2022). *Introduction to Algorithms*.
- Sedgewick, R. & Wayne, K. (2011). *Algorithms*.
- Knuth, D. E. (2011). *The Art of Computer Programming*.
- MIT OpenCourseWare – Binary Search Trees.
- Python Documentation.
- C++ STL Documentation.

---

⭐ Si este proyecto te resultó útil, puedes darle una estrella al repositorio.

- Cormen, T. H. et al. (2022). *Introduction to Algorithms* (4.ª ed.). MIT Press. https://mitpress.mit.edu/9780262046305/
- Sedgewick, R., & Wayne, K. (2011). *Algorithms* (4.ª ed.). https://algs4.cs.princeton.edu/home/
- Bayer, R., & McCreight, E. M. (1972). Organization and maintenance of large ordered indexes. *Acta Informatica, 1*(3). https://doi.org/10.1007/BF00288683
