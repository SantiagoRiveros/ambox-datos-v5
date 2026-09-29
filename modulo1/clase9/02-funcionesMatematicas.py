import numpy as np

numeros = np.array([10, 20, 30, 40, 50])

# Sumatoria:

print("Sumatoria")
print(np.sum(numeros)) # 150

# Promedio:
print("Promedio")
print(np.mean(numeros)) # 30

# Minimo:
print("Minimo")
print(np.min(numeros))

# Maximo:
print("Maximo")
print(np.max(numeros))

# Desvacion estandar:
print("Desviacion Estandar")
print(np.std(numeros))

# Varianza:
print("Varianza")
print(np.var(numeros))

# Redondeo

print("Redondeo")
precios = np.array([10.234, 20.678, 30.456])

print(np.round(precios, 1))

# Redondeo para abajo:
print("Redondeo Abajo")
print(np.floor(precios))

print("Redondeo Arriba")
print(np.ceil(precios))

# Funciones matematicas:
print("------------------------------")
print("- FUNCIONES MATEMATICAS -")

# Raiz cuadrada:

numeros = np.array([4, 9, 16, 25])

print("Raiz cuadrada")
print(np.sqrt(numeros))

# Valor absoluto:
numeros = np.array([-10, -5, 0, 5, 10])

print("Valor absoluto")
print(np.abs(numeros))

# Exponencial

print("Exponencial")
print(np.exp([1, 2, 3]))

# Logaritmo

print("Logaritmo")
print(np.log([1, 10, 100]))

