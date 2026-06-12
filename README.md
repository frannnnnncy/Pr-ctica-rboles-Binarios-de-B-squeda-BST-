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

- Cormen, T. H. et al. (2022). *Introduction to Algorithms* (4.ª ed.). MIT Press. https://mitpress.mit.edu/9780262046305/
- Sedgewick, R., & Wayne, K. (2011). *Algorithms* (4.ª ed.). https://algs4.cs.princeton.edu/home/
- Bayer, R., & McCreight, E. M. (1972). Organization and maintenance of large ordered indexes. *Acta Informatica, 1*(3). https://doi.org/10.1007/BF00288683
