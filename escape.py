#Actividad 1 Velocidad de Escape

#Se solicita crear un script escape.py que permita calcular la velocidad de escape
#ingresando como datos de entradas el radio r y la constante g. Los datos de entrada
#deben ingresarse de manera interactiva utilizando la función input().

import math

print("Calculo de la Velocidad de Escape de un Planeta")

#Datos de entrada
#Gravedad
gravedad = float(input("Ingrese la gravedad en m/s: "))

#radio del planeta
radio = float(input("Ingrese el radio del planeta en km: "))

#Calculo
ve1=2*radio*gravedad
ve= math.sqrt(ve1*1000)

#Respuesta
print(f"la velocidad de escape es: {ve}[m/s]")