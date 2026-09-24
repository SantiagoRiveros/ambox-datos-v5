import pandas as pd

clientes = pd.read_csv("./csv/clientes.csv")
productos = pd.read_csv("./csv/productos.csv")
ventas = pd.read_csv("./csv/ventas.csv")
""" 
print(clientes)
print(productos)
print(ventas) 
"""

resultado = pd.merge(ventas, clientes, on="cliente_id")
print(resultado)

# resultado.to_excel("resultado.xlsx")

resultadoLeft = pd.merge(ventas,clientes,on="cliente_id",how="left")

print(resultadoLeft)

resultadoOuter = pd.merge(ventas, clientes, on="cliente_id", how="outer")

print(resultadoOuter)

# Ahora vamos a unir el resultado con productos
resultado = pd.merge(resultado, productos, on="producto_id", how="left")

resultado.to_csv("resultado.csv")