import sqlite3


def cargar_datos(df_etl, df_prediccion, ruta_bd):
    # Conectar a la base de datos. Si no existe, se crea.
    conexion = sqlite3.connect(ruta_bd)

    try:
        # Guardar los conjuntos como tablas.
        df_etl.to_sql(
            "estudiantes_completo",
            conexion,
            if_exists="replace",
            index=False
        )

        df_prediccion.to_sql(
            "estudiantes_prediccion_temprana",
            conexion,
            if_exists="replace",
            index=False
        )
    finally:
        conexion.close()