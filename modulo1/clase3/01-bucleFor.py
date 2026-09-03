for numero in range(5):
    print(numero)

print("---------------------")

edades = [18, 25, 31, 42, 19]

for edad in edades:
    print(edad)

print("---------------------")

ventas = [1200, 500, 3000, 600, 4500]
acumuladorVentas = 0

for venta in ventas:
    acumuladorVentas = acumuladorVentas + venta

print("Total Ventas:", acumuladorVentas)
print("Promedio de ventas:", acumuladorVentas / len(ventas))

for venta in ventas:
    if venta >= 1000:
        print("Venta importante:", venta)