import pandas as pd
import numpy as np

def validate_dataset(df: pd.DataFrame) -> dict:
    """
    Validates dataset completeness, missing values, duplicates, and column structure.
    Returns a status dictionary.
    """
    if df is None or df.empty:
        return {"is_valid": False, "message": "Dataset is empty or null."}
        
    num_rows, num_cols = df.shape
    missing_count = int(df.isnull().sum().sum())
    duplicate_count = int(df.duplicated().sum())
    
    num_cols_list = df.select_dtypes(include=[np.number]).columns.tolist()
    cat_cols_list = df.select_dtypes(exclude=[np.number]).columns.tolist()
    
    target_col = "price" if "price" in df.columns else (num_cols_list[0] if len(num_cols_list) > 0 else None)
    
    return {
        "is_valid": True,
        "num_rows": num_rows,
        "num_cols": num_cols,
        "missing_count": missing_count,
        "duplicate_count": duplicate_count,
        "num_cols_list": num_cols_list,
        "cat_cols_list": cat_cols_list,
        "target_col": target_col
    }

def calculate_quality_score(df: pd.DataFrame) -> dict:
    """
    Generates a Data Quality Score out of 100 based on missingness, duplicates, and schema consistency.
    """
    total_cells = df.shape[0] * df.shape[1]
    if total_cells == 0:
        return {"score": 0, "status": "Needs Cleaning", "color": "#EF4444"}
        
    missing_pct = (df.isnull().sum().sum() / total_cells) * 100
    dup_pct = (df.duplicated().sum() / df.shape[0]) * 100
    
    score = 100 - (missing_pct * 3) - (dup_pct * 2)
    score = max(0, min(100, round(score, 1)))
    
    if score >= 90:
        status = "Excellent"
        color = "#0F766E"
    elif score >= 70:
        status = "Good"
        color = "#D4A017"
    else:
        status = "Needs Cleaning"
        color = "#EF4444"
        
    return {
        "score": score,
        "status": status,
        "color": color,
        "missing_pct": round(missing_pct, 2),
        "dup_pct": round(dup_pct, 2)
    }
