import pandas as pd

dataframe = pd.read_csv("coffe_sales_clean.csv")

def periodo_dia(hora):
    if hora < 12:
        return "Mañana"
    elif hora < 18:
        return "Tarde"
    else:
        return "noche"

dataframe["datetime"] = pd.to_datetime(dataframe["datetime"])

dataframe["periodo"] = dataframe["datetime"].dt.hour.apply(periodo_dia)

# renombramos columnas:
dataframe = dataframe.rename(columns={
    "date" : "fecha",
    "datetime": "fecha_hora",
    "cash_type": "tipo_pago",
    "card": "numero_tarjeta",
    "money": "dinero",
    "coffee_name": "tipo_cafe"
})

print(dataframe["tipo_cafe"].unique())

dataframe["tipo_cafe"] = dataframe["tipo_cafe"].replace({
    "Latte": "Latte",
    "Hot Chocolate": "Chocolate Caliente",
    "Americano": "Americano",
    "Americano with Milk": "Americano con Leche",
    "Cocoa": "Cacao",
    "Cortado": "Cortado",
    "Espresso": "Espresso",
    "Cappuccino": "Capuchino"
})

dataframe["tipo_pago"] = dataframe["tipo_pago"].replace({
    "card": "Tarjeta",
    "cash": "Billete"
})

dataframe.to_csv("dataset_estructurado.csv", index=False)