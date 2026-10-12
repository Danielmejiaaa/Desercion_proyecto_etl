from pathlib import Path

import pandas as pd


def extraer_datos(ruta_archivo: Path) -> pd.DataFrame:
    """Lee el CSV original sin modificarlo."""
    return pd.read_csv(ruta_archivo, sep=";")