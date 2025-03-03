import os
import time
from busqueda import bfs, dfs, greedy, astar
from heuristicas import manhattan, euclidiana
from animacion import animar_laberinto


def cargar_laberinto():
    laberintos = os.listdir("laberintos")
    print("\nSeleccione el archivo del laberinto:\n")
    for i, archivo in enumerate(laberintos):
        print(f"{i+1}. {archivo}")
    eleccion = int(input("\n-> ")) - 1

    archivo = 'laberintos/' + laberintos[eleccion]
    with open(archivo, 'r') as file:
        laberinto = []
        for row in file:
            laberinto.append([int(x) for x in row.strip().split(',')])
    return laberinto


def encontrar_puntos(laberinto, valor):
    puntos = []
    for i, fila in enumerate(laberinto):
        for j, celda in enumerate(fila):
            if celda == valor:
                puntos.append((i, j))
    return puntos

stay = True
while(stay):
    laberinto = cargar_laberinto()

    # Buscar inicio y meta
    inicios = encontrar_puntos(laberinto, 2)
    metas = encontrar_puntos(laberinto, 3)
    if not inicios or not metas:
        print("No se encontró inicio (2) o meta (3) en el laberinto.")
        break
    inicio = inicios[0]
    meta = metas[0]

    # Selección de algoritmo
    print("\nSeleccione el algoritmo de búsqueda:")
    print("1. Breadth First Search")
    print("2. Depth First Search")
    print("3. Greedy First Search")
    print("4. A*")
    print("5. Salir")
    algoritmo = int(input("\n-> "))

    heuristica = None
    heuristica_opcion = 0
    if algoritmo in [3, 4]:
        print("\nSeleccione la heurística:")
        print("1. Distancia Manhattan")
        print("2. Distancia Euclidiana")
        heuristica_opcion = int(input("\n-> "))
        heuristica = manhattan if heuristica_opcion == 1 else euclidiana

    inicio_tiempo = time.time()
    if algoritmo == 1:
        print("\n+--------------------------------+")
        print("| Algoritmo Breadth First Search ")
        print("+--------------------------------+")
        solucion, recorrido, branching_factor, total_branches = bfs(laberinto, inicio, meta)
    elif algoritmo == 2:
        print("\n+------------------------------+")
        print("| Algoritmo Depth First Search |")
        print("+------------------------------+")
        solucion, recorrido, branching_factor, total_branches = dfs(laberinto, inicio, meta)
    elif algoritmo == 3:
        print("\n+-------------------------------+")
        print("| Algoritmo Greedy First Search |")
        print("+-------------------------------+")
        if(heuristica_opcion!= 0):
            print("|           Manhattan           |\n+-------------------------------+" if heuristica_opcion==1 else "|           Euclidiana          |\n+-------------------------------+")
        solucion, recorrido, branching_factor, total_branches = greedy(laberinto, inicio, meta, heuristica)
    elif algoritmo == 4:
        print("\n+--------------+")
        print("| Algoritmo A* | ")
        print("+--------------+")
        if(heuristica_opcion!= 0):
            print("|   Manhattan  |\n+-------------+" if heuristica_opcion==1 else "|  Euclidiana  |\n+--------------+")
        solucion, recorrido, branching_factor, total_branches = astar(laberinto, inicio, meta, heuristica)
    elif algoritmo == 5:
        print("¡Hasta la próxima!")
        stay = False
        break
    else:
        print("\nAlgoritmo no válido.")
        break
    fin_tiempo = time.time()

    if solucion and algoritmo != 5 :
        camino = []
        nodo = solucion
        while nodo:
            camino.append(nodo.estado)
            nodo = nodo.padre
        camino.reverse()

        print(f"¡Solución encontrada! :D")
        print(f"Nodos visitados: {len(recorrido)}")
        print(f"Largo del camino: {len(camino)}")
        print(f"Branches totales creadas: {total_branches}")
        print(f"Branch creadas en promedio por cada nodo expandido: {branching_factor:.2f}")
        print(f"Tiempo de ejecución: {fin_tiempo - inicio_tiempo:.4f} segundos")
    else:
        print("\nNo se encontró solución. :(")
        print(f"\n Cant. nodos revisados: {total_branches:.2f}")
        camino = None
        
    animar_laberinto(laberinto, recorrido, solucion)

