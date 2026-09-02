producto1 = {
    "nombre" : "Mesa",
    "precio" : 10000,
    "categoria": "Muebles",
    "stock": 13
}

producto2 = {
    "nombre" : "TV",
    "precio" : 1000000,
    "categoria": "Electronica",
    "stock": 4
}

producto3 = {
    "nombre" : "Ventana",
    "precio" : 25000,
    "categoria": "Hogar",
    "stock": 2
}

print(producto1["nombre"])
print(producto1["precio"])
producto1["stock"] = 3
producto1["descuento"] = 0

print(producto1)

listaProductos = [producto1, producto2, producto3]