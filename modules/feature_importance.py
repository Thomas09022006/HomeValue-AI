import pandas as pd
import numpy as np
import plotly.express as px

def plot_feature_importance(model, feature_names: list, model_name: str, top_n: int = 15):
    """
    Extracts feature importances or coefficients and plots horizontal bar chart.
    """
    if hasattr(model, "feature_importances_"):
        importances = model.feature_importances_
        type_str = "Tree Feature Importance"
    elif hasattr(model, "coef_"):
        importances = np.abs(model.coef_)
        type_str = "Absolute Regression Coefficient Weight"
    else:
        return None
        
    df_fi = pd.DataFrame({
        "Feature": feature_names,
        "Importance": importances
    }).sort_values(by="Importance", ascending=False).head(top_n)
    
    fig = px.bar(
        df_fi,
        x="Importance",
        y="Feature",
        orientation="h",
        color="Importance",
        color_continuous_scale="Tealgrn",
        title=f"<b>Top {top_n} Influencing Features ({model_name} - {type_str})</b>"
    )
    fig.update_layout(
        template="plotly_dark",
        font_family="Inter",
        font_color="#F8FAFC",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        yaxis=dict(autorange="reversed")
    )
    return fig
