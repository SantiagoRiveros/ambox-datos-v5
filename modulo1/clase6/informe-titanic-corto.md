# Informe del análisis del dataset Titanic

## Introducción

En este trabajo se realizó la limpieza y el análisis exploratorio del dataset Titanic con el objetivo de preparar la información para su posterior interpretación. La base original contenía valores faltantes, columnas poco útiles y registros duplicados, por lo que fue necesario limpiar la información antes de realizar agrupaciones y cálculos estadísticos.

## Objetivo

El objetivo principal fue obtener una versión ordenada y útil del dataset para estudiar variables como la edad, la clase del pasajero, la tarifa y la supervivencia.

## Proceso de limpieza

Se cargó el dataset con Pandas y se eliminó la columna Cabin, ya que presentaba muchos valores nulos y no aportaba información relevante para un análisis inicial.

Posteriormente, se completaron los valores faltantes de la columna Age con el promedio de la edad del conjunto, y los valores nulos de Embarked se reemplazaron por "Unknown" para conservar la información sin perder filas.

También se verificaron los duplicados y, de existir, se eliminaron para evitar resultados distorsionados en los cálculos.

Finalmente, se guardó la versión limpia del dataset en un archivo llamado "titanic-clean.csv".

## Análisis realizado

A partir del dataset limpio, se realizaron agrupaciones para responder preguntas clave sobre la información:

- promedio de edad por clase,
- tarifa promedio por clase,
- edad máxima por clase,
- promedio de edad según clase y género,
- supervivencia por clase,
- proporción de supervivencia por clase,
- estadísticas resumidas con agg().

Estas operaciones permitieron comparar cómo se comportan las variables principales y observar posibles diferencias entre grupos.

## Conclusión

La limpieza del dataset fue una etapa necesaria para garantizar la calidad de los análisis. Una vez preparado el archivo, se pudieron hacer agrupaciones y cálculos que ayudaron a interpretar mejor la información disponible. El análisis permitió identificar patrones relevantes relacionados con la clase del pasajero, la edad, la tarifa y la supervivencia.

En conclusión, el proceso realizado resulta adecuado para un primer análisis exploratorio y sirve como base para continuar con estudios más profundos sobre los factores que influyeron en la supervivencia de los pasajeros del Titanic.
