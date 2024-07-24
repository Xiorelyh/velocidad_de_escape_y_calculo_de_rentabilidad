import math

#Calculo de Rentabilidad Nro.2

#Utilidades = P * U - GT
#u_normal: usuario normal
#u_premium: usuario premium
#p_normal: precio plan basico
#p_premium: precio plan premium
#GT: Gastos Totales


#Informacion solicitada al usuario
#Tipos de Usuarios
u_normal = int(input("Ingrese el numero de usuarios plan básico: "))
u_premium = int(input("Ingrese el numero de usuarios plan premium: "))

# Precios de suscripción en CLP
p_normal = float(input("Ingrese el precio de suscripción PLAN BÁSICO en CLP: "))
p_premiun = float(input("Ingrese el precio de suscripción PLA PREMIUM en CLP: "))
gt = float(input("Ingrese gasto total: "))

#Calculo de rentabilidad
utilidades = (p_normal * u_normal) + (p_premiun * u_premium) - gt

#Resultado
print(f"La utilidad es de: ${utilidades:}")