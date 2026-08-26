import streamlit as st
import pandas as pd
from utils.ui_helpers import apply_custom_css, render_header, render_progress_stepper, render_sidebar, render_kpi_card
from utils.dataset_helpers import load_default_housing_dataset, calculate_memory
from modules.dataset_validation import validate_dataset, calculate_quality_score
from modules.dataset_profile import (
    feature_summary, 
    summary_statistics, 
    generate_recommendations, 
    plot_feature_type_pie, 
    plot_price_distribution_mini
)

st.set_page_config(
    page_title="Dataset Insights - HomeValue AI",
    page_icon="📊",
    layout="wide"
)

apply_custom_css()
render_sidebar()

# Stepper for Step 2
render_progress_stepper(2)

# Page Header
render_header(
    title="Dataset Insights & Profiling",
    subtitle="Explore, validate, and understand the housing dataset structure before machine learning.",
    icon="📊"
)

# ------------------------------------------------------------
# DATASET SELECTION / UPLOAD
# ------------------------------------------------------------
with st.container(border=True):
    st.markdown("### 📥 Load Dataset")
    col_upload, col_action = st.columns([2, 1])

    with col_upload:
        uploaded_file = st.file_uploader("Upload Property CSV File", type=["csv"], help="Accepts CSV files containing house prices and attributes.")

    with col_action:
        st.markdown("<div style='height: 28px;'></div>", unsafe_allow_html=True)
        if st.button("🔄 Reset to Default Dataset", width="stretch"):
            if "df" in st.session_state:
                del st.session_state["df"]
            st.rerun()

# Dataset resolution logic
if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        st.session_state["df"] = df
        st.success("Uploaded CSV loaded successfully!")
    except Exception as e:
        st.error(f"Error loading CSV file: {e}")
        df = load_default_housing_dataset()
        st.session_state["df"] = df
elif "df" not in st.session_state:
    df = load_default_housing_dataset()
    st.session_state["df"] = df
else:
    df = st.session_state["df"]

# Validate dataset
validation_info = validate_dataset(df)
if not validation_info["is_valid"]:
    st.error(f"Invalid dataset: {validation_info['message']}")
    st.stop()

quality_info = calculate_quality_score(df)

# Save into session state
st.session_state["target_col"] = validation_info["target_col"]
st.session_state["numerical_cols"] = validation_info["num_cols_list"]
st.session_state["categorical_cols"] = validation_info["cat_cols_list"]
st.session_state["quality_score"] = quality_info["score"]

# ------------------------------------------------------------
# DATASET STATUS KPI CARDS (2 rows of 3 columns)
# ------------------------------------------------------------
st.markdown("### 📈 Dataset Overview")
r1_1, r1_2, r1_3 = st.columns(3)
with r1_1:
    render_kpi_card("Total Properties", f"{df.shape[0]:,}", "Properties Count", "🔢", "#14B8A6")
with r1_2:
    render_kpi_card("Total Attributes", str(df.shape[1]), "Columns Count", "🏷️", "#3B82F6")
with r1_3:
    render_kpi_card("Target Variable", str(validation_info["target_col"]).upper(), "Valuation Target", "🎯", "#F59E0B")

r2_1, r2_2, r2_3 = st.columns(3)
with r2_1:
    render_kpi_card("Missing Values", str(validation_info["missing_count"]), f"{quality_info['missing_pct']}% null", "⚠️", "#14B8A6")
with r2_2:
    render_kpi_card("Duplicates", str(validation_info["duplicate_count"]), "Exact duplicate rows", "📑", "#3B82F6")
with r2_3:
    render_kpi_card("Memory Allocation", calculate_memory(df), "RAM Usage", "💾", "#F8FAFC")

# ------------------------------------------------------------
# DATA QUALITY SCORE & OVERVIEW
# ------------------------------------------------------------
q_col, c_col = st.columns([1, 1])

with q_col:
    with st.container(border=True):
        st.markdown("### 🏆 Data Health Rating")
        score = quality_info["score"]
        status = quality_info["status"]
        color = quality_info["color"]
        
        st.markdown(f'''
            <div style="text-align: center; padding: 10px;">
                <div style="font-size: 3rem; font-weight: 800; color: {color};">{score} / 100</div>
                <div style="font-size: 1.1rem; font-weight: 700; color: #F9FAFB; margin-top: 4px;">
                    Status: <span style="color: {color};">{status}</span>
                </div>
                <p style="color: #9CA3AF; font-size: 0.82rem; margin-top: 8px;">
                    High data quality score based on zero missing fields, clean schema, and unique records.
                </p>
            </div>
        ''', unsafe_allow_html=True)

with c_col:
    with st.container(border=True):
        fig_pie = plot_feature_type_pie(len(validation_info["num_cols_list"]), len(validation_info["cat_cols_list"]))
        st.plotly_chart(fig_pie, width="stretch")

# ------------------------------------------------------------
# FEATURE INFORMATION & SUMMARY STATISTICS
# ------------------------------------------------------------
t1, t2, t3 = st.tabs(["📋 Feature Metadata", "📊 Summary Statistics", "🎯 Target Variable Summary"])

with t1:
    with st.container(border=True):
        feat_df = feature_summary(df)
        st.dataframe(feat_df, width="stretch", hide_index=True)

with t2:
    with st.container(border=True):
        stats_df = summary_statistics(df)
        st.dataframe(stats_df, width="stretch")

with t3:
    with st.container(border=True):
        target_col = validation_info["target_col"]
        if target_col in df.columns and pd.api.types.is_numeric_dtype(df[target_col]):
            col_t1, col_t2 = st.columns([1, 1.5])
            with col_t1:
                st.markdown(f"#### 🎯 '{target_col.capitalize()}' Metrics")
                st.write(f"• **Minimum:** ₹{df[target_col].min():,}")
                st.write(f"• **Maximum:** ₹{df[target_col].max():,}")
                st.write(f"• **Average:** ₹{df[target_col].mean():,.2f}")
                st.write(f"• **Median:** ₹{df[target_col].median():,}")
                st.write(f"• **Std Dev:** ₹{df[target_col].std():,.2f}")
            with col_t2:
                fig_target = plot_price_distribution_mini(df, target_col)
                if fig_target:
                    st.plotly_chart(fig_target, width="stretch")
        else:
            st.info("Target column is categorical or not numeric.")

# ------------------------------------------------------------
# SAMPLE DATA VIEWER & RECOMMENDATIONS
# ------------------------------------------------------------
with st.container(border=True):
    st.markdown("### 👁️ Sample Data Preview (First 10 Rows)")
    st.dataframe(df.head(10), width="stretch", hide_index=True)

# Smart Recommendations
with st.container(border=True):
    st.markdown("### 💡 Smart Dataset Recommendations")
    recommendations = generate_recommendations(df, quality_info)
    for rec in recommendations:
        st.markdown(f"- {rec}")

# ------------------------------------------------------------
# DOWNLOAD CLEAN DATASET & NAVIGATION
# ------------------------------------------------------------
st.markdown("<br>", unsafe_allow_html=True)
d_col, nav1, nav2 = st.columns([1.5, 1, 1])

with d_col:
    csv_bytes = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download Dataset (CSV)",
        data=csv_bytes,
        file_name="homevalue_clean_dataset.csv",
        mime="text/csv",
        width="stretch"
    )

with nav1:
    st.page_link("pages/1_Home.py", label="⬅️ Home", width="stretch")

with nav2:
    st.page_link("pages/3_EDA.py", label="Next: Market Analysis ➔", width="stretch")
