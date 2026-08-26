import time
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import cross_val_score

try:
    from xgboost import XGBRegressor
    HAS_XGBOOST = True
except ImportError:
    HAS_XGBOOST = False

def train_models_dict(X_train, y_train, X_test, y_test, selected_models: list) -> dict:
    """
    Trains selected machine learning regression models and computes evaluation metrics.
    """
    results = {}
    
    models = {}
    if "Linear Regression" in selected_models:
        models["Linear Regression"] = LinearRegression()
    if "Decision Tree Regressor" in selected_models:
        models["Decision Tree Regressor"] = DecisionTreeRegressor(random_state=42)
    if "Random Forest Regressor" in selected_models:
        models["Random Forest Regressor"] = RandomForestRegressor(n_estimators=100, random_state=42)
    if "XGBoost Regressor" in selected_models:
        if HAS_XGBOOST:
            models["XGBoost Regressor"] = XGBRegressor(n_estimators=100, learning_rate=0.1, random_state=42)
        else:
            models["XGBoost Regressor"] = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, random_state=42)
            
    for name, model in models.items():
        start_time = time.time()
        model.fit(X_train, y_train)
        elapsed_time = round(time.time() - start_time, 3)
        
        y_pred = model.predict(X_test)
        
        mae = mean_absolute_error(y_test, y_pred)
        mse = mean_squared_error(y_test, y_pred)
        rmse = np.sqrt(mse)
        r2 = r2_score(y_test, y_pred)
        
        # 5-fold CV score
        cv_scores = cross_val_score(model, X_train, y_train, cv=5, scoring='r2')
        cv_r2_mean = np.mean(cv_scores)
        
        results[name] = {
            "model": model,
            "y_pred": y_pred,
            "MAE": round(mae, 2),
            "MSE": round(mse, 2),
            "RMSE": round(rmse, 2),
            "R2": round(r2, 4),
            "CV_R2": round(cv_r2_mean, 4),
            "Time_Sec": elapsed_time
        }
        
    return results
