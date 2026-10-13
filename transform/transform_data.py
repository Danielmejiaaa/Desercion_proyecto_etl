import pandas as pd


def transformar_datos(
    datos: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Prepara el conjunto completo y el de predicción temprana."""
    datos_limpios = datos.copy()

    # Eliminar espacios y tabulaciones en los extremos de los nombres.
    datos_limpios.columns = datos_limpios.columns.str.strip()

    # Estos valores representan categorías, no cantidades.
    columnas_categoricas = [
        "Marital status",
        "Application mode",
        "Course",
        "Daytime/evening attendance",
        "Previous qualification",
        "Nacionality",
        "Mother's qualification",
        "Father's qualification",
        "Mother's occupation",
        "Father's occupation",
        "Displaced",
        "Educational special needs",
        "Debtor",
        "Tuition fees up to date",
        "Gender",
        "Scholarship holder",
        "International",
        "Target",
    ]

    for columna in columnas_categoricas:
        datos_limpios[columna] = datos_limpios[columna].astype("category")

    # Excluir información posterior al momento de predicción.
    columnas_segundo_semestre = [
        "Curricular units 2nd sem (credited)",
        "Curricular units 2nd sem (enrolled)",
        "Curricular units 2nd sem (evaluations)",
        "Curricular units 2nd sem (approved)",
        "Curricular units 2nd sem (grade)",
        "Curricular units 2nd sem (without evaluations)",
    ]

    datos_tempranos = datos_limpios.drop(
        columns=columnas_segundo_semestre
    )

    return datos_limpios, datos_tempranos