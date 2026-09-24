import pandas as pd

enero = pd.read_csv("./csv/ventas_enero.csv")
febrero = pd.read_csv("./csv/ventas_febrero.csv")

ventas = pd.concat([enero, febrero], ignore_index=True)

print(ventas)

df1 = pd.DataFrame({
    "nombre": ["Ana", "Bruno"],
    "edad": [25, 30]
})

df2 = pd.DataFrame({
    "nombre": ["Carla", "Diego"],
    "ciudad": ["Quilmes", "Lanús"]
})

resultado = pd.concat([df1, df2], ignore_index=True)

print(resultado)