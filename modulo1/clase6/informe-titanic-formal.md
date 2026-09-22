# Informe de limpieza y análisis del dataset Titanic

## 1. Introducción

El presente trabajo tiene como objetivo preparar y analizar un dataset de pasajeros del Titanic para identificar patrones relevantes en la información disponible. El proceso incluye la limpieza de datos, la imputación de valores faltantes, la eliminación de duplicados y el análisis descriptivo mediante agrupaciones por variables clave.

La base de datos utilizada corresponde al conjunto de pasajeros del Titanic, el cual incluye información demográfica, de tarifa, clase de pasajero, puerto de embarque y estado de supervivencia.

---

## 2. Objetivos

Los objetivos del análisis son los siguientes:

- preparar el dataset para su uso en análisis estadísticos,
- mejorar la calidad de los datos eliminando inconsistencias,
- completar valores faltantes de manera adecuada,
- generar una versión limpia para futuros análisis,
- identificar relaciones relevantes entre clase, edad, tarifa y supervivencia.

---

## 3. Metodología

### 3.1 Carga de datos

Se cargó el archivo CSV con la librería Pandas mediante el siguiente comando:

```python
import pandas as pd

titanic = pd.read_csv("titanic.csv")
```

Esta etapa permitió trabajar con la información en un DataFrame, facilitando la manipulación y análisis posterior.

### 3.2 Eliminación de columnas poco útiles

Se evaluó la variable Cabin, la cual presenta una gran cantidad de valores nulos. Dado que no resulta especialmente útil para un análisis inicial, se decidió eliminarla:

```python
titanic = titanic.drop(columns=["Cabin"])
```

Esta decisión reduce ruido en la base de datos y evita que columnas con alta proporción de datos faltantes distorsionen el análisis.

### 3.3 Imputación de valores faltantes

Se completaron los valores faltantes de la columna Age con el promedio de la edad total:

```python
titanic["Age"] = titanic["Age"].fillna(titanic["Age"].mean())
```

Este procedimiento permite conservar todas las filas del dataset sin perder información útil para el análisis.

En el caso de la columna Embarked, se reemplazaron los null por la etiqueta "Unknown":

```python
titanic["Embarked"] = titanic["Embarked"].fillna("Unknown")
```

Esto permitió mantener la integridad del conjunto sin eliminar registros completos.

### 3.4 Detección y eliminación de duplicados

Se verificó la presencia de registros duplicados con:

```python
print(titanic.duplicated().sum())
```

En caso de existir duplicados, se procedió a eliminarlos:

```python
titanic = titanic.drop_duplicates()
```

La eliminación de duplicados es una etapa indispensable para evitar errores en conteos, promedios y comparaciones.

### 3.5 Exportación del dataset limpio

Una vez realizada la limpieza, el resultado se guardó en un nuevo archivo:

```python
titanic.to_csv("titanic-clean.csv", index=False)
```

De esta forma, se generó una versión reutilizable del dataset para análisis posteriores.

---

## 4. Validación de la limpieza

Se utilizó la siguiente verificación para controlar la calidad del dataset:

```python
print(titanic.isnull().sum())
```

Este chequeo permitió confirmar que los valores faltantes disminuyeron significativamente y que el conjunto quedó en mejor estado para análisis.

---

## 5. Análisis exploratorio y agrupaciones

Una vez finalizada la limpieza, se realizó un análisis descriptivo mediante agrupaciones para resumir información relevante del dataset.

### 5.1 Promedio de edad por clase

```python
dataframe.groupby("Pclass")["Age"].mean()
```

El objetivo fue comparar la edad promedio de los pasajeros según su clase, identificando si existían diferencias relevantes entre primera, segunda y tercera clase.

### 5.2 Tarifa promedio por clase

```python
dataframe.groupby("Pclass")["Fare"].mean()
```

Este análisis permitió observar la diferencia en el costo del pasaje según la categoría socioeconómica del pasajero.

### 5.3 Edad máxima por clase

```python
dataframe.groupby("Pclass")["Age"].max()
```

Con este cálculo se pudo identificar la edad máxima de cada grupo y evaluar la distribución por clase.

### 5.4 Agrupación por clase y género

```python
dataframe.groupby(["Pclass", "Sex"])["Age"].mean()
```

Este análisis permitió estudiar la relación entre clase, género y edad media, aportando una visión más detallada de la composición del pasaje.

### 5.5 Supervivencia por clase

```python
dataframe.groupby("Pclass")["Survived"].sum()
```

Este indicador muestra cuántos pasajeros sobrevivieron en cada categoría de clase.

### 5.6 Proporción de supervivencia por clase

```python
dataframe.groupby("Pclass")["Survived"].mean() * 100
```

Este cálculo permite comparar porcentualmente la tasa de supervivencia de cada clase, una de las preguntas más relevantes del análisis.

### 5.7 Estadísticas múltiples con agg()

```python
dataframe.groupby("Pclass")["Age"].agg(["count", "mean", "max", "min"])
```

La función agg() facilita la obtención de múltiples medidas estadísticas simultáneamente, resultando especialmente útil para resúmenes comparativos.

---

## 6. Resultados esperados y conclusiones preliminares

El análisis realizado permite inferir que la limpieza de datos fue una etapa clave para preparar el dataset y evitar sesgos derivados de valores faltantes o registros duplicados. Asimismo, las agrupaciones realizadas permiten identificar patrones importantes en la distribución de la edad, la tarifa y la supervivencia por clase.

En particular, resulta útil observar:

- la diferencia de tarifa entre clases,
- las diferencias de edad promedio entre grupos,
- la relación entre clase y supervivencia,
- y la posible influencia de género y clase en los resultados finales.

---

## 7. Conclusión

El trabajo desarrollado evidencia un proceso correcto de limpieza y preparación de datos, con un enfoque metodológico sencillo y efectivo para análisis iniciales. La combinación de limpieza, validación y agrupaciones permite convertir un dataset crudo en una base útil para análisis estadísticos y para la elaboración de un informe final con conclusiones claras.

En resumen, la metodología aplicada resulta apropiada para una primera etapa de análisis exploratorio y ofrece una base sólida para continuar con estudios más avanzados, por ejemplo, análisis de correlación, segmentación por edad y gráficos comparativos.

---

## 8. Recomendaciones para continuar

Para fortalecer el informe final, se recomienda continuar con análisis adicionales como:

- supervivencia por sexo y clase,
- tasa de supervivencia según rango etario,
- análisis de correlación entre tarifa y supervivencia,
- comparación de pasajeros con y sin cabina,
- generación de gráficos estadísticos para facilitar la interpretación.

Estos pasos permitirán transformar el análisis básico en una presentación más completa y de mayor valor informativo.
