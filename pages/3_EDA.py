import streamlit as st
import pandas as pd
from utils.ui_helpers import apply_custom_css, render_header, render_progress_stepper, render_sidebar, render_kpi_card
from utils.dataset_helpers import load_default_housing_dataset
from modules.eda_logic import compute_eda_kpis, segment_housing_data
from modules.visualizations import (
    plot_price_distribution,
    plot_feature_distributions,
    plot_scatter_relationship,
    generate_heatmap,
    plot_price_segments_donut,
    plot_outliers_box
)

st.set_page_config(
    page_title="Market Analysis (EDA) - HomeValue AI",
    page_icon="📈",
    layout="wide"
)

apply_custom_css()
render_sidebar()

# Stepper Step 3
render_progress_stepper(3)

# Header
render_header(
    title="Market Analysis & EDA",
    subtitle="Uncover structural pricing trends, spatial demand correlations, and feature distributions across property segments.",
    icon="📈"
)

# Dataset Resolution
if "df" not in st.session_state:
    st.session_state["df"] = load_default_housing_dataset()
df = st.session_state["df"]
target_col = st.session_state.get("target_col", "price" if "price" in df.columns else df.columns[0])

# Compute EDA KPI metrics
eda_kpis = compute_eda_kpis(df, target_col)

# ------------------------------------------------------------
# MARKET METRICS KPI CARDS (2 rows of 2 columns)
# ------------------------------------------------------------
st.markdown("### 📊 Key Market Statistics")
m1, m2 = st.columns(2)
with m1:
    render_kpi_card("Mean Property Price", f"₹{eda_kpis['mean_price']:,.2f}", f"Median: ₹{eda_kpis['median_price']:,.0f}", "💵", "#14B8A6")
with m2:
    render_kpi_card("Price Range (Min - Max)", f"₹{eda_kpis['min_price']:,.0f} - ₹{eda_kpis['max_price']:,.0f}", f"Std Dev: ₹{eda_kpis['std_price']:,.0f}", "📐", "#3B82F6")

m3, m4 = st.columns(2)
with m3:
    render_kpi_card("Average Property Area", f"{eda_kpis['avg_area']:,.0f} sq.ft", "Average Floor Space", "🏠", "#F59E0B")
with m4:
    render_kpi_card("Top Price Correlation", f"{eda_kpis['top_corr_col'].capitalize()} ({eda_kpis['top_corr_val']})", "Highest linear relationship", "🔥", "#14B8A6")

# ------------------------------------------------------------
# INTERACTIVE EDA TABS
# ------------------------------------------------------------
st.markdown("### 🔍 Market Analysis Explorer")
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📈 Price Distribution", 
    "📊 Attribute Breakdown", 
    "🎯 Price Relationships", 
    "🔥 Correlation Heatmap", 
    "🏷️ Price Segmentation & Outliers"
])

# Tab 1: Price Distribution
with tab1:
    with st.container(border=True):
        fig_dist = plot_price_distribution(df, target_col)
        st.plotly_chart(fig_dist, width="stretch")

# Tab 2: Feature Distributions
with tab2:
    with st.container(border=True):
        st.markdown("#### Attribute Breakdown Across Dataset")
        feat_figs = plot_feature_distributions(df)
        
        if feat_figs:
            f_cols = st.columns(min(len(feat_figs), 3))
            for idx, (feat_name, fig) in enumerate(feat_figs.items()):
                with f_cols[idx % len(f_cols)]:
                    st.plotly_chart(fig, width="stretch")
        else:
            st.info("No numerical feature distributions available.")

# Tab 3: Price Relationships
with tab3:
    with st.container(border=True):
        st.markdown("#### Scatter & Trendline Explorer")
        c_x1, c_x2 = st.columns([2, 1])
        num_cols = [c for c in df.select_dtypes(include=['number']).columns if c != target_col]
        
        with c_x1:
            scatter_target = st.selectbox("Select X-Axis Feature", options=num_cols, index=0 if num_cols else 0)
        
        fig_scatter = plot_scatter_relationship(df, x_col=scatter_target, y_col=target_col, color_col="furnishingstatus")
        st.plotly_chart(fig_scatter, width="stretch")

# Tab 4: Correlation Heatmap
with tab4:
    with st.container(border=True):
        c_heatmap, corr_matrix = generate_heatmap(df)
        if c_heatmap:
            st.plotly_chart(c_heatmap, width="stretch")
            
            st.markdown("#### Top Correlated Features with Price")
            if target_col in corr_matrix.columns:
                top_corr = corr_matrix[target_col].drop(target_col).sort_values(ascending=False).reset_index()
                top_corr.columns = ["Feature Attribute", "Correlation Factor"]
                st.dataframe(top_corr, width="stretch", hide_index=True)
        else:
            st.info("Insufficient numerical data for correlation matrix.")

# Tab 5: Price Segmentation & Outliers
with tab5:
    with st.container(border=True):
        col_seg1, col_seg2 = st.columns(2)
        
        df_segmented = segment_housing_data(df, target_col)
        
        with col_seg1:
            fig_box = plot_outliers_box(df, num_col=target_col)
            st.plotly_chart(fig_box, width="stretch")
            
        with col_seg2:
            fig_donut = plot_price_segments_donut(df_segmented)
            st.plotly_chart(fig_donut, width="stretch")
            
        st.markdown("#### Average Metrics per Price Segment")
        seg_means = df_segmented.groupby("Price_Segment")[["area", "bedrooms", "bathrooms", target_col]].mean().reset_index()
        st.dataframe(seg_means, width="stretch", hide_index=True)

# ------------------------------------------------------------
# NAVIGATION BUTTONS
# ------------------------------------------------------------
st.markdown("<br>", unsafe_allow_html=True)
nav1, nav2 = st.columns(2)
with nav1:
    st.page_link("pages/2_Dataset_Insights.py", label="⬅️ Dataset Insights", width="stretch")

with nav2:
    st.page_link("pages/4_Model_Training.py", label="Next: AI Model Training ➔", width="stretch")
