from colas.fifo import ColaFIFO
from colas.lifo import ColaLIFO
from colas.prio import ColaPRIORITY
from nodo import Nodo
from heuristicas import manhattan, euclidiana

movimientos = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def es_valido(laberinto, pos):
    filas, columnas = len(laberinto), len(laberinto[0])
    return 0 <= pos[0] < filas and 0 <= pos[1] < columnas and laberinto[pos[0]][pos[1]] != 1

def bfs(laberinto, inicio, meta):
    frontera = ColaFIFO()
    frontera.add(Nodo(inicio))
    visitados = set()
    recorrido = []

    while not frontera.empty():
        actual = frontera.pop()
        recorrido.append(actual.estado)
        
        if actual.estado == meta:
            return actual, recorrido
        
        visitados.add(actual.estado)
        
        for mov in movimientos:
            nuevo_estado = (actual.estado[0] + mov[0], actual.estado[1] + mov[1])
            if es_valido(laberinto, nuevo_estado) and nuevo_estado not in visitados:
                frontera.add(Nodo(nuevo_estado, actual))
                
    return None, recorrido

def dfs(laberinto, inicio, meta):
    frontera = ColaLIFO()
    frontera.add(Nodo(inicio))
    visitados = set()
    recorrido = []

    while not frontera.empty():
        actual = frontera.pop()
        recorrido.append(actual.estado)

        if actual.estado == meta:
            return actual, recorrido
        
        visitados.add(actual.estado)

        for mov in movimientos:
            nuevo_estado = (actual.estado[0] + mov[0], actual.estado[1] + mov[1])
            if es_valido(laberinto, nuevo_estado) and nuevo_estado not in visitados:
                frontera.add(Nodo(nuevo_estado, actual))

    return None, recorrido

def greedy(laberinto, inicio, meta, heuristica):
    frontera = ColaPRIORITY()
    frontera.add(Nodo(inicio, heuristica=heuristica(inicio, meta)))
    visitados = set()
    recorrido = []

    while not frontera.empty():
        actual = frontera.pop()
        recorrido.append(actual.estado)

        if actual.estado == meta:
            return actual, recorrido
        
        visitados.add(actual.estado)

        for mov in movimientos:
            nuevo_estado = (actual.estado[0] + mov[0], actual.estado[1] + mov[1])
            if es_valido(laberinto, nuevo_estado) and nuevo_estado not in visitados:
                frontera.add(Nodo(nuevo_estado, actual, heuristica=heuristica(nuevo_estado, meta)))

    return None, recorrido


# TODO: A*