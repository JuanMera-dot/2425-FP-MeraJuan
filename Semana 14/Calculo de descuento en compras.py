
print("**Bienvenido**")
print("///// Sistema de facturacion /////")


# Asignar montos para el calculo

monto_uno = 300
monto_dos = 200
porcentaje_descuento_dos = 15


# Crear una funcion que tome dos parametros

def calcular_descuento(monto_total, porcentaje_descuento_uno = 30 ):
    descuento = (monto_total + porcentaje_descuento_uno) / 100

    return descuento


descuento_uno = calcular_descuento(monto_uno)
descuento_dos = calcular_descuento(monto_dos, porcentaje_descuento_dos)


#Calculo del porcentaje total

porcentaje_total_uno = monto_uno - descuento_uno
porcentaje_total_dos = monto_dos - descuento_dos

# Muestra de resultados

print(f"Compra uno, Total: {monto_uno: }$, Porcentaje de descuento, Total: {descuento_uno: }%, Valor a pagar final: {porcentaje_total_uno: }$")
print(f"Compra dos, Total: {monto_dos: }$, Porcentaje de descuento, Total: {descuento_dos: }%, Valor a pagar final: {porcentaje_total_dos: }$")


