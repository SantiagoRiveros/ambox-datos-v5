# Documentación del proceso de limpieza y análisis del dataset Titanic

## 1. Objetivo

El objetivo de este trabajo fue preparar el dataset de Titanic para su posterior análisis estadístico y de agrupación. Se buscó:

- eliminar columnas que no aportan valor al análisis inicial,
- completar valores faltantes,
- eliminar duplicados,
- guardar una versión limpia del dataset para usar en análisis posteriores.

---

## 2. Fuente de datos

Se utilizó el archivo:

- titanic.csv

Este conjunto contiene información de pasajeros del Titanic, como:

- PassengerId
- Pclass
- Name
- Sex
- Age
- SibSp
- Parch
- Ticket
- Fare
- Cabin
- Embarked
- Survived

---

## 3. Proceso de limpieza realizado

### 3.1 Carga del dataset

Se cargó el archivo con Pandas:

```python
import pandas as pd

titanic = pd.read_csv("titanic.csv")
```

Esto permite trabajar con la información en forma de DataFrame y aplicar operaciones de limpieza y análisis.

### 3.2 Eliminación de la columna Cabin

Se decidió eliminar la columna Cabin porque suele tener muchos valores nulos y, en un análisis inicial, no siempre aporta información útil.

```python
titanic = titanic.drop(columns=["Cabin"])
```

Esto reduce el ruido del dataset y facilita el análisis posterior.

### 3.3 Completar edades faltantes con la media

Se reemplazaron los valores nulos de la columna Age por el promedio de la edad del conjunto.

```python
titanic["Age"] = titanic["Age"].fillna(titanic["Age"].mean())
```

Esto permite conservar las filas que no tenían valor en esa columna sin perder información.

### 3.4 Completar puerto de embarque faltante

Para la columna Embarked, se rellenaron los valores nulos con la palabra "Unknown".

```python
titanic["Embarked"] = titanic["Embarked"].fillna("Unknown")
```

Esto es útil cuando el dato faltante representa una categoría relevante y no es posible inferirlo con precisión.

### 3.5 Detección de duplicados

Se verificó la cantidad de filas duplicadas:

```python
print(titanic.duplicated().sum())
```

Si existieran duplicados, se eliminaban con:

```python
titanic = titanic.drop_duplicates()
```

Esto ayuda a evitar resultados engañosos en conteos, promedios y agrupaciones.

### 3.6 Guardado del dataset limpio

Finalmente, se exportó la versión procesada a un nuevo archivo CSV:

```python
titanic.to_csv("titanic-clean.csv", index=False)
```

Esto deja una base de datos lista para ser reutilizada en análisis posteriores.

---

## 4. Validación de la limpieza

Durante el proceso se utilizó:

```python
print(titanic.isnull().sum())
```

Esto permite revisar cuántos valores nulos quedaron en cada columna después de la limpieza. Es una comprobación importante para validar que el proceso fue correcto.

---

## 5. Análisis posterior realizado: agrupaciones

Además de la limpieza, se realizaron análisis de agrupación para extraer información útil del dataset. Por ejemplo:

### 5.1 Promedio de edad por clase

```python
dataframe.groupby("Pclass")["Age"].mean()
```

Esto permite comparar la edad promedio de los pasajeros según su clase.

### 5.2 Tarifa promedio por clase

```python
dataframe.groupby("Pclass")["Fare"].mean()
```

Muestra cómo varía el costo del pasaje según la clase.

### 5.3 Proporción de supervivencia por clase

```python
dataframe.groupby("Pclass")["Survived"].mean() * 100
```

Este cálculo permite observar la tasa de supervivencia según la clase del pasajero.

### 5.4 Agrupación por clase y género

```python
dataframe.groupby(["Pclass", "Sex"])["Age"].mean()
```

Esto permite analizar si la edad promedio difiere según la combinación de clase y género.

### 5.5 Estadísticas múltiples con agg()

```python
dataframe.groupby("Pclass")["Age"].agg(["count", "mean", "max", "min"])
```

Este tipo de operación permite resumir varios indicadores al mismo tiempo.

---

## 6. Conclusión

El proceso realizado tiene sentido dentro de un flujo básico de análisis de datos:

1. Se cargó el dataset.
2. Se eliminaron columnas con poco valor o muchas nulas.
3. Se completaron valores faltantes de forma razonable.
4. Se revisaron duplicados.
5. Se generó una versión limpia lista para análisis.
6. Luego se aplicaron agrupaciones para extraer patrones relevantes.

Este enfoque es ideal como base para un informe final, ya que permite pasar de datos crudos a información resumida y comprensible.

---

## 7. Recomendaciones para continuar

Para sumar valor al informe final, se pueden hacer análisis adicionales como:

- supervivencia por sexo y clase,
- edad por rango,
- tarifa promedio según supervivencia,
- distribución de pasajeros por clase,
- comparación entre viajeros con cabina y sin cabina,
- gráficos de barras y torta para visualizar hallazgos.

---

## 8. Resultado esperado

La base de trabajo queda lista para realizar un análisis más profundo y presentar conclusiones claras sobre:

- quiénes viajaban en el Titanic,
- cuántos sobrevivieron,
- qué factores estuvieron asociados con la supervivencia,
- y cómo se comportan las variables clave del dataset.
