import pandas as pd

dataframe = pd.read_csv("titanic.csv")

# Quiero nombre, edad y tarifa de pasajeros mayores de 50.

resultado1 = dataframe[dataframe["Age"] > 50][["Name", "Age", "Fare"]]

print(resultado1)

# Que pasa si queremos devolver pasajeros de primera o segunda clase?

# Podriamos hacer:

resultado2 = dataframe[(dataframe["Pclass"] == 1) | (dataframe["Pclass"] == 2)]

print(resultado2)

# Existe el metodo isin:

resultado3 = dataframe[dataframe["Pclass"].isin([1, 2])]
print(resultado3)

print("-------------------------------------")
# Top 5 precios de pasaje:
top5pasaje = dataframe["Fare"].sort_values().head()  # Orden Ascendente

pasajeDescedente = dataframe["Fare"].sort_values(ascending=False).head()  # Descendente

print(top5pasaje)

print(pasajeDescedente)