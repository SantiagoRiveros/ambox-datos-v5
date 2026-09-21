import pandas as pd

titanic = pd.read_csv("titanic.csv")

# Vamos a eliminar la columna cabin

titanic = titanic.drop(columns=["Cabin"]) # Esto, elimina Cabin.

# Vamos a reemplazar los valores de edad con su promedio

titanic["Age"] = titanic["Age"].fillna(titanic["Age"].mean())

print(titanic.isnull().sum())

# Reemplazamos los null de Embarked:

titanic["Embarked"] = titanic["Embarked"].fillna("Unknown")

print(titanic.isnull().sum())

# Detectemos duplicados:
print(titanic.duplicated().sum())

# Si hubiera duplicados:
titanic = titanic.drop_duplicates()

titanic.to_csv("titanic-clean.csv", index=False)