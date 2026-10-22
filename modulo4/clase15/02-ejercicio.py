import matplotlib.pyplot as plt

# Creamos nuestro primer grafico.

meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio"]
ventas = [120, 150, 135, 180, 210, 195]

# Creamos el grafico:
plt.plot(meses, ventas)

# Agreguemos texto a los ejes:
# Eje x : horizontal, eje y: vertical
plt.xlabel("Meses")
plt.ylabel("Ventas")

# Agregamos titulo
plt.title("Evolucion de ventas")

# Guardamos el grafico
plt.savefig("grafico1.jpg")

