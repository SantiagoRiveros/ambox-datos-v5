import pandas as pd

# Empezamos creando un diccionario cuyos valores son listas:
datos = {
    "producto": ["Notebook", "Mouse", "Teclado", "Monitor"],
    "precio": [800000, 25000, 45000, 300000],
    "stock": [5, 30, 20, 8]
}

# Creamos un DataFrame
dataframe = pd.DataFrame(datos)

print(dataframe)

# Como muestro una columna?
#Supongamos que quiero mostrar columna "producto"
print(dataframe["producto"])

# Si quiero mostrar varias:
print(dataframe[["producto", "precio"]])

# Seleccionamos filas:
# al metodo iloc, le pasamos entre corchetes, el numero de indice de la fila

# primera fila:
print(dataframe.iloc[0])

# segunda fila
print(dataframe.iloc[1])

# SI queremos un rango de filas:
print(dataframe.iloc[0:2])
# El primer numero es el primer indice que muestra
# El ultimo es hasta donde muestra, sin incluirlo
# Es decir, me va a mostrar indice 0 y 1

# Filtrar Datos:

print("FILTRADO DE DATOS")

# Productos con mayor precio que 100.000
print("Productos con mayor precio que 100.000")
print(dataframe[dataframe["precio"] > 100000]) # dEVUELVE solo las filas con precio > 100.000

# Productos con stock menor a 10:
print("Productos con stock menor a 10:")
print(dataframe[dataframe["stock"] < 10])

# Producto específico:
print("Producto específico:")
print(dataframe[dataframe["producto"] == "Mouse"])

# productos con precio mayor a 100.000 y stock menor a 10
print("productos con precio mayor a 100.000 y stock menor a 10")
print(dataframe[(dataframe["precio"] > 100000) & (dataframe["stock"] < 10)]) # el simbolo & conecta dos condiciones

# Creando nuevas columnas:
# QUeremos saber cuanto dinero representa el stock de cada producto:
dataframe["valor_stock"] = dataframe["precio"] * dataframe["stock"]
# Es una columna calculada, por cada fila, multiplica el valor de precio por el de stock
print(dataframe)

# VAmos a guardar el dataframe en un archivo:
dataframe.to_csv("dataframe.csv") # Esto es para guardar el dataframe en un archivo