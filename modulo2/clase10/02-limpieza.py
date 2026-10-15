import pandas as pd

dataframe = pd.read_csv("coffe_sales.csv")

# Ver valores faltantes
print("Valores faltantes:")
print(dataframe.isnull().sum()) # card 89

dataframe["card"] = dataframe["card"].fillna("NO CARD")

# Verificamos duplicados
print(dataframe.duplicated().sum())


dataframe["date"] = pd.to_datetime(dataframe["date"])
print(dataframe["date"].head())

print(dataframe["date"].dt.year) # Año
print(dataframe["date"].dt.month) # Mes
print(dataframe["date"].dt.day) # Dia



dataframe["datetime"] = pd.to_datetime(dataframe["datetime"])

print(dataframe["datetime"].head())

dataframe.to_csv("coffe_sales_clean.csv", index=False)