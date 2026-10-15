import pandas as pd

dataframe = pd.read_csv("dataset_estructurado.csv")

# Cuanto vendimos?

print("Cantidad total de ventas")
print(dataframe["dinero"].sum())

print("Promedio por venta")
print(dataframe["dinero"].mean())

print("Ventas mas alta")
print(dataframe["dinero"].max())

print("Ventas mas baja")
print(dataframe["dinero"].min())

# Que cafe vende mas?

print("Que cafe vende mas:")
print(dataframe["tipo_cafe"].value_counts())

""" 
Americano con Leche    824
Latte                  782
Americano              578
Capuchino              501
Cortado                292
Chocolate Caliente     282
Cacao                  243
Espresso               134
 """

# Cual cafe genera mas dinero?

print("Cual cafe genera mas dinero?")
print(dataframe.groupby("tipo_cafe")["dinero"].sum().sort_values(ascending=False))

""" 
tipo_cafe
Latte                  27866.30
Americano con Leche    25269.12
Capuchino              18034.14
Americano              15062.26
Chocolate Caliente     10172.46
Cacao                   8678.16
Cortado                 7534.86
Espresso                2814.28
 """

# Cuanto gasta en promedio cada cliente por tipo de cafe
print("Cuanto gasta en promedio cada cliente por tipo de cafe")

print(dataframe.groupby("tipo_cafe")["dinero"].mean().sort_values(ascending=False))

""" 
tipo_cafe
Chocolate Caliente     36.072553
Capuchino              35.996287
Cacao                  35.712593
Latte                  35.634655
Americano con Leche    30.666408
Americano              26.059273
Cortado                25.804315
Espresso               21.002090
 """

# Como pagan los clientes?
print("Como pagan los clientes?")
print(dataframe.groupby("tipo_pago")["dinero"].agg(["count", "sum", "mean"]))
""" 
           count        sum       mean
tipo_pago                             
Billete       89    3186.00  35.797753
Tarjeta     3547  112245.58  31.645216
"""

# Cuando vende mas la cafeteria?
print("Cuando vende mas la cafeteria?")
print(dataframe.groupby("periodo")["dinero"].agg(["count", "sum", "mean"]))

""" 
         count       sum       mean
periodo                            
Mañana    1221  37380.20  30.614414
Tarde     1476  46978.80  31.828455
noche      939  31072.58  33.091140
 """

dataframe["fecha"] = pd.to_datetime(dataframe["fecha"])

# Facturacion diaria:
print("Facturacion diaria")
print(dataframe.groupby("fecha")["dinero"].sum().sort_values(ascending=False))

""" 
fecha
2024-10-11    836.66
2025-02-03    796.00
2025-02-05    760.24
2025-03-03    737.72
2024-10-17    726.46
               ...  
2024-07-15     32.82
2024-08-27     32.82
2024-07-17     27.92
2025-01-06     25.96
2024-08-29     23.02
"""

# Que cliente compra mas:
print("Top 10 clientes")
print(dataframe["numero_tarjeta"].value_counts().head(10))

# Quienes gastan mas:
print("Quienes gastan mas:")
print(dataframe.groupby(
    "numero_tarjeta"
)["dinero"].sum().sort_values(ascending=False))

# Que cafe se vende en cada periodo?
print("Que cafe se vende en cada periodo?")
print(dataframe.groupby(["periodo", "tipo_cafe"]).size())

""" 
Mañana   Americano              225
         Americano con Leche    336
         Cacao                   59
         Capuchino              126
         Chocolate Caliente      50
         Cortado                145
         Espresso                46
         Latte                  234
Tarde    Americano              275
         Americano con Leche    296
         Cacao                   95
         Capuchino              206
         Chocolate Caliente     110
         Cortado                103
         Espresso                68
         Latte                  323
noche    Americano               78
         Americano con Leche    192
         Cacao                   89
         Capuchino              169
         Chocolate Caliente     122
         Cortado                 44
         Espresso                20
         Latte                  225
 """