import pandas as pd
import numpy as np

def preprocess_input(input_dict: dict, preprocessor, feature_names: list) -> np.ndarray:
    """
    Converts property user input dictionary into a pandas DataFrame, transforms via preprocessor.
    """
    input_df = pd.DataFrame([input_dict])
    X_trans = preprocessor.transform(input_df)
    return X_trans

def predict_price(model, preprocessor, input_dict: dict) -> float:
    """
    Predicts property market value from input dictionary using loaded preprocessor and model.
    """
    input_df = pd.DataFrame([input_dict])
    X_trans = preprocessor.transform(input_df)
    pred = model.predict(X_trans)[0]
    return float(pred)
