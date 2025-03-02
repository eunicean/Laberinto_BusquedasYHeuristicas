from colas.fifo import ColaFIFO
from colas.lifo import ColaLIFO
from colas.prio import ColaPRIORITY
from nodo import Nodo
from heuristicas import manhattan, euclidiana

movimientos = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def dentro_del_laberinto(laberinto, pos):
    filas, columnas = len(laberinto), len(laberinto[0])
    return 0 <= pos[0] < filas and 0 <= pos[1] < columnas and laberinto[pos[0]][pos[1]] != 1

def bfs(laberinto, inicio, meta):
    frontera = ColaFIFO()
    frontera.add(Nodo(inicio))
    visitados = set()
    recorrido = []
    total_hijos = 0  # Para el branching factor

    while not frontera.empty():
        actual = frontera.pop()
        recorrido.append(actual.estado)
        
        if actual.estado == meta:
            branching_factor = total_hijos / len(recorrido)
            return actual, recorrido, branching_factor, total_hijos
        
        visitados.add(actual.estado)
        
        hijos_generados = 0
        for mov in movimientos:
            nuevo_estado = (actual.estado[0] + mov[0], actual.estado[1] + mov[1])
            if dentro_del_laberinto(laberinto, nuevo_estado) and nuevo_estado not in visitados:
                frontera.add(Nodo(nuevo_estado, actual))
                hijos_generados += 1
        total_hijos += hijos_generados

    return None, recorrido, 0, total_hijos

def dfs(laberinto, inicio, meta):
    frontera = ColaLIFO()
    frontera.add(Nodo(inicio))
    visitados = set()
    recorrido = []
    total_hijos = 0

    while not frontera.empty():
        actual = frontera.pop()
        recorrido.append(actual.estado)

        if actual.estado == meta:
            branching_factor = total_hijos / len(recorrido)
            return actual, recorrido, branching_factor, total_hijos
        
        visitados.add(actual.estado)

        hijos_generados = 0
        for mov in movimientos:
            nuevo_estado = (actual.estado[0] + mov[0], actual.estado[1] + mov[1])
            if dentro_del_laberinto(laberinto, nuevo_estado) and nuevo_estado not in visitados:
                frontera.add(Nodo(nuevo_estado, actual))
                hijos_generados += 1
        total_hijos += hijos_generados

    return None, recorrido,0, total_hijos

def greedy(laberinto, inicio, meta, heuristica):
    frontera = ColaPRIORITY()
    frontera.add(Nodo(inicio, heuristica=heuristica(inicio, meta)))
    visitados = set()
    recorrido = []
    total_hijos = 0

    while not frontera.empty():
        actual = frontera.pop()
        recorrido.append(actual.estado)

        if actual.estado == meta:
            branching_factor = total_hijos / len(recorrido)
            return actual, recorrido, branching_factor, total_hijos
        
        visitados.add(actual.estado)

        hijos_generados = 0
        for mov in movimientos:
            nuevo_estado = (actual.estado[0] + mov[0], actual.estado[1] + mov[1])
            if dentro_del_laberinto(laberinto, nuevo_estado) and nuevo_estado not in visitados:
                frontera.add(Nodo(nuevo_estado, actual, heuristica=heuristica(nuevo_estado, meta)))
                hijos_generados += 1
        total_hijos += hijos_generados

    return None, recorrido, 0, total_hijos

def astar(laberinto, inicio, meta, heuristica):
    frontera = ColaPRIORITY()
    frontera.add(Nodo(inicio, costo=0, heuristica=heuristica(inicio, meta)))
    visitados, recorrido = set(), []
    total_hijos = 0

    while not frontera.empty():
        actual = frontera.pop()
        recorrido.append(actual.estado)

        if actual.estado == meta:
            branching_factor = total_hijos / len(recorrido)
            return actual, recorrido, branching_factor, total_hijos
        
        visitados.add(actual.estado)

        hijos_generados = 0
        for mov in movimientos:
            nuevo_estado = (actual.estado[0] + mov[0], actual.estado[1] + mov[1])
            if dentro_del_laberinto(laberinto, nuevo_estado) and nuevo_estado not in visitados:
                costo = actual.costo + 1
                frontera.add(Nodo(nuevo_estado, actual, costo, heuristica(nuevo_estado, meta)))
                hijos_generados += 1
        total_hijos += hijos_generados

    return None, recorrido, 0, total_hijos