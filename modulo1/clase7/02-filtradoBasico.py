import pandas as pd

dataframe = pd.read_csv("titanic.csv")

# Devolvemos solo Pclass, sex y survived

print(dataframe[["Pclass", "Survived", "Sex"]])

# Devolver con una condicion

# Solo los pasajeros que son mayores de 50 años
print(dataframe[dataframe["Age"] > 50])

# Cuantos pasajeros sobrevivieron?
print("-------------------------")
print(dataframe[dataframe["Survived"] == 1]) # Sobrevivieorn 342 personas

# Cuantas mujeres sobrevivieron?
print(dataframe[(dataframe["Sex"] == "female") & (dataframe["Survived"] == 1)]) # 233

# Edad promedio de los pasajeros:
print(dataframe["Age"].mean())

# Pasajeros de primera clase:
print(dataframe[dataframe["Pclass"] == 1]) # 216

# Pasajeros de segunda clase:
print(dataframe[dataframe["Pclass"] == 2]) # 184

# Pasajeros de tercera clase:

print(dataframe[dataframe["Pclass"] == 3]) # 491

# Tarifa promedio:
print(dataframe["Fare"].mean())

# Pasajeros de primera clase que sobrevivieron:
print(dataframe[(dataframe["Pclass"] == 1) & (dataframe["Survived"] == 1)]) # 136