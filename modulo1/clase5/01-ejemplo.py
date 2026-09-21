import pandas as pd

# Diccionario
datos = {
    "nombre": ["Ana", "Juan", "Pedro"],
    "edad": [25, 32, 28],
    "ciudad": ["Buenos Aires", "La Plata", "Quilmes"],
    "salario": [850000, 1200000, 950000]
}

dataframe = pd.DataFrame(datos)

print(dataframe)

# Lista de diccionarios:
datos2 = [
    {
        "producto": "Notebook",
        "precio": 850000
    },
    {
        "producto": "Mouse",
        "precio": 15000
    },
    {
        "producto": "Teclado",
        "precio": 30000
    }
]

dataframe2 = pd.DataFrame(datos2)

print(dataframe2)

# Listas
productos = ["Notebook", "Mouse", "Teclado"]
precios = [850000, 15000, 30000]

dataframe3 = pd.DataFrame({
    "producto": productos,
    "precios": precios
})

print(dataframe3)

dataframe3.index = ["A", "B", "C"]

print(dataframe3)