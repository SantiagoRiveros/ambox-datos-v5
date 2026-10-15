-- creamos la tabla
CREATE TABLE ventas (
	id INTEGER PRIMARY KEY,
  	producto TEXT NOT NULL,
  	categoria TEXT NOT NULL,
  	vendedor TEXT NOT NULL,
  	cantidad INTEGER NOT NULL,
  	precio_UNITARIO REAL NOT NULL
);

DROP TABLE ventas;

INSERT INTO ventas
    (id, producto, categoria, vendedor, cantidad, precio_unitario)
VALUES
    (1, 'Teclado', 'Perifericos', 'Ana', 3, 15000),
    (2, 'Mouse', 'Perifericos', 'Luis', 5, 8000),
    (3, 'Monitor', 'Pantallas', 'Ana', 2, 120000),
    (4, 'Notebook', 'Computadoras', 'Pedro', 1, 750000),
    (5, 'Mouse', 'Perifericos', 'Ana', 4, 8000),
    (6, 'Monitor', 'Pantallas', 'Luis', 3, 120000),
    (7, 'Teclado', 'Perifericos', 'Pedro', 2, 15000),
    (8, 'Notebook', 'Computadoras', 'Ana', 2, 750000),
    (9, 'Tablet', 'Computadoras', 'Luis', 3, 200000),
    (10, 'Tablet', 'Computadoras', 'Pedro', 2, 200000),
    (11, 'Monitor', 'Pantallas', 'Pedro', 1, 120000),
    (12, 'Mouse', 'Perifericos', 'Luis', 2, 8000);

-- SUM(): calcular totales: 

-- Saber el total de cantidades vendidas:
SELECT SUM(cantidad) AS unidades_vendidas
FROM ventas;

-- Calculemos la facturacion total,
SELECT SUM(cantidad * precio_unitario) AS facturacion_total
FROM ventas;

-- Calculamos promedio de venta de unidades por venta 
SELECT AVG(cantidad) AS promedio_unidades
FROM ventas;

-- calcular precio unitario promedio de los registros 
SELECT AVG(precio_unitario) AS precio_promedio
FROM ventas;

--Calcular cantidad de registros: 
SELECT COUNT(*) AS total_ventas
FROM ventas;

--Precio mas bajo: 
SELECT MIN(precio_unitario) AS precio_minimo
FROM ventas;

--Precio mas alto
SELECT MAX(precio_unitario) AS precio_maximo
FROM ventas;

CREATE TABLE vendedores(
	id INTEGER PRIMARY KEY,
  	nombre TEXT NOT NULL,
  	edad INTEGER,
  	ciudad TEXT
);

INSERT INTO vendedores(id, nombre, edad, ciudad)
VALUES
	(1, 'Ana', 28, 'Berazategui'),
    (2, 'Luis', 35, 'Quilmes'),
    (3, 'Pedro', 31, 'Avellaneda');
    
    
 -- Ejemplo 1, unidades vendidas por vendedor: 
SELECT vendedor, SUM(cantidad) AS unidades_vendidas
FROM ventas
GROUP BY vendedor
ORDER BY unidades_vendidas DESC;

-- EJEMPLO 2: facturacion por vendedor 
SELECT
	vendedor,
    SUM(cantidad * precio_unitario) AS facturacion
FROM ventas
GROUP BY vendedor
ORDER BY facturacion DESC;

-- EJEMPLO 3: facturacion por categori
SELECT
	categoria,
    SUM(cantidad * precio_unitario) AS facturacion
FROM ventas
GROUP BY categoria;

-- EJEMPLO 4: cantidad de registros por producto:
SELECT
	producto,
    COUNT(*) AS cantidad_registros
FROM ventas
GROUP BY producto;

-- ejemplo 5: unidades vendidas por producto
SELECT
	producto,
    SUM(cantidad) AS unidades_vendidas
FROM ventas
GROUP BY producto
order BY unidades_vendidas DESC;

-- Ejemplo 6: Varias agregaciopnes por categoria:
SELECT
	categoria,
    COUNT(*) AS operaciones,
    SUM(cantidad) as unidades,
    AVG(precio_unitario) AS precio_promedio,
    MIN(precio_unitario) AS precio_minimo,
    MAX(precio_unitario) AS precio_maximo
FROM ventas
GROUP BY categoria;

-- HAVING
-- Ejemplo 1. Vendedores con facturación superior a $1.200.000
SELECT
	vendedor,
    SUM(cantidad * precio_unitario) AS facturacion
FROM ventas
GROUP BY vendedor
HAVING SUM(cantidad * precio_unitario) > 1200000;

-- Ejemplo 2: Categorias con mas de 5 unidades vendidas
SELECT categoria, SUM(cantidad) AS unidades_vendidas
FROM ventas
GROUP BY categoria
HAVING SUM(cantidad) > 5;

-- EJEMPLO 3: Productos presentes en mas de dos registros
SELECT
    producto,
    COUNT(*) AS cantidad_registros
FROM ventas
GROUP BY producto
HAVING COUNT(*) > 2;

-- Ejemplo 4: vendedores con promedio superior a 2 unidades
SELECT
	vendedor,
    AVG(cantidad) AS promedio_unidades
FROM ventas
GROUP BY vendedor
HAVING AVG(cantidad) > 2;