# TODO: cambiar diferentes procesos a funciones

import os

labyrinths = os.listdir("laberintos")

print("Seleccione el numero de archivo que desea abrir:\n")
for x in range(len(labyrinths)): 
    print(f"{x+1}. {labyrinths[x]}")
to_resolve = int(input("->")) - 1


file_path = 'laberintos/' + labyrinths[to_resolve]
print(file_path)
try:
    with open(file_path, 'r') as file:
        data = []
        for row in file:
            data.append([int(x) for x in row.split(',')])

except FileNotFoundError:
    print(f'{file_path} not found')
except Exception as e:
    print(f'An error occurred: {e}')

# Graficando el laberinto desde la matriz

import numpy as np  
import matplotlib.pyplot as plt 

plt.imshow(data, cmap='binary')  
plt.xticks([])  # Ocultar marcas de los ejes  
plt.yticks([])  
plt.show()