import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import joblib

def prepare_pipeline_and_splits(df: pd.DataFrame, target_col: str = "price", test_size: float = 0.2, random_state: int = 42):
    """
    Prepares data splits, preprocessing pipeline (StandardScaler for numerical, OneHotEncoder for categorical).
    """
    if target_col not in df.columns:
        raise ValueError(f"Target column '{target_col}' missing from dataset.")
        
    X = df.drop(columns=[target_col])
    y = df[target_col]
    
    num_cols = X.select_dtypes(include=[np.number]).columns.tolist()
    cat_cols = X.select_dtypes(exclude=[np.number]).columns.tolist()
    
    # Define preprocessing steps
    num_transformer = Pipeline(steps=[('scaler', StandardScaler())])
    cat_transformer = Pipeline(steps=[('encoder', OneHotEncoder(handle_unknown='ignore', sparse_output=False))])
    
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', num_transformer, num_cols),
            ('cat', cat_transformer, cat_cols)
        ]
    )
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    
    # Fit preprocessor on training data
    X_train_trans = preprocessor.fit_transform(X_train)
    X_test_trans = preprocessor.transform(X_test)
    
    # Get feature names after encoding
    feature_names = list(num_cols)
    if cat_cols:
        cat_encoder = preprocessor.named_transformers_['cat'].named_steps['encoder']
        encoded_cat_names = cat_encoder.get_feature_names_out(cat_cols).tolist()
        feature_names.extend(encoded_cat_names)
        
    return {
        "X_train": X_train,
        "X_test": X_test,
        "y_train": y_train,
        "y_test": y_test,
        "X_train_trans": X_train_trans,
        "X_test_trans": X_test_trans,
        "preprocessor": preprocessor,
        "feature_names": feature_names,
        "num_cols": num_cols,
        "cat_cols": cat_cols
    }
