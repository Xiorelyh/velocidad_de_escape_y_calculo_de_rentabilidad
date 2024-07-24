#Un emprendedor quiere crear una app que provea un servicio de entrega de comida para
#mascotas. Este proyecto tiene buenos pronósticos, pero su éxito dependerá de cuántos
#usuarios pueda alcanzar. La manera en la que se medirá esto es calculando las utilidades
#del proyecto

import math

#Calculo de Rentabilidad Nro.1

print("Calculo de rentabilidad de APP")

#Informacion solicitada al usuario
precio_suscripcion = float(input("Ingrese monto de suscripcion: "))
numero_usuarios = float(input("Ingrese nro. de usuarios: "))
gastos_totales = float(input("Ingrese total de gastos: "))

#Calculo de rentabilidad
utilidades = precio_suscripcion * numero_usuarios - gastos_totales

#Resultado
print(f"La rentabilidad es: {utilidades}$")