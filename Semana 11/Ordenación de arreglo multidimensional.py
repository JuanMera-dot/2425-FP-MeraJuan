# Ordenación de arreglo multidimensional


matriz = [
    [9, 3, 5],
    [1, 6, 8],
    [4, 7, 2]
]

matriz_ = [element for fila in matriz for element in fila]
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

matriz_or = bubbleSort(matriz_)
matriz_or = [matriz_or[i:i+3] for i in range (0, len(matriz_or), 3)]

print("Matriz original. : ", matriz)
for fila in matriz:
    print(fila)

print("Matriz organizada. : ", matriz_or)
for fila in matriz_or:
    print (fila)




