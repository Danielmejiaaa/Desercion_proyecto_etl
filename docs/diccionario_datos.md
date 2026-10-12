# Diccionario de datos

## Organización

Cada fila representa un estudiante.

La base `data/estudiantes.db` contiene:

- `estudiantes_completo`: 4.424 registros y 37 columnas.
- `estudiantes_prediccion_temprana`: 4.424 registros y 31 columnas.

La segunda tabla excluye las seis variables del segundo semestre.
Conserva 30 variables predictoras y la variable objetivo `Target`.

No se agregó un identificador de estudiante ni se definieron relaciones
entre tablas. Son dos versiones del mismo conjunto de datos.

## Tipos

Los tipos de esta tabla corresponden al almacenamiento en SQLite:

- INTEGER: números enteros, incluidos los códigos categóricos.
- REAL: números decimales.
- TEXT: texto.

En pandas, las variables categóricas se convierten a `category`.
Los CSV no conservan ese tipo: contienen sus valores originales.

## Columnas comunes a ambas tablas

Los ejemplos son ilustrativos y no representan juntos a un estudiante.

| Columna | Tipo SQLite | Descripción | Ejemplo |
|---|---|---|---|
| Marital status | INTEGER | Estado civil codificado. | 1 |
| Application mode | INTEGER | Modalidad de admisión codificada. | 17 |
| Application order | INTEGER | Orden de preferencia de solicitud. | 5 |
| Course | INTEGER | Programa académico codificado. | 171 |
| Daytime/evening attendance | INTEGER | Jornada: 1 diurna; 0 nocturna. | 1 |
| Previous qualification | INTEGER | Formación previa codificada. | 1 |
| Previous qualification (grade) | REAL | Calificación de formación previa. | 122.0 |
| Nacionality | INTEGER | Nacionalidad codificada. | 1 |
| Mother's qualification | INTEGER | Formación de la madre codificada. | 19 |
| Father's qualification | INTEGER | Formación del padre codificada. | 12 |
| Mother's occupation | INTEGER | Ocupación de la madre codificada. | 5 |
| Father's occupation | INTEGER | Ocupación del padre codificada. | 9 |
| Admission grade | REAL | Calificación de admisión. | 126.0 |
| Displaced | INTEGER | Indicador de desplazamiento del estudiante según UCI. | 1 |
| Educational special needs | INTEGER | Indicador de necesidades educativas especiales. | 0 |
| Debtor | INTEGER | Indicador de deuda. | 0 |
| Tuition fees up to date | INTEGER | Indicador de pagos al día. | 1 |
| Gender | INTEGER | Género codificado. | 1 |
| Scholarship holder | INTEGER | Indicador de beca. | 0 |
| Age at enrollment | INTEGER | Edad al ingresar, en años. | 20 |
| International | INTEGER | Indicador de estudiante internacional. | 0 |
| Curricular units 1st sem (credited) | INTEGER | Unidades reconocidas, primer semestre. | 0 |
| Curricular units 1st sem (enrolled) | INTEGER | Unidades matriculadas, primer semestre. | 6 |
| Curricular units 1st sem (evaluations) | INTEGER | Evaluaciones, primer semestre. | 8 |
| Curricular units 1st sem (approved) | INTEGER | Unidades aprobadas, primer semestre. | 5 |
| Curricular units 1st sem (grade) | REAL | Calificación, primer semestre. | 12.5 |
| Curricular units 1st sem (without evaluations) | INTEGER | Unidades sin evaluación, primer semestre. | 0 |
| Unemployment rate | REAL | Tasa de desempleo. | 10.8 |
| Inflation rate | REAL | Tasa de inflación. | 1.4 |
| GDP | REAL | Indicador de PIB. | 1.74 |
| Target | TEXT | Resultado académico: Dropout, Enrolled o Graduate. | Graduate |

## Columnas exclusivas de estudiantes_completo

Se excluyen del conjunto temprano porque corresponden al segundo semestre.

| Columna | Tipo SQLite | Descripción | Ejemplo |
|---|---|---|---|
| Curricular units 2nd sem (credited) | INTEGER | Unidades reconocidas, segundo semestre. | 0 |
| Curricular units 2nd sem (enrolled) | INTEGER | Unidades matriculadas, segundo semestre. | 6 |
| Curricular units 2nd sem (evaluations) | INTEGER | Evaluaciones, segundo semestre. | 10 |
| Curricular units 2nd sem (approved) | INTEGER | Unidades aprobadas, segundo semestre. | 5 |
| Curricular units 2nd sem (grade) | REAL | Calificación, segundo semestre. | 12.4 |
| Curricular units 2nd sem (without evaluations) | INTEGER | Unidades sin evaluación, segundo semestre. | 0 |

## Interpretación y conservación de valores

- Los códigos categóricos se conservan: un código mayor no implica
  una cantidad mayor.
- Se conserva el nombre original `Nacionality`.
- Se eliminan espacios y tabulaciones en los extremos de los encabezados.
- Los ceros se conservan; no se convierten automáticamente en valores nulos.
- `Target` es el resultado que se desea analizar, no una variable predictora.
- El significado detallado de los códigos debe consultarse en el
  catálogo de variables de UCI enlazado abajo.

## Fuente

[UCI — Predict Students' Dropout and Academic Success](https://archive.ics.uci.edu/dataset/697/predict+students+dropout+and+academic+success)