import pandas as pd

titanic = pd.read_csv("titanic-clean.csv")

# Renombrar columnas:
titanic = titanic.rename(columns={
    "PassengerId": "id_pasajero",
    "Survived": "sobrevivio",
    "Pclass" : "clase",
    "Sex": "genero",
    "Age": "edad",
    "Fare": "tarifa",
    "Embarked": "puerto_embarque",
    "Name": "nombre",
    "Ticket": "ticket"
})

print(titanic.columns)

# Transformar valores
# en genero tenemos male y female
titanic["genero"] = titanic["genero"].replace({
    "male": "Masculino",
    "female": "Femenino"
})

# En sobrevivio tenemos 1 = sobrevivio y 0 = murio
titanic["sobrevivio"] = titanic["sobrevivio"].astype(bool)

# Vamos a sumar SibSp y Parch para generar grupo_familiar
titanic["grupo_familiar"] = titanic["SibSp"] + titanic["Parch"] + 1 # Incluimos 1 por el pasajero en si

titanic = titanic.drop(columns=["SibSp", "Parch"])
print(titanic.columns)

# Vamos a categorizar a la gente, agregando una nueva columna, segun su edad

def clasificar_edad(edad):
    if edad < 18:
        return "menor"
    else:
        return "mayor"

titanic["grupo_edad"] = titanic["edad"].apply(clasificar_edad)

print(titanic.columns)

titanic.to_csv("titanic-transform.csv", index=False)