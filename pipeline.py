import sqlite3
from pathlib import Path

from extract.extract_data import extraer_datos
from transform.transform_data import transformar_datos
from load.load_data import cargar_datos
from transform.validar_datos import validar_datos

def main():
    carpeta_proyecto = Path(__file__).resolve().parent
    ruta_original = carpeta_proyecto / "data" / "raw" / "data.csv"
    carpeta_procesados = carpeta_proyecto / "data" / "processed"

    datos = extraer_datos(ruta_original)

    print(
        f"Extracción completada: "
        f"{datos.shape[0]} registros y {datos.shape[1]} columnas."
    )

    datos_limpios, datos_tempranos = transformar_datos(datos)
        # Validar los datos antes de exportarlos y cargarlos.
    resumen = validar_datos(datos, datos_limpios, datos_tempranos)

    print("\nResumen de calidad:")
    print(resumen.to_string(index=False))

    carpeta_procesados.mkdir(parents=True, exist_ok=True)

    resumen.to_csv(
        carpeta_procesados / "resumen_calidad.csv",
        index=False,
        encoding="utf-8"
    )


    datos_limpios.to_csv(
        carpeta_procesados / "data_etl_clean.csv",
        index=False,
        encoding="utf-8",
    )

    datos_tempranos.to_csv(
        carpeta_procesados / "data_prediccion_temprana.csv",
        index=False,
        encoding="utf-8",
    )

    print(
        f"Conjunto completo: "
        f"{datos_limpios.shape[0]} registros y "
        f"{datos_limpios.shape[1]} columnas."
    )

    print(
        f"Conjunto para predicción temprana: "
        f"{datos_tempranos.shape[0]} registros y "
        f"{datos_tempranos.shape[1]} columnas."
    )

    print("Archivos guardados en data/processed.")

        # Cargar los conjuntos preparados en SQLite.
    ruta_bd = carpeta_proyecto / "data" / "estudiantes.db"

    cargar_datos(datos_limpios, datos_tempranos, ruta_bd)

    print("Carga completada en data/estudiantes.db.")

        # Consultar cuántos registros quedaron en cada tabla.
    conexion = sqlite3.connect(ruta_bd)

    try:
        for tabla in [
            "estudiantes_completo",
            "estudiantes_prediccion_temprana"
        ]:
            cantidad = conexion.execute(
                f"SELECT COUNT(*) FROM {tabla}"
            ).fetchone()[0]

            print(f"Tabla {tabla}: {cantidad} registros.")

                    # Consultar la distribucion del resultado academico.
        consulta = """
            SELECT Target, COUNT(*) AS cantidad
            FROM estudiantes_prediccion_temprana
            GROUP BY Target
            ORDER BY cantidad DESC
        """

        resultados = conexion.execute(consulta).fetchall()

        print("\nDistribucion de estudiantes en la base de datos:")

        for categoria, cantidad in resultados:
            print(f"{categoria}: {cantidad}")


    finally:
        conexion.close()


if __name__ == "__main__":
    main()