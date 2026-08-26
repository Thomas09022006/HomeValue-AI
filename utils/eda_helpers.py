import numpy as np
import pandas as pd
import streamlit as st

def calculate_iqr_outliers(series: pd.Series) -> dict:
    """
    Calculates outlier count and percentage using Interquartile Range (IQR) method.
    """
    clean_series = series.dropna()
    if clean_series.empty:
        return {"outliers_count": 0, "outliers_pct": 0.0, "lower_bound": 0, "upper_bound": 0}
        
    q25 = clean_series.quantile(0.25)
    q75 = clean_series.quantile(0.75)
    iqr = q75 - q25
    
    lower_bound = q25 - 1.5 * iqr
    upper_bound = q75 + 1.5 * iqr
    
    outliers = clean_series[(clean_series < lower_bound) | (clean_series > upper_bound)]
    outliers_count = len(outliers)
    outliers_pct = round((outliers_count / len(clean_series)) * 100, 2)
    
    return {
        "outliers_count": outliers_count,
        "outliers_pct": outliers_pct,
        "lower_bound": round(lower_bound, 2),
        "upper_bound": round(upper_bound, 2)
    }

def classify_price_segments(df: pd.DataFrame, price_col: str = "price") -> pd.DataFrame:
    """
    Classifies properties into Budget, Mid-Range, Premium, and Luxury price segments.
    """
    if price_col not in df.columns or not pd.api.types.is_numeric_dtype(df[price_col]):
        df_copy = df.copy()
        df_copy["Price_Segment"] = "Standard"
        return df_copy
        
    df_copy = df.copy()
    q25 = df_copy[price_col].quantile(0.25)
    q50 = df_copy[price_col].quantile(0.50)
    q75 = df_copy[price_col].quantile(0.75)
    
    def get_segment(p):
        if p <= q25:
            return "Budget"
        elif p <= q50:
            return "Mid-Range"
        elif p <= q75:
            return "Premium"
        else:
            return "Luxury"
            
    df_copy["Price_Segment"] = df_copy[price_col].apply(get_segment)
    return df_copy
