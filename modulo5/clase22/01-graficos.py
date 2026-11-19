import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("datos.csv")

print("HEAD")
print(df.head())
print("--------------------------")
print("INFO")
print(df.info())
print("--------------------------")
print("DESCRIBE")
print(df.describe())

# Histograma
# ¿Como se distribuyen los importes de las ventas de nuestra tienda?

# ¿Toda slas ventas tienen el mismo importe?
# ¿La mayoria sonv entas pequeñas o grandes?
# ¿Existen algunas ventas mucho mas grandes que el resto?

sns.histplot(data=df, x="ventas", bins=40)

plt.title("Distribucion de los importes de venta")
plt.xlabel("Importe de venta")
plt.ylabel("Cantidad de operaciones")

plt.savefig("histograma.jpg")
plt.clf()

# KDE (Kernel Density Estimation)

sns.kdeplot(data=df, x="ventas", fill=True)

plt.title("Densidad de los importes de ventas")
plt.xlabel("Importe de venta")
plt.ylabel("Densidad")

plt.savefig("kde.jpg")
plt.clf()

# Combinar Histograma con kde

sns.histplot(
    data=df,
    x="ventas",
    bins=8,
    kde=True
)

plt.title("Distribución de ventas")
plt.xlabel("Importe de venta")
plt.ylabel("Frecuencia")

plt.savefig("hist-kde.jpg")
plt.clf()

# Boxplot para ver valores atipicos

sns.boxplot(data=df, x="ventas")

plt.title("Distribución y valores atípicos de las ventas")
plt.xlabel("Importe de venta")

plt.savefig("boxplot.jpg")
plt.clf()

# Scatterplot - Existe relacion entre dos variables?

sns.regplot(
    data=df,
    x="publicidad",
    y="ventas"
)

plt.title("Publicidad vs Ventas")
plt.xlabel("Inversión en publicidad")
plt.ylabel("Importe de ventas")

plt.savefig("regplot.jpg")

plt.clf()

# heatmap

correlacion = df.corr(numeric_only=True)

plt.figure(figsize=(10, 7))

sns.heatmap(
    correlacion,
    annot=True,
    cmap="coolwarm",
    vmin=-1,
    vmax=1,
    fmt=".2f"
)

plt.title("Matriz de correlación")

plt.savefig("heatmap.jpg")