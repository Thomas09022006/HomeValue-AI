import os
import joblib
import pandas as pd
import numpy as np

def load_saved_model_payload(model_path: str = None):
    """
    Loads saved model, preprocessor, and metadata from joblib payload.
    """
    if model_path is None or not os.path.exists(model_path):
        model_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "models", "best_model.joblib")
        
    if os.path.exists(model_path):
        payload = joblib.load(model_path)
        return payload
    return None

def format_currency_inr(val: float) -> str:
    """
    Formats numeric price value into formatted Indian Rupee (₹) standard currency notation.
    """
    if val >= 10000000:
        return f"₹{val / 10000000:.2f} Cr"
    elif val >= 100000:
        return f"₹{val / 100000:.2f} Lakhs (₹{val:,.0f})"
    else:
        return f"₹{val:,.0f}"
