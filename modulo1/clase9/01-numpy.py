import numpy as np

# Lista vs Array

numeros = [10, 20, 30, 40, 50]

# Ahora quiero sumarle 1 a todos los indices:

resultado = []

for numero in numeros:
    resultado.append(numero + 1)

print(resultado)

#Ahora:

numerosArray = np.array([10, 20, 30, 40, 50])

print(numerosArray + 1) # suma

print(numerosArray - 1) # resta

print(numerosArray / 2) # division

print(numerosArray * 2) # multiplicacion

# Operaciones entre arrays
precios = np.array([100, 200, 300, 400])

cantidades= np.array([2, 3, 1, 4])

#podemos hacer:

total = precios * cantidades

print(total)