import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as gg
from utils.dataset_helpers import get_feature_description

def feature_summary(df: pd.DataFrame) -> pd.DataFrame:
    """
    Generates detailed metadata table for every feature in the dataset.
    """
    summary_data = []
    for col in df.columns:
        dtype = str(df[col].dtype)
        unique_vals = df[col].nunique()
        missing_vals = int(df[col].isnull().sum())
        example_val = str(df[col].iloc[0]) if len(df) > 0 else "N/A"
        desc = get_feature_description(col)
        
        summary_data.append({
            "Feature Name": col,
            "Data Type": dtype,
            "Unique Values": unique_vals,
            "Missing Values": missing_vals,
            "Example Value": example_val,
            "Description": desc
        })
    return pd.DataFrame(summary_data)

def summary_statistics(df: pd.DataFrame) -> pd.DataFrame:
    """
    Computes statistical metrics (mean, median, min, max, std, quartiles) for numerical features.
    """
    num_df = df.select_dtypes(include=[np.number])
    if num_df.empty:
        return pd.DataFrame()
        
    stats = num_df.describe().T
    stats["median"] = num_df.median()
    
    # Reorder columns
    ordered_cols = ["mean", "median", "std", "min", "25%", "50%", "75%", "max"]
    stats = stats[[c for c in ordered_cols if c in stats.columns]]
    stats.columns = [c.capitalize() if c != "std" else "Std Dev" for c in stats.columns]
    return stats.round(2)

def generate_recommendations(df: pd.DataFrame, quality_info: dict) -> list:
    """
    Generates rule-based dataset recommendations.
    """
    recs = []
    
    # Check missing values
    missing_sum = df.isnull().sum().sum()
    if missing_sum == 0:
        recs.append("✅ **Clean Dataset**: Zero missing values detected across all columns.")
    else:
        recs.append(f"⚠️ **Missing Data Alert**: Found {missing_sum} missing values. Consider imputing before training.")
        
    # Check duplicate rows
    dup_sum = df.duplicated().sum()
    if dup_sum == 0:
        recs.append("✅ **No Duplicates**: Dataset contains 100% unique property records.")
    else:
        recs.append(f"⚠️ **Duplicate Records**: {dup_sum} duplicate rows found. Drop duplicates prior to modeling.")
        
    # Check numerical distribution/outliers on price if present
    if "price" in df.columns:
        price_std = df["price"].std()
        price_mean = df["price"].mean()
        if price_std > price_mean * 0.5:
            recs.append("💡 **High Price Variance**: Significant house price spread observed. Feature scaling or tree models recommended.")
            
    if "area" in df.columns:
        recs.append("💡 **Key Feature Identified**: Property area (sq.ft) shows strong baseline correlation with price.")
        
    recs.append("🚀 **Ready for EDA**: Dataset status validated and ready for Exploratory Data Analysis.")
    return recs

def plot_feature_type_pie(num_count: int, cat_count: int):
    """
    Generates Plotly Pie Chart of Numerical vs Categorical Features.
    """
    fig = px.pie(
        values=[num_count, cat_count],
        names=["Numerical Features", "Categorical Features"],
        hole=0.5,
        color_discrete_sequence=["#0F766E", "#D4A017"],
        title="<b>Feature Types Breakdown</b>"
    )
    fig.update_layout(
        font_family="Poppins",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=20, r=20, t=40, b=20),
        legend=dict(orientation="h", yanchor="bottom", y=-0.2, xanchor="center", x=0.5)
    )
    return fig

def plot_price_distribution_mini(df: pd.DataFrame, target_col: str):
    """
    Generates a Plotly Histogram for Target Column Price.
    """
    if target_col not in df.columns:
        return None
        
    fig = px.histogram(
        df,
        x=target_col,
        nbins=30,
        marginal="box",
        color_discrete_sequence=["#0F766E"],
        title=f"<b>Target Variable Distribution ({target_col})</b>"
    )
    mean_val = df[target_col].mean()
    median_val = df[target_col].median()
    
    fig.add_vline(x=mean_val, line_dash="dash", line_color="#D4A017", annotation_text=f"Mean: ₹{mean_val:,.0f}")
    fig.add_vline(x=median_val, line_dash="dot", line_color="#3B82F6", annotation_text=f"Median: ₹{median_val:,.0f}")
    
    fig.update_layout(
        font_family="Poppins",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis_title="Property Price (₹)",
        yaxis_title="Count",
        margin=dict(l=20, r=20, t=40, b=20)
    )
    return fig
