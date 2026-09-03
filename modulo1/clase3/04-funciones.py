def sumar(num1, num2):
    resultado = num1 + num2
    return resultado

print(sumar(10, 20))

def evaluar_nota(nota):
    if nota >= 6:
        return "Aprobado"
    else:
        return "Desaprobado"

print(evaluar_nota(3))

print(evaluar_nota(5))

print(evaluar_nota(9))

def calcular_total(ventas):
    total = 0
    for venta in ventas:
        total = total + venta
    return total 

print(calcular_total([100, 2000, 300, 400]))