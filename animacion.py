import matplotlib.pyplot as plt

def animar_laberinto(laberinto, recorrido, solucion = None):
    plt.xlabel("Laberinto " + str(len(laberinto)) + "x" + str(len(laberinto)))
    lab_copy = [row[:] for row in laberinto]
    for pos in recorrido:
        if lab_copy[pos[0]][pos[1]] == 0:
            lab_copy[pos[0]][pos[1]] = 4
        plt.imshow(lab_copy, cmap='tab20b')
        plt.pause(0.01)
    
    if solucion:
        nodo = solucion
        while nodo:
            pos = nodo.estado
            lab_copy[pos[0]][pos[1]] = 5  # Camino solución
            nodo = nodo.padre
            plt.imshow(lab_copy, cmap='tab20b')
            plt.pause(0.01)
    
    plt.xticks([])
    plt.yticks([])
    plt.show()
