import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")

dataframe = sns.load_dataset("tips")

# Ejemplo 1 - Histograma con curva de densidad.

# Vamos a ver, que algunas cosas se configuran en seaborn, y otras se hacen en pyplot
plt.figure(figsize=(8, 5)) # Esto es el tamaño del canvas (o lienzo) que vamos a usar.

# Aca definimos el tipo de grafico
sns.histplot(
    data=dataframe, # Aca especificamos la fuente de datos, en este caso el dataframe
    x="total_bill", # Especificamos cual sera el eje horizontal
    bins=20, # Frecuencia de muestreo
    kde=True # Agrega una estimacion suavizada de la distribucion
)

# Ahora los ejes, los textos de los ejes, los definimos en pyplot
plt.title("Distribucion de los importes de las cuentas") # Definimos titulo
plt.xlabel("Importe de la cuenta") # Texto del eje horizontal
plt.ylabel("Frecuencia") # Texto del eje vertical
 
plt.savefig("ejemplo1.jpg") # Guardamos el grafico
plt.clf() # Limpiamos cache

# Ejemplo 2 - Distribuciones por categoria:
plt.figure(figsize=(8, 5))

sns.histplot(
    data=dataframe,
    x="total_bill",
    hue="time",
    bins=20,
    kde=True,
    element="step"
)

plt.title("Importes de las cuentas segun el momento del dia")
plt.xlabel("Importe de la cuenta")
plt.ylabel("Conteo")

plt.savefig("ejemplo2.jpg")
plt.clf()

# Ejemplo 3 - KDE por separado
plt.figure(figsize=(8, 5))

sns.kdeplot(
    data=dataframe,
    x="total_bill",
    hue="time",
    fill=True,
    common_norm=False # Cada grupo se normaliza por separado
)

plt.title("Densidad de los importes por momento del dia")
plt.xlabel("Importe de la cuenta")

plt.savefig("ejemplo3.jpg")
plt.clf()

# Boxplots y Violinplots:

# Ejemplo 4 - Boxplot
plt.figure(figsize=(8, 5))

sns.boxplot(
    data=dataframe,
    x="day",
    y="total_bill"
)

plt.title("Distribucion de las cuentas segun el dia")
plt.xlabel("Dia")
plt.ylabel("Importe de la cuenta")

plt.savefig("ejemplo4.jpg")
plt.clf()

# Ejemplo 5 - Boxplot con una segunda categoria:
plt.figure(figsize=(9, 5))

sns.boxplot(
    data=dataframe,
    x="day",
    y="total_bill",
    hue="time"
)

plt.title("Cuentas por día y momento del día")
plt.xlabel("Día")
plt.ylabel("Importe de la cuenta")

plt.savefig("ejemplo5.jpg")
plt.clf()

# Ejemplo 6 - Violinplot
plt.figure(figsize=(8, 5))

sns.violinplot(
    data=dataframe,
    x="day",
    y="total_bill",
    inner="quartile",
    cut=0
)

plt.title("Distribución de las cuentas por día")
plt.xlabel("Día")
plt.ylabel("Importe de la cuenta")

plt.savefig("ejemplo6.jpg")
plt.clf()

# Ejemplo 7 - Scatterplot con categorias:
plt.figure(figsize=(8, 5))

sns.scatterplot(
    data=dataframe,
    x="total_bill",
    y="tip",
    hue="smoker",
    style="time",
    size="size",
    sizes=(30, 180),
    alpha=0.8
)

plt.title("Relación entre importe y propina")
plt.xlabel("Importe de la cuenta")
plt.ylabel("Propina")

plt.savefig("ejemplo7.jpg")

# Ejemplo 8 - Linea de regresion
plt.figure(figsize=(8, 5))

sns.regplot(
    data=dataframe,
    x="total_bill",
    y="tip",
    scatter_kws={"alpha": 0.6},
    line_kws={"color": "red"}
)

plt.title("Relación entre importe y propina")
plt.xlabel("Importe de la cuenta")
plt.ylabel("Propina")

plt.savefig("ejemplo8.jpg")
plt.clf()

# Ejemplo 9 — Comparar las tendencias por grupo
sns.lmplot(
    data=dataframe,
    x="total_bill",
    y="tip",
    hue="time",
    height=5,
    aspect=1.4
)

plt.title("Relación entre importe y propina por momento del día")
plt.savefig("ejemplo9.jpg")
plt.clf()

# Ejemplo 10 - Promedio de propinas por dia
plt.figure(figsize=(8, 5))

sns.barplot(
    data=dataframe,
    x="day",
    y="tip",
    errorbar=None
)

plt.title("Propina promedio según el día")
plt.xlabel("Día")
plt.ylabel("Propina promedio")

plt.savefig("ejemplo10.jpg")
plt.clf()

# Ejemplo 11 — Cantidad de registros por categoría

plt.figure(figsize=(8, 5))

sns.countplot(
    data=dataframe,
    x="day"
)

plt.title("Cantidad de cuentas registradas por día")
plt.xlabel("Día")
plt.ylabel("Cantidad de registros")

plt.savefig("ejemplo11.jpg")
plt.clf()

# Ejemplo 12 — Matriz de correlación

# Seleccionar únicamente columnas numéricas
numericas = dataframe.select_dtypes(include="number")

# Calcular las correlaciones
correlaciones = numericas.corr()

print(correlaciones)

# Visualizar la matriz
plt.figure(figsize=(8, 6))

sns.heatmap(
    correlaciones,
    annot=True,
    cmap="coolwarm",
    vmin=-1,
    vmax=1,
    fmt=".2f"
)

plt.title("Matriz de correlación")
plt.savefig("ejemplo12.jpg")
plt.clf()

# Ejemplo 13 — Todas las relaciones numéricas

sns.pairplot(
    data=dataframe,
    vars=["total_bill", "tip", "size"],
    hue="time",
    diag_kind="hist"
)

plt.savefig("ejemplo13.jpg")
plt.clf()

# Ejemplo 14 — Un gráfico separado para cada momento del día

sns.relplot(
    data=dataframe,
    x="total_bill",
    y="tip",
    col="time",
    hue="smoker",
    kind="scatter",
    height=4,
    aspect=1.1
)

plt.savefig("ejemplo14.jpg")