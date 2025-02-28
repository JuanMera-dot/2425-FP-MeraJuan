# Busqueda en arreglo multidimencional

Matriz = [
    [3, 4, 5],
    [7, 6, 8],
    [9, 10, 4]
]

valor_a_buscar =  4
fila_e = -1
columna_e = -1

if any(valor_a_buscar in fila for fila in Matriz):
    print("Se encontró el valor buscado en la matriz = ", valor_a_buscar)

else:
    print("El valor no se encontró. ")

for fila in range(len(Matriz)):
    for columna in range(len(Matriz[fila])):
        if Matriz[fila][columna] == valor_a_buscar:
            fila_e = fila
            columna_e = columna
            break
    if fila_e != -1:
        break


if fila_e != -1:
    print("Se encontró el valor en la fila: ", fila_e, "y en la columna: ", columna_e )

else:
    print("No se encontró la posicion")