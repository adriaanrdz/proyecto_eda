# Proyecto EDA de Freelancers

Este proyecto contiene un análisis exploratorio de un dataset de freelancers, incluyendo limpieza de datos, visualizaciones y conclusiones exploratorias.

---

## 1. Estructura del proyecto
```
proyecto_eda/
│
├── data/ ← CSVs originales y limpios
│ ├── dataset_original.csv
│ └── dataset_limpio.csv
│
├── notebooks/ ← Notebooks de análisis
│ ├── exploracion.ipynb
│ ├── limpieza.ipynb
│ └── eda.ipynb
│
├── src/ ← Funciones y módulos Python
│ ├── __init__.py
│ └── funciones_limpieza.py
│
├── .gitignore ← Archivos y carpetas a ignorar por Git
└── README.md
```
---

## 2. Objetivo

El objetivo de este proyecto es:

- Analizar las características principales de los freelancers en el dataset.
- Detectar valores nulos, inconsistencias y outliers.
- Visualizar patrones relevantes para entender la distribución de variables numéricas y categóricas.
- Presentar conclusiones exploratorias basadas en los datos limpios.

---

## 3. Descripción del dataset

- **Número de filas:** 1000  
- **Columnas del dataset:**
  - `freelancer_id` : identificador único del freelancer  
  - `name` : nombre del freelancer
  - `age` : edad del freelancer
  - `gender` : género  
  - `country` : país de procedencia del freelancer
  - `language` : idioma principal del freelancer  
  - `years_of_experience` : años de experiencia  
  - `hourly_rate` : tarifa por hora en USD  
  - `primary_skill` : habilidad principal  
  - `rating` : calificación obtenida por el freelancer  
  - `client_satisfaction` : satisfacción del cliente  
  - `is_active` : indica si el freelancer está activo  

---

## 4. Limpieza de datos

Durante la limpieza se realizaron los siguientes pasos:

- Normalización de nombres de columnas (`lowercase`, renombrar columnas complejas).
- Limpieza y estandarización de valores categóricos (`gender`, `primary_skill`).
- Limpieza de valores mixtos en columnas numéricas (`hourly_rate`, `client_satisfaction`).
- Imputación de valores nulos solo en columnas objetivas (`age`), usando mediana.
- Conversión de tipos numéricos (`int64` para edad).
- Conservación de valores subjetivos (`rating`, `client_satisfaction`) y económicos (`hourly_rate`) sin imputar para no sesgar el análisis.

---

## 5. Visualizaciones

Se generaron las siguientes visualizaciones para explorar los datos:

1. **Histograma de años de experiencia:** para analizar la distribución de la experiencia.
2. **Barplot de `primary_skill`:** para identificar los trabajos más frecuentes.
3. **Countplot de `primary_skill` por `gender`:** para ver diferencias entre hombres y mujeres en cada habilidad.
4. **Scatterplot de `years_of_experience` vs `rating`:** para analizar la relación entre experiencia y desempeño.
5. **Boxplot de `hourly_rate` por `country`:** para observar la variación de tarifas y detectar outliers.

---

## 6. Conclusiones exploratorias

- La mayoría de freelancers tiene poca experiencia, aunque eso no es una barrera para obtener buenos ratings. Con esto vemos que no es tan importante los años de experiencia como la habilidad y el talento del freelancer (freelancers con poca experiencia y ratings altos) 
- En general, cuando analizamos la cantidad de hombres y mujeres que hay por profesión, tenemos una proporción equilibrada, aunque hay algunas que destacan uno sobre el otro (ej. Mobile Apps con más mujeres).  
- El precio/h varían significativamente según el país, con presencia de outliers.  
- La limpieza y normalización permiten un análisis más robusto y coherente.