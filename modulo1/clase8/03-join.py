import pandas as pd

empleados = pd.read_csv("./csv/empleados.csv")
departamentos = pd.read_csv("./csv/departamentos.csv")

# Preparamos los indices:
empleados = empleados.set_index("departamento_id")
departamentos = departamentos.set_index("departamento_id")

print(empleados)
print(departamentos)

# Hagamos el JOIN

resultado = empleados.join(
    departamentos,
    lsuffix="_empleado", 
    rsuffix="_departamento"
)

print(resultado)