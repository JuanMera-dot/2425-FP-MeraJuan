# Trabajo con diccionarios....
# Crear un diccionario que contenga informacion de la persona....


# Diccionario original
informacion_personal =  {"Nombre": "Juan Mera", "Edad": 18, "Ciudad": "Quito" }

# Diccionario a cambiar
informacion_personal_ =  {"Nombre": "Juan Mera", "Edad": 18, "Ciudad": "Quito" }

print("Diccionario original")
print(informacion_personal)

# Acceder a la clave "ciudad" y cambiarla
informacion_personal_["Ciudad"] = "Guayaquil"

# Agregar una clave-valor que represente la profesion de la persona
informacion_personal_["Profesion"] = "Carpintero"

# Verificar si cuenta con un numero telefonico y sino, agregarlo
informacion_personal_["Telefono"] = 0,9,6,4,7,8,8,8,5,6

# Eliminar la clave "Edad"
del(informacion_personal_["Edad"])

# Imprimir el diccionario despues de los cambios
print("Diccionario alternativo")
print(informacion_personal_)

