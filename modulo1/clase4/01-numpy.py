# Como se importa numpy y pandas? 
# Esto es un comentario, esta linea Visual Studio la va a ignorar
# Sirve para tomar anotaciones
import pandas as pd
# lo primero va importa pandas, la palabra reservada import, seguida del nombre de la libreria
# "as pd" significa que a pandas lo voy a llamar "pd"
import numpy as np

precios = np.array([100, 200, 300, 400]) # Aca cree el array

# Como devuelvo el array, con cada uno de sus elementos multiplicado por dos?


arrayMultiplicado = precios * 2
print("Array original:")
print(precios)
print("Array multiplicado por dos:")
print(arrayMultiplicado)

print(3 * 2)

# Vamos ahora a agregarle 50 a cada uno de los elementos:
print("Array con 50 de mas:")
print(precios + 50)

print("Le restamos 20 al array")
print(precios - 20)

print("dividimos a la mitad todo")
print(precios / 2)

# Ejemplo util de que hacer con esto? Supongamos que tenemos que hacer un aumento del 10%

print(precios * 1.1)

# Funciones matematicas
# Supongamos que queremos sumar todos los numeros de precios:

# Sumatoria
print(np.sum(precios))

# Promedio
print(np.mean(precios))

# Minimo:
print(np.min(precios))

# Maximo:
print(np.max(precios))