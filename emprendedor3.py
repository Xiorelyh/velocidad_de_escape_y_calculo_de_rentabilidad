import math

#Calculo de Rentabilidad Nro.3

#Utilidades = P * U - GT
#p: Precio de Suscripción
#u: Número de Usuarios
#gt: Gastos Totales
#u_anterior: utilidades año anterior

#Informacion solicitada al usuario
p = float(input("Ingrese el precio de suscripción: "))
u = int(input("Ingrese el numero de usuarios: "))
gt = float(input("Ingrese gasto total: "))
u_anterior = float(input("Ingrese las utilidades del año anterior, Deben ser distinto a 0!!!: "))

#Calculo de utilidad
utilidades = p * u - gt
razon_de_utilidad = utilidades/u_anterior

#Resultados
print(f"Las utilidades obtenidades de este año es de: {utilidades}")
print(f"La razón entre la utilidad actual y la del año anterior es de : {razon_de_utilidad:.2f}")