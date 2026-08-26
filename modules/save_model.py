import os
import joblib

def save_best_model(model_obj, preprocessor_obj, feature_names: list, model_name: str, save_dir: str = "models") -> str:
    """
    Saves the best model, preprocessor, feature names, and metadata dictionary into models/best_model.joblib.
    """
    abs_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), save_dir)
    os.makedirs(abs_dir, exist_ok=True)
    
    save_path = os.path.join(abs_dir, "best_model.joblib")
    
    payload = {
        "model": model_obj,
        "preprocessor": preprocessor_obj,
        "feature_names": feature_names,
        "model_name": model_name
    }
    
    joblib.dump(payload, save_path)
    return save_path
