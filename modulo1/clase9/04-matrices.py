import numpy as np

# Una matriz es un array multidimensional
matriz = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print(matriz)

# Podemos "preguntar":
print(matriz.shape) # (2, 3) 2 filas, 3 columnas

print(matriz.ndim) # 2, son la cantidad de dimensiones del array

# Accediendo a elementos:

# Primera fila:
print(matriz[0]) # 10, 20, 30

# primer fila, segunda columna:
print(matriz[0][1]) # 20

# Es como si le pasaramos "coordenadas"

# Operaciones sobre matrices:

ventas = np.array([
    [100, 200, 300],
    [150, 250, 350]
])

print(np.sum(ventas)) # suma TODOS los elementos de todas las dimensiones

# Pero, podemos tambien hacerlo por filas o columnas

# Por columnas:

print(np.sum(ventas, axis=0)) # esto suma las columnas

# Por filas:

print(np.sum(ventas, axis=1)) # Esto suma por filas