import pandas as pd

df = pd.DataFrame({
    "producto": ["Notebook", "Mouse", "Teclado", "Monitor", "Auriculares"],
    "categoria": ["Computación", "Accesorios", "Accesorios", "Computación", "Audio"],
    "precio": [850000, 15000, 30000, 250000, 80000],
    "stock": [10, 50, 25, 15, 40]
})

# head = Primeras filas, por defecto muestra 5
print(df.head(3))

# tail = ultimas 5 filas, le podemos pedir otro numero
print(df.tail(2))

# shape = Muestra dimensiones: (5, 4) 5 filas 4 columnas
print(df.shape)

# columns = Obtener valor de columnas
print(df.columns)

# informacioin general con info
print(df.info())

""" 
Cantidad de filas.
Cantidad de columnas.
Nombre de columnas.
Valores no nulos.
Tipo de dato.
Posibles problemas.
"""

# dtypes = tipos de datos:
print(df.dtypes)

# isnull = detecta valores nulos:
print(df.isnull())

# Si queremos saber cuantos:
print(df.isnull().sum())

# describe = estadistica descriptiva:
print(df.describe())

""" 
count

Cantidad de valores disponibles.

mean

Promedio.

std

Desviación estándar.

min

Valor mínimo.

25%

Primer cuartil.

50%

Mediana.

75%

Tercer cuartil.

max

Valor máximo.
 """

# Estadisticas indivuales:

# promedio
print(df["precio"].mean())

# mediana
print(df["precio"].median())

# minimo
df["precio"].min()

# maximo

print( df["precio"].max())

# desviacion estandar:

print(df["precio"].std())

# sumatoria:
print(df["precio"].sum())

# conteo:
print(df["precio"].count())


# VARIABLES CATEGORICAS:

# Esto nos permite saber cuántas veces aparece cada categoría.
print(df["categoria"].value_counts())

# Categorias diferentes:
print(df["categoria"].nunique())

# Para ver cuales son:
print(df["categoria"].unique())