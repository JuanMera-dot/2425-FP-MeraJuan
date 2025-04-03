# Acceder al archivo_Lectura 1

print("Lectura uno\n")
file = open('my_notes.txt', 'r')
lineas = file.readlines()
print(lineas)
# Cerrar el archivo
file.close()

print("\n")

## lectura 2

print("Lectura dos\n")
with open('my_notes.txt', 'r') as archivo:
    lineas = archivo.readlines()
for l in lineas:
    print(l.replace('\n', ''))

# Agregar un parametro str al achivo de texto
with open('my_notes.txt', 'a') as archivo:
    archivo.write('Chile')




