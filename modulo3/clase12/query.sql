-- Creacion de una base de datos
-- CREATE DATABASE nombre_de_la_base 

-- Crear una tabla. 
CREATE TABLE clientes(
	id INT PRIMARY KEY,
  	nombre VARCHAR(100),
  	edad INT,
  	ciudad VARCHAR(100)
 );
 
 -- Vamos a insertar datos en clientes 
 INSERT INTO clientes(id, nombre, edad, ciudad)
 VALUES 
 (1, 'Juan', 25, 'Buenos Aires'),
 (2, 'Armando', 41, 'Rosario'),
 (3, 'Carlos', 29, 'Trelew'),
 (4, 'Santiago', 33, 'Berazategui'),
 (5, 'Fernanda', 19, 'Posadas');
 
 -- COMO PUEDO VER LOS DATOS? 
 -- Hay 4 operaciones basicas de query: Leer, escribir, editar, y eliminar
 -- CRUD (Create, Read, Update, Delete)
 SELECT * FROM clientes;
 -- * significa TODOS
 
 SELECT nombre, ciudad FROM clientes;
 
 -- Nosotros podemos condicionar los datos que traemos.
 -- Que pasa si quiero ver clientes mayores o iguales a 25 años? 
 SELECT * FROM clientes
 WHERE edad >= 25;
 
 -- Yo puedo concatenar y juntar varias condiciones: 
 SELECT * FROM clientes 
 WHERE edad >= 20 AND edad <= 40;
 
 -- Quiero traer a todos los clientes MENOS los de "Berazategui" 
 SELECT * FROM clientes
 WHERE ciudad <> 'Berazategui';
 
 -- Quiero clientes SOLO de Rosario 
 SELECT * FROM clientes 
 WHERE ciudad = 'Rosario';
 
 -- Quiero clientes de rosario o berazategui 
 SELECT * FROM clientes 
 WHERE ciudad = 'Rosario' or ciudad = 'Berazategui';
 
 -- Creamos tabla productos 
 CREATE TABLE productos (
   id INT PRIMARY KEY,
   nombre VARCHAR(100),
   categoria VARCHAR(50),
   precio DECIMAL(10, 2),
   stock INT
 );
 
 INSERT INTO productos (id, nombre, categoria, precio, stock)
 VALUES
(1, 'Teclado', 'Perifericos', 45000, 10),
(2, 'Mouse', 'Perifericos', 25000, 20),
(3, 'Monitor', 'Pantallas', 180000, 5),
(4, 'Notebook', 'Computadoras', 850000, 3),
(5, 'Auriculares', 'Audio', 60000, 15),
(6, 'Webcam', 'Perifericos', 55000, 8),
(7, 'Parlantes', 'Audio', 90000, 6),
(8, 'Tablet', 'Computadoras', 350000, 4);

-- Ejercicio 1 - Mostrar todos los productos:
SELECT * FROM productos;

-- Ejercicio 2 - Mostrar solamente nombre y precio:
SELECT nombre, precio FROM productos;

-- Ejercicio 3 - Mostrar todos los productos que cuestan mas de 100.000 
SELECT *
FROM productos
WHERE precio > 100000;

-- Ejercicio 4 - Mostrar productos con stock menor a 10: 
SELECT * 
FROM productos
WHERE stock < 10;

-- Ejercicio 5 - Mostrar productos de la categoria Perifericos: 
SELECT *
FROM productos
WHERE categoria = 'Perifericos';

-- Ejercicio 6 - Mostrar productos cuyo precio sea menor o igual a 60.000
SELECT *
FROM productos
WHERE precio <= 60000;

-- Ejercicio 7 - Mostrar productos de categoria Audio:
SELECT *
FROM productos
WHERE categoria = 'Audio';

-- Ejercicio 8 - Mostrar productos que cuesten mas de 50.000 y stock menor a 10
SELECT *
FROM productos
WHERE precio > 50000
AND stock < 10;