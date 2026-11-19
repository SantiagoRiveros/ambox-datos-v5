import numpy as np

ventas = np.array([100, 150, 120, 80, 200])

print("Ventas: ", ventas)

# Calcular la media:
media = np.mean(ventas)

# Calcular la mediana
mediana = np.median(ventas)

# Calcular la desviacion estandar:
desviacion = np.std(ventas)

print("Media:", media)
print("Mediana:", mediana)
print("Desviación estándar:", desviacion)