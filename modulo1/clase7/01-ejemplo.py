import pandas as pd

dataframe = pd.read_csv("titanic.csv")

# Estadisticas:

print("-------------- HEAD")
print(dataframe.head())

print("-------------- SHAPE")
print(dataframe.shape)

print("-------------- COLUMNS")
print(dataframe.columns)

print("-------------- INFO")
print(dataframe.info())

print("-------------- DESCRIBE")
print(dataframe.describe())