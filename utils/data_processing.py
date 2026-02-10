from __future__ import annotations

import io
from typing import Iterable

import numpy as np
import pandas as pd


def read_csv(uploaded_file) -> pd.DataFrame:
    data = uploaded_file.read()
    buffer = io.BytesIO(data)
    try:
        return pd.read_csv(buffer, encoding="utf-8")
    except UnicodeDecodeError:
        buffer.seek(0)
        return pd.read_csv(buffer, encoding="latin-1")


def basic_quality_report(df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame(
        {
            "missing": df.isna().sum(),
            "missing_pct": (df.isna().mean() * 100).round(2),
            "dtype": df.dtypes.astype(str),
        }
    ).reset_index(names="column")


def apply_numeric_imputation(
    df: pd.DataFrame,
    columns: Iterable[str],
    method: str,
) -> pd.DataFrame:
    out = df.copy()
    if method == "Media":
        fill_values = out[list(columns)].mean(numeric_only=True)
    elif method == "Mediana":
        fill_values = out[list(columns)].median(numeric_only=True)
    else:
        fill_values = 0
    out[list(columns)] = out[list(columns)].fillna(fill_values)
    return out


def handle_outliers_iqr(
    df: pd.DataFrame,
    columns: Iterable[str],
    strategy: str,
) -> pd.DataFrame:
    out = df.copy()
    if not columns:
        return out

    q1 = out[list(columns)].quantile(0.25)
    q3 = out[list(columns)].quantile(0.75)
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr

    if strategy == "Eliminar filas":
        mask = np.ones(len(out), dtype=bool)
        for col in columns:
            mask &= out[col].between(lower[col], upper[col], inclusive="both")
        out = out.loc[mask].reset_index(drop=True)
    else:
        out[list(columns)] = out[list(columns)].clip(lower=lower, upper=upper, axis=1)
    return out


def add_calculated_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Agrega columnas calculadas derivadas de columnas existentes.
    
    - Ticket Promedio: Sales / Quantity
    - Margen Ganancia (%): (Profit / Sales) * 100
    - Descuento Dinero: Sales * Discount
    """
    out = df.copy()
    
    # Ticket Promedio = Ventas / Cantidad
    if "Sales" in out.columns and "Quantity" in out.columns:
        out["Ticket Promedio"] = (out["Sales"] / out["Quantity"]).round(2)
    
    # Margen de Ganancia (%) = (Ganancia / Ventas) * 100
    if "Profit" in out.columns and "Sales" in out.columns:
        out["Margen Ganancia (%)"] = (
            (out["Profit"] / out["Sales"] * 100)
            .replace([np.inf, -np.inf], 0)
            .fillna(0)
            .round(2)
        )
    
    # Descuento en Dinero = Ventas * Descuento
    if "Sales" in out.columns and "Discount" in out.columns:
        out["Descuento Dinero"] = (out["Sales"] * out["Discount"]).round(2)
    
    return out
