import pandas as pd
import numpy as np
from utils.eda_helpers import classify_price_segments

def compute_eda_kpis(df: pd.DataFrame, target_col: str = "price") -> dict:
    """
    Computes key EDA statistics including mean, median, min, max, std, and top correlation.
    """
    if target_col not in df.columns or not pd.api.types.is_numeric_dtype(df[target_col]):
        return {
            "mean_price": 0.0,
            "median_price": 0.0,
            "min_price": 0.0,
            "max_price": 0.0,
            "std_price": 0.0,
            "avg_area": 0.0,
            "top_corr_col": "None",
            "top_corr_val": "+0.00"
        }

    target = df[target_col]
    mean_val = float(target.mean())
    median_val = float(target.median())
    min_val = float(target.min())
    max_val = float(target.max())
    std_val = float(target.std())

    avg_area = float(df["area"].mean()) if "area" in df.columns and pd.api.types.is_numeric_dtype(df["area"]) else 0.0

    # Top numeric correlation with target
    num_df = df.select_dtypes(include=[np.number])
    if target_col in num_df.columns and len(num_df.columns) > 1:
        corr_series = num_df.corr()[target_col].drop(target_col).abs().sort_values(ascending=False)
        if not corr_series.empty:
            top_col = corr_series.index[0]
            top_val = num_df.corr().loc[target_col, top_col]
            top_corr_str = f"{top_val:+.2f}"
        else:
            top_col = "None"
            top_corr_str = "+0.00"
    else:
        top_col = "None"
        top_corr_str = "+0.00"

    return {
        "mean_price": mean_val,
        "median_price": median_val,
        "min_price": min_val,
        "max_price": max_val,
        "std_price": std_val,
        "avg_area": avg_area,
        "top_corr_col": top_col,
        "top_corr_val": top_corr_str
    }

def segment_housing_data(df: pd.DataFrame, target_col: str = "price") -> pd.DataFrame:
    """
    Wrapper function to segment housing dataset by price quantiles.
    """
    return classify_price_segments(df, target_col)
