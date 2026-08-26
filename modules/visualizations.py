import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# Palette: Emerald (#14B8A6), Gold (#F59E0B), Sky Blue (#3B82F6), Slate (#0F172A)
PALETTE = ["#14B8A6", "#F59E0B", "#3B82F6", "#8B5CF6", "#EC4899"]

def plot_price_distribution(df: pd.DataFrame, target_col: str = "price"):
    """
    Plots interactive histogram for property prices with Mean and Median markers.
    """
    mean_val = df[target_col].mean()
    median_val = df[target_col].median()
    
    fig = px.histogram(
        df,
        x=target_col,
        nbins=40,
        color_discrete_sequence=["#14B8A6"],
        title="<b>Property Price Distribution Curve</b>",
        hover_data=df.columns
    )
    fig.add_vline(x=mean_val, line_dash="dash", line_color="#F59E0B", annotation_text=f"Mean: ₹{mean_val:,.0f}", annotation_font_color="#F59E0B")
    fig.add_vline(x=median_val, line_dash="dot", line_color="#3B82F6", annotation_text=f"Median: ₹{median_val:,.0f}", annotation_font_color="#3B82F6")
    
    fig.update_layout(
        template="plotly_dark",
        font_family="Inter",
        font_color="#F8FAFC",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis_title="Property Price (₹)",
        yaxis_title="Property Frequency",
        margin=dict(l=20, r=20, t=50, b=20)
    )
    return fig

def plot_feature_distributions(df: pd.DataFrame):
    """
    Plots feature distributions (Area, Bedrooms, Bathrooms, Stories, Parking).
    """
    figures = {}
    
    if "area" in df.columns:
        fig_area = px.histogram(df, x="area", nbins=30, color_discrete_sequence=["#3B82F6"], title="<b>Area (sq.ft) Distribution</b>")
        fig_area.update_layout(template="plotly_dark", font_family="Inter", font_color="#F8FAFC", paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
        figures["area"] = fig_area
        
    for cat_feat, color in [("bedrooms", "#14B8A6"), ("bathrooms", "#F59E0B"), ("stories", "#3B82F6"), ("parking", "#8B5CF6")]:
        if cat_feat in df.columns:
            cnt_df = df[cat_feat].value_counts().reset_index()
            cnt_df.columns = [cat_feat, "count"]
            cnt_df = cnt_df.sort_values(by=cat_feat)
            fig_bar = px.bar(
                cnt_df, 
                x=cat_feat, 
                y="count", 
                color_discrete_sequence=[color],
                text="count",
                title=f"<b>{cat_feat.capitalize()} Count Breakdown</b>"
            )
            fig_bar.update_layout(template="plotly_dark", font_family="Inter", font_color="#F8FAFC", paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
            figures[cat_feat] = fig_bar
            
    return figures

def plot_scatter_relationship(df: pd.DataFrame, x_col: str, y_col: str = "price", color_col: str = None):
    """
    Generates interactive scatter plot with trendline if statsmodels is available.
    """
    try:
        fig = px.scatter(
            df,
            x=x_col,
            y=y_col,
            color=color_col if color_col in df.columns else None,
            trendline="ols",
            color_discrete_sequence=PALETTE,
            title=f"<b>{y_col.capitalize()} vs {x_col.capitalize()} Relationship</b>",
            hover_data=[c for c in ["bedrooms", "bathrooms", "area"] if c in df.columns]
        )
    except (ImportError, Exception):
        fig = px.scatter(
            df,
            x=x_col,
            y=y_col,
            color=color_col if color_col in df.columns else None,
            color_discrete_sequence=PALETTE,
            title=f"<b>{y_col.capitalize()} vs {x_col.capitalize()} Relationship</b>",
            hover_data=[c for c in ["bedrooms", "bathrooms", "area"] if c in df.columns]
        )
        
    fig.update_layout(
        template="plotly_dark",
        font_family="Inter",
        font_color="#F8FAFC",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis_title=x_col.capitalize(),
        yaxis_title=y_col.capitalize()
    )
    return fig

def generate_heatmap(df: pd.DataFrame):
    """
    Generates interactive correlation heatmap for numerical columns.
    """
    num_df = df.select_dtypes(include=[np.number])
    if num_df.empty:
        return None, None
        
    corr = num_df.corr().round(2)
    fig = px.imshow(
        corr,
        text_auto=True,
        aspect="auto",
        color_continuous_scale="Tealgrn",
        title="<b>Numerical Feature Correlation Matrix</b>"
    )
    fig.update_layout(
        template="plotly_dark",
        font_family="Inter",
        font_color="#F8FAFC",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=20, r=20, t=50, b=20)
    )
    return fig, corr

def plot_price_segments_donut(df_segmented: pd.DataFrame):
    """
    Generates donut chart of property price segments.
    """
    seg_counts = df_segmented["Price_Segment"].value_counts().reset_index()
    seg_counts.columns = ["Segment", "Count"]
    
    fig = px.pie(
        seg_counts,
        values="Count",
        names="Segment",
        hole=0.5,
        color="Segment",
        color_discrete_map={
            "Budget": "#3B82F6",
            "Mid-Range": "#14B8A6",
            "Premium": "#F59E0B",
            "Luxury": "#8B5CF6"
        },
        title="<b>Property Price Segments Distribution</b>"
    )
    fig.update_layout(
        template="plotly_dark",
        font_family="Inter",
        font_color="#F8FAFC",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)"
    )
    return fig

def plot_outliers_box(df: pd.DataFrame, num_col: str):
    """
    Generates Box plot for outlier visualization.
    """
    fig = px.box(
        df,
        y=num_col,
        points="outliers",
        color_discrete_sequence=["#F59E0B"],
        title=f"<b>Outlier Box Plot: {num_col.capitalize()}</b>"
    )
    fig.update_layout(
        template="plotly_dark",
        font_family="Inter",
        font_color="#F8FAFC",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)"
    )
    return fig
