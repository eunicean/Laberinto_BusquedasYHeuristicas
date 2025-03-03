# Resolución de Laberinto - Busquedas Y Heuristicas

#### Librerías necesarias


```
pip install matplotlib.pyplot
pip install heapq
```
### Programa
Para probrar el programa se debe correr el archivo [main.py](main.py) y responder los datos que le piden.

Si se quiere probar un laberinto diferentes, se tiene que agregar a la carpeta [laberintos/](laberintos/) en un archivo .txt. Para que el programa lea el laberinto necesita estar en el siguiente formato (sin '' ni ;)

```
1,1,1,1,1,1,1,1,1,1,1,1,1,1,1
1,3,0,0,1,0,0,1,0,0,0,0,0,0,1
1,0,0,0,1,0,0,1,0,0,1,0,0,0,1
1,0,0,0,1,0,0,1,0,0,1,0,0,0,1
1,0,0,0,1,0,0,1,0,0,1,0,0,0,1
1,1,0,0,1,0,0,0,0,0,1,0,0,0,1
1,0,0,0,1,1,1,0,0,0,1,0,1,1,1
1,0,0,0,1,0,0,0,0,0,1,0,0,0,1
1,0,0,0,1,0,0,0,0,0,1,0,0,0,1
1,0,0,0,1,0,0,0,0,0,1,0,0,0,1
1,0,0,0,1,0,0,0,0,0,1,0,0,0,1
1,0,0,0,1,0,0,0,0,0,1,0,0,0,1
1,0,0,0,1,0,0,0,0,0,1,0,0,0,1
1,0,0,0,0,0,0,0,0,0,1,0,0,2,1
1,1,1,1,1,1,1,1,1,1,1,1,1,1,1

```
Puede ser una matriz no cuadra

### Colas y algoritmos de búsqueda
#### Colas
- [cola FIFO](colas/fifo.py)
- [cola LIFO](colas/lifo.py)
- [cola PRIORITY](colas/prio.py) → Esta es la que usa heapq
#### Nodo
- [Nodo](nodo.py)
#### Algoritmos de búsqueda
- [BFS, DFS, GFS, A*](busqueda.py)
#### Heuristicas
- [Manhattan y Euclidiana](heuristicas.py)
    - [Ecuacion Manhattan referencia](https://en.wikipedia.org/wiki/Taxicab_geometry)
    - [Ecuacion Euclidiana referencia](https://en.wikipedia.org/wiki/Euclidean_distance)

### Referencias para crear código base
- [Tutorial on Path Problems in a Grid, Maze, or Matrix](https://www.geeksforgeeks.org/tutorial-on-path-problems-in-a-grid-maze-or-matrix/)
- [Rat in a maze](https://www.geeksforgeeks.org/rat-in-a-maze/)