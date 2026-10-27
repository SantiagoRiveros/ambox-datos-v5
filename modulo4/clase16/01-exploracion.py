import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Este dataset que vamos au tilizar lo trae seaborn incorporado, y nos sirve para aprender.

# Vamos a darle el "tema" a seaborn
sns.set_theme(style="whitegrid")

# Cargamos el dataset de Tips

dataframe = sns.load_dataset("tips") # Esto nos carga el dataset "Tips" de seaborn

# Primeras Filas:
print("Primeras Filas:")
print(dataframe.head())

print("-------------------------------------------------")

# Cantidad de filas y columnas:
print("Cantidad de filas y columnas:")
print(dataframe.shape)

print("-------------------------------------------------")

# Informacion de las variables:
print("Informacion de las variables:")
print(dataframe.info())

print("-------------------------------------------------")

# Resumen estadistico:
print("Resumen estadistico")
print(dataframe.describe())

print("-------------------------------------------------")

""" 
1. ¿Las cuentas más altas suelen tener propinas más altas?
2. ¿Qué día se registran las cuentas más elevadas?
3. ¿Cambian las propinas según el tamaño de la mesa?
4. ¿Hay diferencias entre almuerzos y cenas?
"""

# [10, 11, 12, 9999, 4542524542]