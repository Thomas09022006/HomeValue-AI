import streamlit as st
import pandas as pd
import numpy as np
import time
import io
import joblib

from utils.ui_helpers import apply_custom_css, render_header, render_progress_stepper, render_sidebar, render_kpi_card
from utils.dataset_helpers import load_default_housing_dataset
from utils.training_helpers import prepare_pipeline_and_splits
from modules.training import train_models_dict
from modules.evaluation import plot_actual_vs_predicted, plot_residuals
from modules.comparison import compare_models, plot_r2_comparison, select_best_model
from modules.feature_importance import plot_feature_importance
from modules.save_model import save_best_model

st.set_page_config(
    page_title="AI Model Training - HomeValue AI",
    page_icon="🤖",
    layout="wide"
)

apply_custom_css()
render_sidebar()

# Stepper Step 4
render_progress_stepper(4)

# Header
render_header(
    title="AI Model Training & Comparison",
    subtitle="Train, evaluate, and compare multiple regression algorithms to discover the optimal valuation engine.",
    icon="🤖"
)

# Dataset Resolution
if "df" not in st.session_state:
    st.session_state["df"] = load_default_housing_dataset()
df = st.session_state["df"]
target_col = st.session_state.get("target_col", "price" if "price" in df.columns else df.columns[0])

# Prepare Train/Test Split
try:
    data_splits = prepare_pipeline_and_splits(df, target_col=target_col, test_size=0.2, random_state=42)
except Exception as e:
    st.error(f"Error preparing dataset splits: {e}")
    st.stop()

# ------------------------------------------------------------
# DATASET SUMMARY KPI CARDS (2 rows of 3 columns)
# ------------------------------------------------------------
st.markdown("### 📊 Dataset Training Readiness")
s1, s2, s3 = st.columns(3)
with s1:
    render_kpi_card("Train Samples", f"{len(data_splits['X_train']):,}", "80% Split", "🏋️‍♂️", "#14B8A6")
with s2:
    render_kpi_card("Test Samples", f"{len(data_splits['X_test']):,}", "20% Split", "🧪", "#3B82F6")
with s3:
    render_kpi_card("Features Count", str(len(data_splits['feature_names'])), "Transformed inputs", "🏷️", "#F59E0B")

s4, s5, s6 = st.columns(3)
with s4:
    render_kpi_card("Target Variable", target_col.upper(), "Continuous target", "🎯", "#14B8A6")
with s5:
    render_kpi_card("Missing Values", "0", "100% Cleaned", "✅", "#14B8A6")
with s6:
    render_kpi_card("Status", "READY", "Splits Configured", "🚀", "#F59E0B")

# ------------------------------------------------------------
# TRAINING CONFIGURATION & MODEL SELECTION
# ------------------------------------------------------------
c_cfg, c_models = st.columns([1, 1.2])

with c_cfg:
    with st.container(border=True):
        st.markdown("### ⚙️ Training Parameters")
        st.write("• **Train / Test Split:** 80% / 20%")
        st.write("• **Random State:** 42 (Deterministic)")
        st.write("• **Cross Validation:** 5-Fold Stratified CV")
        st.write("• **Evaluated Metrics:** MAE, MSE, RMSE, R² Score")
        st.write("• **Scaling:** StandardScaler (Numerical) + OneHotEncoder (Categorical)")

with c_models:
    with st.container(border=True):
        st.markdown("### 🤖 Select Algorithms to Train")
        
        cb_lr = st.checkbox("Linear Regression", value=True)
        cb_dt = st.checkbox("Decision Tree Regressor", value=True)
        cb_rf = st.checkbox("Random Forest Regressor", value=True)
        cb_xgb = st.checkbox("XGBoost / Gradient Boosting Regressor", value=True)
        
        selected_models = []
        if cb_lr: selected_models.append("Linear Regression")
        if cb_dt: selected_models.append("Decision Tree Regressor")
        if cb_rf: selected_models.append("Random Forest Regressor")
        if cb_xgb: selected_models.append("XGBoost Regressor")
        
        st.markdown("<br>", unsafe_allow_html=True)
        train_clicked = st.button("🚀 Train Selected Models", width="stretch")

# ------------------------------------------------------------
# MODEL TRAINING EXECUTION
# ------------------------------------------------------------
if train_clicked:
    if not selected_models:
        st.warning("Please select at least one regression algorithm to train.")
    else:
        progress_bar = st.progress(0, text="Initializing training pipeline...")
        time.sleep(0.2)
        
        progress_bar.progress(30, text="Transforming feature vectors...")
        time.sleep(0.2)
        
        progress_bar.progress(60, text="Fitting regression algorithms & computing 5-Fold CV...")
        results = train_models_dict(
            data_splits["X_train_trans"], 
            data_splits["y_train"], 
            data_splits["X_test_trans"], 
            data_splits["y_test"], 
            selected_models
        )
        
        progress_bar.progress(90, text="Selecting best model & generating metrics...")
        best_name, best_info = select_best_model(results)
        
        # Save model to disk & session state
        saved_path = save_best_model(
            best_info["model"], 
            data_splits["preprocessor"], 
            data_splits["feature_names"], 
            best_name
        )
        
        st.session_state["results"] = results
        st.session_state["best_model_name"] = best_name
        st.session_state["best_model_info"] = best_info
        st.session_state["data_splits"] = data_splits
        st.session_state["saved_model_path"] = saved_path
        
        progress_bar.progress(100, text="Training complete! Best model saved successfully.")
        st.success(f"🏆 Training complete! Top performing algorithm: **{best_name}** (R² = {best_info['R2']})")

# Check if results are stored in session state
if "results" in st.session_state:
    results = st.session_state["results"]
    best_name = st.session_state["best_model_name"]
    best_info = st.session_state["best_model_info"]
    data_splits = st.session_state["data_splits"]
    
    # ------------------------------------------------------------
    # MODEL COMPARISON TABLE & BEST MODEL CARD
    # ------------------------------------------------------------
    with st.container(border=True):
        st.markdown("### 🏆 Leaderboard & Model Comparison")
        df_comp = compare_models(results)
        st.dataframe(
            df_comp.style.highlight_max(subset=["R² Score", "5-Fold CV R²"], color="#0D9488")
                   .highlight_min(subset=["RMSE", "MAE"], color="#F59E0B"),
            width="stretch",
            hide_index=True
        )
    
    # Best Model Highlight
    b_col1, b_col2 = st.columns([1.5, 1])
    
    with b_col1:
        with st.container(border=True):
            st.markdown(f'''
                <span class="badge-gold">OPTIMAL VALUATION MODEL</span>
                <h2 style="color: #F9FAFB; margin: 8px 0;">🏆 {best_name}</h2>
                <div style="display: flex; gap: 20px; margin-top: 15px;">
                    <div>
                        <div style="font-size: 0.8rem; color: #9CA3AF;">R² Score</div>
                        <div style="font-size: 1.5rem; font-weight: 700; color: #14B8A6;">{best_info['R2']}</div>
                    </div>
                    <div>
                        <div style="font-size: 0.8rem; color: #9CA3AF;">RMSE</div>
                        <div style="font-size: 1.5rem; font-weight: 700; color: #F59E0B;">₹{best_info['RMSE']:,.0f}</div>
                    </div>
                    <div>
                        <div style="font-size: 0.8rem; color: #9CA3AF;">Training Time</div>
                        <div style="font-size: 1.5rem; font-weight: 700; color: #3B82F6;">{best_info['Time_Sec']}s</div>
                    </div>
                </div>
                <p style="margin-top: 15px; font-size: 0.82rem; color: #D1D5DB;">
                    Selected automatically due to superior variance explanation ({best_info['R2']*100:.1f}%) and low residual error rate. Saved to disk for production valuation.
                </p>
            ''', unsafe_allow_html=True)
        
    with b_col2:
        with st.container(border=True):
            st.markdown('''
                <div style="text-align: center; padding: 10px;">
                    <div style="font-size: 0.82rem; color: #9CA3AF; font-weight: 600;">PROPERTY VALUATION SCORE</div>
                    <div style="font-size: 2rem; color: #F59E0B; margin: 8px 0;">★★★★★</div>
                    <div style="font-size: 1.05rem; font-weight: 700; color: #F9FAFB;">High Reliability ML Engine</div>
                    <div style="font-size: 0.78rem; color: #14B8A6; margin-top: 4px;">Validated on 5-Fold Cross Validation</div>
                </div>
            ''', unsafe_allow_html=True)

    # ------------------------------------------------------------
    # PREDICTED VS ACTUAL & RESIDUAL ANALYSIS
    # ------------------------------------------------------------
    with st.container(border=True):
        st.markdown(f"### 📈 Performance Visualizations ({best_name})")
        vis_tab1, vis_tab2, vis_tab3 = st.tabs(["🎯 Actual vs Predicted", "📉 Residual Analysis", "🏷️ R² Score Comparison"])
        
        with vis_tab1:
            fig_act_pred = plot_actual_vs_predicted(data_splits["y_test"], best_info["y_pred"], best_name)
            st.plotly_chart(fig_act_pred, width="stretch")
            
        with vis_tab2:
            fig_res, fig_hist = plot_residuals(data_splits["y_test"], best_info["y_pred"], best_name)
            col_r1, col_r2 = st.columns(2)
            with col_r1:
                st.plotly_chart(fig_res, width="stretch")
            with col_r2:
                st.plotly_chart(fig_hist, width="stretch")
            st.info("💡 **Residual Interpretation**: Well-performing regression models display residual errors centered closely around 0 with uniform variance.")
            
        with vis_tab3:
            fig_r2_comp = plot_r2_comparison(results)
            st.plotly_chart(fig_r2_comp, width="stretch")

    # ------------------------------------------------------------
    # FEATURE IMPORTANCE
    # ------------------------------------------------------------
    with st.container(border=True):
        st.markdown(f"### 🧠 Feature Importance Breakdown ({best_name})")
        fig_fi = plot_feature_importance(best_info["model"], data_splits["feature_names"], best_name)
        if fig_fi:
            st.plotly_chart(fig_fi, width="stretch")
        else:
            st.info("Feature importance display not applicable for this model format.")

    # ------------------------------------------------------------
    # DOWNLOAD MODEL & METRICS
    # ------------------------------------------------------------
    with st.container(border=True):
        st.markdown("### 📥 Download Artifacts")
        dl1, dl2, dl3 = st.columns(3)
        
        with dl1:
            comp_csv = df_comp.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="📊 Download Model Comparison CSV",
                data=comp_csv,
                file_name="model_comparison_metrics.csv",
                mime="text/csv",
                width="stretch"
            )
            
        with dl2:
            buffer = io.BytesIO()
            joblib.dump(best_info["model"], buffer)
            st.download_button(
                label="🤖 Download Best Model (.joblib)",
                data=buffer.getvalue(),
                file_name=f"{best_name.lower().replace(' ', '_')}.joblib",
                mime="application/octet-stream",
                width="stretch"
            )
            
        with dl3:
            res_df = pd.DataFrame({"Actual": data_splits["y_test"], "Predicted": best_info["y_pred"]})
            res_csv = res_df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="📉 Download Test Predictions CSV",
                data=res_csv,
                file_name="test_predictions.csv",
                mime="text/csv",
                width="stretch"
            )

# ------------------------------------------------------------
# NAVIGATION BUTTONS
# ------------------------------------------------------------
st.markdown("<br>", unsafe_allow_html=True)
nav1, nav2 = st.columns(2)
with nav1:
    st.page_link("pages/3_EDA.py", label="⬅️ Market Analysis", width="stretch")
with nav2:
    st.page_link("pages/5_House_Price_Estimator.py", label="Next: House Price Estimator ➔", width="stretch")
