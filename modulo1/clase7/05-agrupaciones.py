import pandas as pd

dataframe = pd.read_csv("titanic.csv")

# Promedio de edad por clase:

print("Promedio de edad por clase:")

print(dataframe.groupby("Pclass")["Age"].mean())

# Pandas separo a los pasajeros en tres grupos segun Pclass y calculo el promedio de edad
# de cada grupo

# Tarifa promedio por clase:
print("Tarifa promedio por clase:")
print(dataframe.groupby("Pclass")["Fare"].mean())

# Edad maxima por clase
print("Edad maxima por clase:")
print(dataframe.groupby("Pclass")["Age"].max())

# Agrupar por mas de una columna:

# Cual es la edad promedio segun clase y genero?:

print("Edad promedio segun clase y genero")
print(dataframe.groupby(["Pclass", "Sex"])["Age"].mean())

# Cuantos sobrevivieron de cada clase?
print("Supervivencia por clase")
print(dataframe.groupby("Pclass")["Survived"].sum())

# Proporcion de supervivencia por clase:

print("Proporcion de supervivencia por clase")
print(dataframe.groupby("Pclass")["Survived"].mean() * 100)

# agg() sirve para hacer varios calculos simultaneos

print("AGG:")
print(dataframe.groupby("Pclass")["Age"].agg(["count", "mean", "max", "min"]))

# Varias estadisticas sobre distintas columnas:
print("Varias estadisticas")
print(dataframe.groupby("Pclass").agg({
    "Age": ["mean", "min", "max"],
    "Fare": ["mean", "max"]
}))