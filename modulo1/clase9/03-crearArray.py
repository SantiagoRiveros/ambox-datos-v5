import numpy as np

# Formas de crear un array:

# 1 - np.array
numeros = np.array([1, 2, 3, 4, 5])
print("np.array")
print(numeros)

# 2 - np.arange (SUPER UTIL)
numeros = np.arange(1, 11) # [ 1  2  3  4  5  6  7  8  9 10]
# El primer argumento, es el numero desde el que comienza crear el array
# El segundo, es hasta donde llega el array, sin incluirlo
print("np.arange(1, 11)")
print(numeros)

# Tambien:

numeros = np.arange(0, 20, 2) # [ 0  2  4  6  8 10 12 14 16 18]
# El ultimo argumento, el tercero, es los "pasos" que da entre numero y numero
print("np.arange(0, 20, 2)")
print(numeros)

# La estructura es -> np.arange(inicio, fin, paso)

# 3 - np.linspace (Muy util para generar valores uniformemente)
numeros = np.linspace(0, 100, 5) # [  0.  25.  50.  75. 100.]

print("np.linspace(0, 100, 5)")
print(numeros)
# La diferencia con np.arange es que en este le indicamos cuantos valores queremos
# Ademas, no "evita" el segundo argumento

