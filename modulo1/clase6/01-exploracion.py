import pandas as pd

titanic = pd.read_csv("titanic.csv")

print("----------- COLUMNS")
print(titanic.columns)

print("----------- HEAD")
print(titanic.head())

print("----------- SHAPE") # (891, 12) 891 filas, 12 columnas
print(titanic.shape)

print("------------ INFO")
print(titanic.info())

print("------------ DESCRIBE")
print(titanic.describe())

# VAMOS A VER QUE FALTA
print("-------------- NULOS")
print(titanic.isnull().sum())

# Porcentaje de nulos:
print((titanic.isnull().sum() / len(titanic)) * 100)

# Cuantos pasajeros tienen Age vacio y sobrevivieron
print(titanic[(titanic["Age"].isna()) & (titanic["Survived"] == 1)].shape[0])

# Cuantos no sobrevivieron?
print(titanic[(titanic["Age"].isna()) & (titanic["Survived"] == 0)].shape[0])