import pandas as pd
import plotly.express as px

def compare_models(results_dict: dict) -> pd.DataFrame:
    """
    Constructs a comparison summary DataFrame sorted by highest R2 Score.
    """
    comp_list = []
    for model_name, info in results_dict.items():
        comp_list.append({
            "Model": model_name,
            "MAE": f"₹{info['MAE']:,.2f}",
            "MSE": f"{info['MSE']:,.2e}",
            "RMSE": f"₹{info['RMSE']:,.2f}",
            "R² Score": info["R2"],
            "5-Fold CV R²": info["CV_R2"],
            "Training Time (s)": info["Time_Sec"]
        })
        
    df_comp = pd.DataFrame(comp_list)
    df_comp = df_comp.sort_values(by="R² Score", ascending=False).reset_index(drop=True)
    return df_comp

def plot_r2_comparison(results_dict: dict):
    """
    Bar chart comparing R2 scores across trained regression models.
    """
    data = [{"Model": k, "R2": v["R2"]} for k, v in results_dict.items()]
    df_r2 = pd.DataFrame(data).sort_values(by="R2", ascending=True)
    
    fig = px.bar(
        df_r2,
        x="R2",
        y="Model",
        orientation="h",
        color="R2",
        color_continuous_scale="Tealgrn",
        text="R2",
        title="<b>Model Accuracy Comparison (R² Score)</b>"
    )
    fig.update_layout(
        template="plotly_dark",
        font_family="Inter",
        font_color="#F8FAFC",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis_title="R² Score (Higher is Better)",
        yaxis_title="Algorithm"
    )
    return fig

def select_best_model(results_dict: dict) -> tuple:
    """
    Selects the best performing model based on highest R2 score.
    Returns (best_model_name, best_model_dict).
    """
    best_name = max(results_dict, key=lambda k: results_dict[k]["R2"])
    return best_name, results_dict[best_name]
