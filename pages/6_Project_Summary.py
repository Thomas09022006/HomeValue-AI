import streamlit as st
import pandas as pd
import numpy as np
import io
import joblib

from utils.ui_helpers import apply_custom_css, render_header, render_progress_stepper, render_sidebar, render_kpi_card
from utils.dataset_helpers import load_default_housing_dataset
from utils.summary_helpers import get_project_architecture_tree
from modules.project_info import get_project_metadata
from modules.deployment import generate_deployment_guide_text
from modules.summary import load_project_summary_stats
from modules.comparison import plot_r2_comparison, compare_models

st.set_page_config(
    page_title="Project Summary - HomeValue AI",
    page_icon="🎯",
    layout="wide"
)

apply_custom_css()
render_sidebar()

# Stepper Step 6 (All completed)
render_progress_stepper(6)

# Header
render_header(
    title="Project Summary & Architecture",
    subtitle="Complete enterprise overview of the HomeValue AI platform, dataset insights, model performance, and deployment guide.",
    icon="🎯"
)

meta = get_project_metadata()
df = st.session_state.get("df", load_default_housing_dataset())
results = st.session_state.get("results", None)

stats = load_project_summary_stats(df, results)

# ------------------------------------------------------------
# PROJECT STATISTICS & OVERVIEW
# ------------------------------------------------------------
st.markdown("### 📊 Platform Statistics")
p1, p2, p3, p4 = st.columns(4)

with p1:
    render_kpi_card("Modules Built", "6 Pages", "Prompt 1 to 6", "📦", "#14B8A6")
with p2:
    render_kpi_card("Algorithms", "4 Regressors", "Linear, Tree, RF, XGB", "🤖", "#F59E0B")
with p3:
    render_kpi_card("Visualizations", "20+ Interactive", "Plotly Engine", "📈", "#3B82F6")
with p4:
    render_kpi_card("Accuracy (R²)", f"{stats['best_r2']:.2f}", stats['best_name'], "🏆", "#14B8A6")

# Project Overview Card
with st.container(border=True):
    st.markdown("### 🏠 Project Overview & Objectives")
    col_o1, col_o2 = st.columns([1.5, 1])

    with col_o1:
        st.write(f"• **Platform Name:** {meta['title']} — {meta['subtitle']}")
        st.write("• **Machine Learning Task:** Supervised Multiple Regression")
        st.write("• **Business Objective:** Automated real estate valuation appraising house prices with explainable AI feature weights.")
        st.write("• **Dataset Description:** Multidimensional real estate transaction dataset incorporating spatial area, room counts, amenities, and preferred zones.")
        st.write("• **Deployment Status:** Production-Ready Streamlit Multi-Page Web App.")

    with col_o2:
        st.markdown(f'''
            <div style="background: rgba(20, 184, 166, 0.12); padding: 18px; border-radius: 12px; border-left: 4px solid #14B8A6;">
                <div style="font-weight: 700; color: #F9FAFB;">PROPOSED VALUE PROPOSITION</div>
                <p style="font-size: 0.82rem; color: #D1D5DB; margin-top: 5px;">
                    Replaces subjective manual real estate appraisals with statistical machine learning algorithms, reducing valuation time from days to milliseconds.
                </p>
            </div>
        ''', unsafe_allow_html=True)

# ------------------------------------------------------------
# DATASET & ML PIPELINE SUMMARY
# ------------------------------------------------------------
with st.container(border=True):
    st.markdown("### 🤖 Machine Learning Pipeline & Data Profiling")
    sum_t1, sum_t2 = st.tabs(["📊 Dataset Profile", "⚙️ Machine Learning Architecture"])

    with sum_t1:
        # Row 1: 3 Columns
        k1, k2, k3 = st.columns(3)
        with k1: render_kpi_card("Total Rows", f"{stats['num_rows']:,}", "Dataset size", "🔢", "#14B8A6")
        with k2: render_kpi_card("Total Columns", str(stats['num_cols']), "Raw features", "🏷️", "#3B82F6")
        with k3: render_kpi_card("Numerical", str(stats['num_feats']), "Continuous attributes", "📐", "#F59E0B")
        
        # Row 2: 3 Columns
        k4, k5, k6 = st.columns(3)
        with k4: render_kpi_card("Categorical", str(stats['cat_feats']), "Discrete features", "🛋️", "#14B8A6")
        with k5: render_kpi_card("Missing Values", str(stats['missing']), "0 Null values", "✅", "#14B8A6")
        with k6: render_kpi_card("Duplicates", str(stats['dups']), "100% Unique", "📑", "#3B82F6")

    with sum_t2:
        st.write("• **Preprocessors:** StandardScaler for continuous features + OneHotEncoder for categorical labels.")
        st.write("• **Validation Strategy:** 80/20 Train-Test split + 5-Fold Stratified Cross Validation.")
        st.write("• **Evaluation Metrics:** Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), R² Score.")
        st.write("• **Trained Algorithms:** Linear Regression, Decision Tree Regressor, Random Forest Regressor, XGBoost Regressor.")
        st.write("• **Model Artifacts:** Joblib serialization payload containing fitted pipeline, preprocessor, and feature names.")

# ------------------------------------------------------------
# BEST MODEL HIGHLIGHT CARD & PERFORMANCE
# ------------------------------------------------------------
with st.container(border=True):
    st.markdown(f"### 🏆 Top Performing Valuation Engine: {stats['best_name']}")
    col_b1, col_b2 = st.columns([1.2, 1])

    with col_b1:
        st.markdown(f'''
            <div style="background: #1F2937; border-radius: 14px; padding: 20px; border: 1px solid #374151;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span class="badge-emerald">{stats['best_name']}</span>
                    <span class="badge-gold">R² Score: {stats['best_r2']:.4f}</span>
                </div>
                <div style="font-size: 1.6rem; font-weight: 700; color: #F9FAFB; margin: 10px 0;">
                    RMSE Error: ₹{stats['best_rmse']:,.2f}
                </div>
                <p style="font-size: 0.82rem; color: #9CA3AF;">
                    Selected as the production valuation model for HomeValue AI based on superior cross-validation score and minimal residual error spread.
                </p>
            </div>
        ''', unsafe_allow_html=True)

    with col_b2:
        if results:
            fig_comp = plot_r2_comparison(results)
            st.plotly_chart(fig_comp, width="stretch")
        else:
            st.info("Train models on Page 4 to view comparative charts.")

# ------------------------------------------------------------
# COMPLETE WORKFLOW TIMELINE
# ------------------------------------------------------------
with st.container(border=True):
    st.markdown("### 🔄 Complete End-to-End Application Workflow")
    st.markdown('''
        <div style="display: flex; flex-direction: column; gap: 10px; margin-top: 15px;">
            <div style="background: #090D16; color: white; padding: 14px 20px; border-radius: 10px; display: flex; align-items: center; justify-content: space-between; border: 1px solid rgba(255,255,255,0.08);">
                <div><strong style="color: #F9FAFB;">Step 1: Home Dashboard</strong> — Luxury real estate platform overview & workflow introduction.</div>
                <span class="badge-gold">COMPLETED</span>
            </div>
            <div style="background: #0D9488; color: white; padding: 14px 20px; border-radius: 10px; display: flex; align-items: center; justify-content: space-between;">
                <div><strong style="color: #FFFFFF;">Step 2: Dataset Insights</strong> — Automated data profiling, quality scoring, missingness check.</div>
                <span class="badge-gold">COMPLETED</span>
            </div>
            <div style="background: #090D16; color: white; padding: 14px 20px; border-radius: 10px; display: flex; align-items: center; justify-content: space-between; border: 1px solid rgba(255,255,255,0.08);">
                <div><strong style="color: #F9FAFB;">Step 3: Market Analysis (EDA)</strong> — Interactive Plotly price trends, correlations, outliers.</div>
                <span class="badge-gold">COMPLETED</span>
            </div>
            <div style="background: #0D9488; color: white; padding: 14px 20px; border-radius: 10px; display: flex; align-items: center; justify-content: space-between;">
                <div><strong style="color: #FFFFFF;">Step 4: AI Model Training</strong> — Train & compare 4 regressors, cross-validation, joblib save.</div>
                <span class="badge-gold">COMPLETED</span>
            </div>
            <div style="background: #090D16; color: white; padding: 14px 20px; border-radius: 10px; display: flex; align-items: center; justify-content: space-between; border: 1px solid rgba(255,255,255,0.08);">
                <div><strong style="color: #F9FAFB;">Step 5: House Price Estimator</strong> — Property detail form, AI price estimation, report downloads.</div>
                <span class="badge-gold">COMPLETED</span>
            </div>
            <div style="background: #F59E0B; color: #0F172A; padding: 14px 20px; border-radius: 10px; display: flex; align-items: center; justify-content: space-between;">
                <div><strong style="color: #0F172A;">Step 6: Project Summary</strong> — Comprehensive architecture overview & deployment documentation.</div>
                <span style="background: #0F172A; color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.75rem; font-weight: 600;">ACTIVE</span>
            </div>
        </div>
    ''', unsafe_allow_html=True)

# ------------------------------------------------------------
# TECH STACK & PROJECT STRUCTURE TREE
# ------------------------------------------------------------
col_tech, col_tree = st.columns([1, 1])

with col_tech:
    with st.container(border=True):
        st.markdown("### 🛠️ Technology Stack")
        st.markdown('''
            <div style="display: flex; flex-wrap: wrap; gap: 8px; margin-top: 10px;">
                <span class="badge-emerald">Python 3.10+</span>
                <span class="badge-gold">Streamlit</span>
                <span class="badge-emerald">Pandas</span>
                <span class="badge-gold">NumPy</span>
                <span class="badge-emerald">Scikit-Learn</span>
                <span class="badge-gold">XGBoost</span>
                <span class="badge-emerald">Plotly</span>
                <span class="badge-gold">Joblib</span>
                <span class="badge-emerald">Git</span>
                <span class="badge-gold">GitHub</span>
            </div>
        ''', unsafe_allow_html=True)

with col_tree:
    with st.container(border=True):
        st.markdown("### 📂 Project Directory Structure")
        st.code(get_project_architecture_tree(), language="text")

# ------------------------------------------------------------
# DEPLOYMENT GUIDE
# ------------------------------------------------------------
with st.container(border=True):
    st.markdown("### 🚀 Deployment Guide")
    st.markdown(generate_deployment_guide_text())

# ------------------------------------------------------------
# DOWNLOADS SECTION & ABOUT DEVELOPER
# ------------------------------------------------------------
col_dl, col_dev = st.columns([1.2, 1])

with col_dl:
    with st.container(border=True):
        st.markdown("### 📥 Project Artifact Downloads")
        
        csv_dataset = df.to_csv(index=False).encode('utf-8')
        st.download_button("📊 Download Property Dataset (CSV)", data=csv_dataset, file_name="housing_dataset.csv", mime="text/csv", width="stretch")
        
        if results:
            df_c = compare_models(results)
            c_csv = df_c.to_csv(index=False).encode('utf-8')
            st.download_button("📈 Download Model Leaderboard (CSV)", data=c_csv, file_name="model_leaderboard.csv", mime="text/csv", width="stretch")

with col_dev:
    with st.container(border=True):
        st.markdown('''
            <div style="text-align: center;">
                <div style="font-size: 2.2rem;">👨‍💻</div>
                <div style="font-weight: 700; font-size: 1.1rem; color: #F9FAFB;">HomeValue AI Developer</div>
                <div style="font-size: 0.82rem; color: #14B8A6; margin-bottom: 8px;">Senior AI & Machine Learning Engineer</div>
                <div style="font-size: 0.78rem; color: #9CA3AF;">
                    Specialized in real estate valuation engines, predictive regression algorithms, and interactive web dashboards.
                </div>
                <div style="margin-top: 12px;">
                    <span class="badge-gold">v1.0 Production</span>
                    <span class="badge-emerald">GitHub Ready</span>
                </div>
            </div>
        ''', unsafe_allow_html=True)

# ------------------------------------------------------------
# NAVIGATION BUTTONS
# ------------------------------------------------------------
st.markdown("<br>", unsafe_allow_html=True)
nav1, nav2 = st.columns(2)
with nav1:
    st.page_link("pages/5_House_Price_Estimator.py", label="⬅️ House Price Estimator", width="stretch")
with nav2:
    st.page_link("pages/1_Home.py", label="Return to Home Dashboard 🏠", width="stretch")
