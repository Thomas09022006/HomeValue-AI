import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

def plot_actual_vs_predicted(y_test, y_pred, model_name: str):
    """
    Generates interactive scatter plot comparing Actual vs Predicted prices with 45-degree line.
    """
    df_eval = pd.DataFrame({"Actual Price": y_test, "Predicted Price": y_pred})
    
    fig = px.scatter(
        df_eval,
        x="Actual Price",
        y="Predicted Price",
        color_discrete_sequence=["#14B8A6"],
        title=f"<b>Predicted vs Actual House Prices ({model_name})</b>",
        hover_data=["Actual Price", "Predicted Price"]
    )
    
    # Add 45-degree perfect prediction line
    min_val = min(y_test.min(), y_pred.min())
    max_val = max(y_test.max(), y_pred.max())
    fig.add_shape(
        type="line",
        x0=min_val, y0=min_val,
        x1=max_val, y1=max_val,
        line=dict(color="#F59E0B", width=3, dash="dash")
    )
    
    fig.update_layout(
        template="plotly_dark",
        font_family="Inter",
        font_color="#F8FAFC",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis_title="Actual Market Price (₹)",
        yaxis_title="AI Predicted Price (₹)"
    )
    return fig

def plot_residuals(y_test, y_pred, model_name: str):
    """
    Generates residual scatter plot and residual distribution histogram.
    """
    residuals = y_test - y_pred
    df_res = pd.DataFrame({"Predicted Price": y_pred, "Residuals": residuals})
    
    # Residual scatter
    fig_res = px.scatter(
        df_res,
        x="Predicted Price",
        y="Residuals",
        color_discrete_sequence=["#3B82F6"],
        title=f"<b>Residual Error Scatter ({model_name})</b>"
    )
    fig_res.add_hline(y=0, line_dash="dash", line_color="#F59E0B")
    fig_res.update_layout(
        template="plotly_dark",
        font_family="Inter",
        font_color="#F8FAFC",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis_title="Predicted Price (₹)",
        yaxis_title="Residual Error (Actual - Predicted)"
    )
    
    # Residual histogram
    fig_hist = px.histogram(
        df_res,
        x="Residuals",
        nbins=25,
        color_discrete_sequence=["#14B8A6"],
        title=f"<b>Residual Error Normal Distribution ({model_name})</b>"
    )
    fig_hist.update_layout(
        template="plotly_dark",
        font_family="Inter",
        font_color="#F8FAFC",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)"
    )
    
    return fig_res, fig_hist
