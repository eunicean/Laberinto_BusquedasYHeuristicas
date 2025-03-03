import matplotlib.pyplot as plt

def animar_laberinto(laberinto, recorrido, solucion=None, bloque=50):
    lab_copy = [row[:] for row in laberinto]

    plt.figure(figsize=(6, 6))

    # Animación del recorrido explorado
    for i, pos in enumerate(recorrido):
        if lab_copy[pos[0]][pos[1]] == 0:
            lab_copy[pos[0]][pos[1]] = 4  # Nodo explorado
        if i % bloque == 0:
            plt.clf()
            plt.imshow(lab_copy, cmap='tab20b')
            plt.title(f"Explorando... Nodo {i}/{len(recorrido)}")
            plt.pause(0.001)

    plt.clf()
    plt.imshow(lab_copy, cmap='tab20b')
    plt.title("Exploración completa")
    plt.pause(1)

    if solucion:
        nodo = solucion
        camino = []
        while nodo:
            camino.append(nodo.estado)
            nodo = nodo.padre
        camino

        for i, pos in enumerate(camino):
            lab_copy[pos[0]][pos[1]] = 5  # Camino solución
            plt.clf()
            plt.imshow(lab_copy, cmap='tab20b')
            plt.title(f"Mostrando solución... Paso {i+1}/{len(camino)}")
            plt.pause(0.02)

    plt.title("¡Camino final encontrado!")
    plt.show()
