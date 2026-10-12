import pandas as pd


def validar_datos(df, df_etl, df_prediccion):
    # Comparar el conjunto original con los conjuntos preparados.
    resumen = pd.DataFrame({
        "Verificacion": [
            "Numero de registros",
            "Numero de columnas",
            "Valores nulos",
            "Registros duplicados"
        ],
        "Original": [
            df.shape[0],
            df.shape[1],
            df.isnull().sum().sum(),
            df.duplicated().sum()
        ],
        "ETL completo": [
            df_etl.shape[0],
            df_etl.shape[1],
            df_etl.isnull().sum().sum(),
            df_etl.duplicated().sum()
        ],
        "Prediccion temprana": [
            df_prediccion.shape[0],
            df_prediccion.shape[1],
            df_prediccion.isnull().sum().sum(),
            df_prediccion.duplicated().sum()
        ]
    })

    # Comprobar que se conservaron los registros.
    if not (len(df) == len(df_etl) == len(df_prediccion)):
        raise ValueError("El numero de registros cambio durante el proceso.")

    # Comprobar las categorias de la variable objetivo.
    categorias_validas = {"Graduate", "Dropout", "Enrolled"}

    if not df_etl["Target"].isin(categorias_validas).all():
        raise ValueError("Target contiene valores nulos o categorias no validas.")

    # Las cantidades de unidades curriculares no pueden ser negativas.
    columnas_cantidades = [
        columna for columna in df_etl.columns
        if columna.startswith("Curricular units")
        and "(grade)" not in columna
    ]

    if not df_etl[columnas_cantidades].ge(0).all().all():
        raise ValueError("Hay cantidades de unidades curriculares no validas.")

    # No debe quedar informacion del segundo semestre.
    if any("2nd sem" in columna for columna in df_prediccion.columns):
        raise ValueError("El conjunto temprano conserva columnas del segundo semestre.")

    return resumen