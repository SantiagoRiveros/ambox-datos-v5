import pandas as pd

dataframe = pd.read_csv("resultado.csv")

# vamos a agregarle una columna con el valor total de la venta:

dataframe["total"] = (dataframe["cantidad"] * dataframe["precio_unitario"])

print(dataframe[["precio_unitario", "cantidad", "total"]])