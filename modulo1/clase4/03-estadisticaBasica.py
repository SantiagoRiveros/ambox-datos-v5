import pandas as pd

dataframe = pd.read_csv("dataframe.csv")

# dataframe_excel = pd.read_excel("nombre_del_archivo")
# dataframe_excel.to_excel("nuevo_archivo")

# promedio
print("Promedio:")
print(dataframe["precio"].mean())

# Sumatoria
print("Sumatoria")
print(dataframe["precio"].sum())

# Minimo
print("Minimo")
print(dataframe["precio"].min())

# Maximo
print("Maximo")
print(dataframe["precio"].max())

# Una de las mas importantes:
print("Describe:")
print(dataframe.describe())



# Ordenar datos:
# por precio, De mayor a menor::

df_ordenado_precio = dataframe.sort_values("precio", ascending=False)

print(df_ordenado_precio)

# sort_values, ordena un dataframe segun su columna