contador = 0

while contador < 5:
    print(contador)
    contador = contador + 1

password = ""
while password != "python123":
    if password.upper() == "SALIR":
        break
    password = input("Ingrese la contraseña o escriba SALIR: ")

print("acceso permitido")