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
        # Read the content of the file
        file_content = file.read()
        
        # Print the content
        print('File Content:\n', file_content)

except FileNotFoundError:
    print(f'{file_path} not found.&quot;')
except Exception as e:
    print(f'An error occurred: {e}')