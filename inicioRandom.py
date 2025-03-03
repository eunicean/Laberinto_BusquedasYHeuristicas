import random

def cambiar_inicio_aleatorio(laberinto):
    # Buscar todas las posiciones libres (0)
    posiciones_libres = []
    for i in range(len(laberinto)):
        for j in range(len(laberinto[0])):
            if laberinto[i][j] == 0:
                posiciones_libres.append((i, j))

    if not posiciones_libres:
        print("No hay posiciones libres para mover el inicio.")
        return None

    # Buscar y limpiar el inicio actual
    for i in range(len(laberinto)):
        for j in range(len(laberinto[0])):
            if laberinto[i][j] == 2:
                laberinto[i][j] = 0
                break

    # Elegir nueva posición aleatoria
    nuevo_inicio = random.choice(posiciones_libres)
    laberinto[nuevo_inicio[0]][nuevo_inicio[1]] = 2

    return nuevo_inicio
