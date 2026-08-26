import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import io

from utils.ui_helpers import apply_custom_css, render_header, render_progress_stepper, render_sidebar, render_kpi_card
from utils.prediction_helpers import load_saved_model_payload, format_currency_inr
from utils.dataset_helpers import load_default_housing_dataset
from utils.training_helpers import prepare_pipeline_and_splits
from modules.training import train_models_dict
from modules.comparison import select_best_model
from modules.save_model import save_best_model
from modules.prediction import predict_price
from modules.valuation import plot_property_value_gauge
from modules.recommendation import generate_investment_recommendation
from modules.report_generator import generate_property_report_text
from modules.feature_importance import plot_feature_importance

st.set_page_config(
    page_title="House Price Estimator - HomeValue AI",
    page_icon="🏡",
    layout="wide"
)

apply_custom_css()
render_sidebar()

# Stepper Step 5
render_progress_stepper(5)

# Header
render_header(
    title="House Price Estimator",
    subtitle="Input property specifications to receive instant AI market valuation, value tier breakdown, and appraisal reports.",
    icon="🏡"
)

# Load saved model or auto-train baseline if missing
payload = load_saved_model_payload()

if payload is None:
    # Auto-train default model if not trained yet
    df = st.session_state.get("df", load_default_housing_dataset())
    splits = prepare_pipeline_and_splits(df, target_col="price")
    res = train_models_dict(splits["X_train_trans"], splits["y_train"], splits["X_test_trans"], splits["y_test"], ["Random Forest Regressor"])
    b_name, b_info = select_best_model(res)
    save_path = save_best_model(b_info["model"], splits["preprocessor"], splits["feature_names"], b_name)
    payload = load_saved_model_payload(save_path)

model = payload["model"]
preprocessor = payload["preprocessor"]
feature_names = payload["feature_names"]
model_name = payload.get("model_name", "Random Forest Regressor")

# ------------------------------------------------------------
# PROPERTY DETAILS FORM
# ------------------------------------------------------------
with st.container(border=True):
    st.markdown("### 📋 Enter Property Specifications")

    form_tab1, form_tab2 = st.tabs(["🏠 Basic Information", "📍 Property Amenities & Features"])

    with form_tab1:
        col_b1, col_b2, col_b3 = st.columns(3)
        with col_b1:
            area = st.number_input("Property Area (sq.ft)", min_value=500, max_value=25000, value=6000, step=100, help="Total built-up plot floor space.")
            bedrooms = st.selectbox("Bedrooms Count", options=[1, 2, 3, 4, 5, 6], index=2)
        with col_b2:
            bathrooms = st.selectbox("Bathrooms Count", options=[1, 2, 3, 4], index=1)
            stories = st.selectbox("Building Stories / Levels", options=[1, 2, 3, 4], index=1)
        with col_b3:
            parking = st.selectbox("Parking Spaces", options=[0, 1, 2, 3], index=1)

    with form_tab2:
        col_p1, col_p2, col_p3 = st.columns(3)
        with col_p1:
            mainroad = st.radio("Main Road Access?", options=["yes", "no"], index=0, horizontal=True)
            guestroom = st.radio("Guest Room Quarters?", options=["yes", "no"], index=1, horizontal=True)
        with col_p2:
            basement = st.radio("Basement Space?", options=["yes", "no"], index=1, horizontal=True)
            hotwaterheating = st.radio("Hot Water Heating?", options=["yes", "no"], index=1, horizontal=True)
        with col_p3:
            airconditioning = st.radio("Central Air Conditioning?", options=["yes", "no"], index=0, horizontal=True)
            prefarea = st.radio("Preferred Prime Area Zone?", options=["yes", "no"], index=0, horizontal=True)
            
        furnishingstatus = st.selectbox("Furnishing Level", options=["furnished", "semi-furnished", "unfurnished"], index=1)

    input_dict = {
        "area": area,
        "bedrooms": bedrooms,
        "bathrooms": bathrooms,
        "stories": stories,
        "mainroad": mainroad,
        "guestroom": guestroom,
        "basement": basement,
        "hotwaterheating": hotwaterheating,
        "airconditioning": airconditioning,
        "parking": parking,
        "prefarea": prefarea,
        "furnishingstatus": furnishingstatus
    }

    st.markdown("<br>", unsafe_allow_html=True)
    col_btn1, col_btn2 = st.columns([2, 1])

    with col_btn1:
        predict_clicked = st.button("🏠 Estimate Property Value", width="stretch")

    with col_btn2:
        if st.button("🔄 Reset Inputs to Default", width="stretch"):
            st.rerun()

# Run prediction if clicked or if stored in session state
if predict_clicked or "last_prediction" in st.session_state:
    if predict_clicked:
        pred_price = predict_price(model, preprocessor, input_dict)
        st.session_state["last_prediction"] = pred_price
        st.session_state["last_inputs"] = input_dict
        st.session_state["last_pred_time"] = datetime.now().strftime("%H:%M:%S, %d %b %Y")
    else:
        pred_price = st.session_state["last_prediction"]
        input_dict = st.session_state["last_inputs"]
        
    pred_time = st.session_state.get("last_pred_time", datetime.now().strftime("%H:%M:%S"))
    price_per_sqft = pred_price / area if area > 0 else 0

    # ------------------------------------------------------------
    # AI PREDICTION RESULT CARD
    # ------------------------------------------------------------
    with st.container(border=True):
        st.markdown(f'''
            <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap;">
                <div>
                    <span class="badge-gold">ESTIMATED MARKET VALUE</span>
                    <h1 style="color: #F9FAFB; font-size: 2.8rem; margin: 10px 0;">{format_currency_inr(pred_price)}</h1>
                    <div style="display: flex; gap: 15px; font-size: 0.85rem; color: #9CA3AF;">
                        <span>Engine: <strong style="color: #14B8A6;">{model_name}</strong></span>
                        <span>Confidence: <strong style="color: #F59E0B;">★★★★★ (High)</strong></span>
                        <span>Appraised: <strong>{pred_time}</strong></span>
                    </div>
                </div>
                <div style="text-align: right; padding-top: 10px;">
                    <div style="font-size: 0.8rem; color: #9CA3AF; font-weight: 600;">UNIT RATE METRIC</div>
                    <div style="font-size: 1.8rem; font-weight: 700; color: #14B8A6;">₹{price_per_sqft:,.2f}</div>
                    <div style="font-size: 0.75rem; color: #6B7280;">per sq.ft area</div>
                </div>
            </div>
        ''', unsafe_allow_html=True)

    # ------------------------------------------------------------
    # PROPERTY SUMMARY & GAUGE METER
    # ------------------------------------------------------------
    col_sum, col_gauge = st.columns([1, 1.2])
    
    with col_sum:
        with st.container(border=True):
            st.markdown("### 📝 Valuation Summary Table")
            
            sum_data = [
                {"Property Attribute": "Area (sq.ft)", "Input Value": f"{area:,} sq.ft"},
                {"Property Attribute": "Bedrooms / Bathrooms", "Input Value": f"{bedrooms} Beds / {bathrooms} Baths"},
                {"Property Attribute": "Stories / Parking", "Input Value": f"{stories} Stories / {parking} Spots"},
                {"Property Attribute": "Air Conditioning", "Input Value": airconditioning.upper()},
                {"Property Attribute": "Preferred Zone", "Input Value": prefarea.upper()},
                {"Property Attribute": "Furnishing Level", "Input Value": furnishingstatus.capitalize()},
                {"Property Attribute": "Predicted Price", "Input Value": f"₹{pred_price:,.2f}"},
                {"Property Attribute": "Unit Square Rate", "Input Value": f"₹{price_per_sqft:,.2f} / sq.ft"}
            ]
            st.dataframe(pd.DataFrame(sum_data), width="stretch", hide_index=True)

    with col_gauge:
        with st.container(border=True):
            fig_gauge = plot_property_value_gauge(pred_price)
            st.plotly_chart(fig_gauge, width="stretch")

    # ------------------------------------------------------------
    # PRICE INFLUENCING FACTORS & RECOMMENDATIONS
    # ------------------------------------------------------------
    col_fi, col_rec = st.columns([1, 1])
    
    with col_fi:
        with st.container(border=True):
            st.markdown("### 📊 Valuation Feature Drivers")
            fig_fi = plot_feature_importance(model, feature_names, model_name, top_n=8)
            if fig_fi:
                st.plotly_chart(fig_fi, width="stretch")
            else:
                st.info("Feature driver analysis active.")

    with col_rec:
        with st.container(border=True):
            st.markdown("### 💡 AI Investment Advisory")
            recs = generate_investment_recommendation(input_dict, pred_price)
            for r in recs:
                st.markdown(f"- {r}")

    # ------------------------------------------------------------
    # DOWNLOAD VALUATION REPORT
    # ------------------------------------------------------------
    with st.container(border=True):
        st.markdown("### 📄 Download Property Appraisal Report")
        
        report_text = generate_property_report_text(input_dict, pred_price, model_name, recs)
        
        d1, d2 = st.columns(2)
        with d1:
            st.download_button(
                label="📄 Download Valuation Report (.txt)",
                data=report_text,
                file_name=f"HomeValue_Appraisal_Report_{datetime.now().strftime('%Y%m%d')}.txt",
                mime="text/plain",
                width="stretch"
            )
            
        with d2:
            val_df = pd.DataFrame([input_dict])
            val_df["Estimated_Price"] = pred_price
            val_df["Price_Per_Sqft"] = price_per_sqft
            val_csv = val_df.to_csv(index=False).encode('utf-8')
            
            st.download_button(
                label="📊 Download Valuation Data (CSV)",
                data=val_csv,
                file_name="property_valuation_record.csv",
                mime="text/csv",
                width="stretch"
            )

# ------------------------------------------------------------
# NAVIGATION BUTTONS
# ------------------------------------------------------------
st.markdown("<br>", unsafe_allow_html=True)
nav1, nav2 = st.columns(2)
with nav1:
    st.page_link("pages/4_Model_Training.py", label="⬅️ Model Training", width="stretch")
with nav2:
    st.page_link("pages/6_Project_Summary.py", label="Next: Project Summary ➔", width="stretch")
