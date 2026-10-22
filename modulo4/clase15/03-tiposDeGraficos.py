# Importamos la libreria:
import matplotlib.pyplot as plt

meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo"]
ventas = [100, 150, 130, 180, 220]

# Grafico de Lineas:
# Sirve para mostrar la evolucion de una variable, por ejemplo las ventas a lo largo del tiempo

plt.plot(meses, ventas, marker="o", color="blue")

# Le damos titulos y estilos

plt.title("Ventas mensuales")
plt.xlabel("Mes")
plt.ylabel("Unidades Vendidas")
plt.grid(True)

plt.savefig("lineas.jpg")

# IMPORTANTE: Luego de graficar, siempre ejecutamos esto para borrar el cache del grafico
plt.clf()

# Grafico de barras:
# Sirve para comparar valores entre distintas categorias, como las ventas de diferentes productos

productos = ["Mouse", "Teclado", "Monitor", "Auriculares"]
ventas = [50, 35, 20, 45]

plt.bar(productos, ventas, color="steelblue")

# Damos titulos y estilos:
plt.title("Ventas por producto")
plt.xlabel("Producto")
plt.ylabel("Unidades vendidas")

plt.savefig("barras.jpg")

plt.clf()

# Grafico de barras horizontales:
# Similar al anterior, pero las barras son horizontales, util cuando las categorias tienen nombres largos

productos = ["Mouse inalámbrico", "Teclado mecánico", "Monitor", "Auriculares"]
ventas = [50, 35, 20, 45]

plt.barh(productos, ventas, color="seagreen")

# Titulo y estilos:
plt.title("Ventas por producto")
plt.xlabel("Unidades Vendidas")
plt.ylabel("Producto")

plt.savefig("barras-horizontales.jpg")
plt.clf()

# Grafico de sectores o torta:
# Sirve para mostrar como se distribuye un total entre distintas categorias:

categorias = ["Tecnologia", "Indumentaria", "Hogar", "Deportes"]
ventas= [40, 25, 20, 15]

plt.pie(
    ventas,
    labels=categorias,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Porcentaje de ventas por categoria")

plt.savefig("torta.jpg")
plt.clf()

# Histograma
# Sirve para observar como se distribuyen los valores numericos agrupandolos en intervalos

notas = [
    4, 5, 6, 7, 8, 9, 6, 7, 5, 8,
    9, 10, 6, 7, 8, 4, 5, 9, 7, 8
]

plt.hist(notas, bins=10, edgecolor="black", color="orange")

plt.title("Distribucion de notas")
plt.xlabel("Nota")
plt.ylabel("Cantidad de alumnos")

plt.savefig("histograma10bins.jpg")
plt.clf()

# Grafico de dispersion (Scatterplot):
# Sirve para explorar las relacion entre dos variables numericas:

horas_estudio = [1, 2, 2, 3, 4, 4, 5, 6, 7]
notas = [4, 5, 6, 5, 7, 8, 7, 9, 10]

plt.scatter(horas_estudio, notas, color="purple")

plt.title("Horas de estudio de y notas")

plt.xlabel("Horas de estudio")
plt.ylabel("Nota obtenida")

plt.savefig("scatterplot.jpg")
plt.clf()

# Graficos de lineas con varias series:
# permite comparar dos conjuntos de datos en el mismo grafico, por ejemplo las ventas de dos años.


meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo"]

ventas_2025 = [100, 120, 115, 140, 160]
ventas_2026 = [110, 130, 125, 155, 180]

plt.plot(meses, ventas_2025, marker="o", label="2025")
plt.plot(meses, ventas_2026, marker="s", label="2026")

plt.title("Comparación de ventas")
plt.xlabel("Mes")
plt.ylabel("Unidades vendidas")

plt.legend()
plt.grid(True)

plt.savefig("lineas-multiseries.jpg")
plt.clf()

# Caja y bigotes: Boxplot
# Sirve para resumir la distribución de los datos, visualizar la mediana, la dispersión y posibles valores atípicos.
notas = [4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 10, 20]

plt.boxplot(notas)

plt.title("Distribución de notas")
plt.ylabel("Nota")

plt.savefig("boxplot.jpg")