import streamlit as st
from utils.ui_helpers import apply_custom_css, render_progress_stepper, render_sidebar

st.set_page_config(
    page_title="HomeValue AI - Luxury Real Estate Valuation",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply UI design system
apply_custom_css()
render_sidebar()

# Stepper for Step 1
render_progress_stepper(1)

# ------------------------------------------------------------
# HERO SECTION
# ------------------------------------------------------------
st.markdown('''
    <div class="hero-banner" style="padding: 40px; text-align: left;">
        <div style="display: flex; flex-wrap: wrap; justify-content: space-between; align-items: center;">
            <div style="flex: 1; min-width: 300px; padding-right: 20px;">
                <span class="badge-gold" style="margin-bottom: 10px;">PREMIUM REAL ESTATE TECH</span>
                <h1 class="hero-title" style="font-size: 2.6rem; margin-top: 5px; color: #FFFFFF;">🏠 HomeValue AI</h1>
                <p class="hero-subtitle" style="color: #E5E7EB;">
                    AI-Powered House Price Prediction & Property Valuation Platform. Experience machine learning precision tailored for commercial real estate valuation.
                </p>
            </div>
            <div style="flex: 0.8; min-width: 280px; text-align: center; margin-top: 15px;">
                <div style="background: rgba(31, 41, 55, 0.7); border-radius: 20px; padding: 25px; border: 1px solid rgba(255,255,255,0.15); backdrop-filter: blur(10px);">
                    <div style="font-size: 4rem; margin-bottom: 8px;">🏰</div>
                    <div style="font-weight: 700; font-size: 1.1rem; color: #FFFFFF;">Smart Property Intelligence</div>
                    <div style="font-size: 0.82rem; color: #D1D5DB; margin-top: 4px;">Valuation accuracy powered by 4 Advanced Regression Algorithms</div>
                </div>
            </div>
        </div>
    </div>
''', unsafe_allow_html=True)

col_hero1, col_hero2 = st.columns([1, 1])
with col_hero1:
    st.page_link("pages/2_Dataset_Insights.py", label="📊 Explore Dataset Insights", width="stretch")
with col_hero2:
    st.page_link("pages/5_House_Price_Estimator.py", label="🏡 Estimate Property Value", width="stretch")

st.markdown("<br>", unsafe_allow_html=True)

# ------------------------------------------------------------
# ABOUT PROJECT
# ------------------------------------------------------------
with st.container(border=True):
    st.markdown("### 🌟 About The Platform")
    st.write(
        """
        **HomeValue AI** bridges the gap between complex Data Science algorithms and high-end Real Estate decision making. 
        By leveraging historical housing datasets, physical property characteristics, and location parameters, our AI models perform automated market appraisals with high statistical precision.
        """
    )

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('''
            <div style="background: #1F2937; border-radius: 14px; padding: 18px; border: 1px solid #374151; text-align: center;">
                <div style="font-size: 1.8rem;">🏙️</div>
                <div style="font-weight: 700; color: #F9FAFB; margin: 6px 0;">What is House Valuation?</div>
                <div style="font-size: 0.82rem; color: #9CA3AF;">Estimating property fair market value based on structural attributes, area, and spatial demand factors.</div>
            </div>
        ''', unsafe_allow_html=True)

    with col2:
        st.markdown('''
            <div style="background: #1F2937; border-radius: 14px; padding: 18px; border: 1px solid #374151; text-align: center;">
                <div style="font-size: 1.8rem;">🧠</div>
                <div style="font-weight: 700; color: #F9FAFB; margin: 6px 0;">How ML Predicts Prices</div>
                <div style="font-size: 0.82rem; color: #9CA3AF;">Supervised regression algorithms analyze feature patterns, weighted correlations, and nonlinear relationships.</div>
            </div>
        ''', unsafe_allow_html=True)

    with col3:
        st.markdown('''
            <div style="background: #1F2937; border-radius: 14px; padding: 18px; border: 1px solid #374151; text-align: center;">
                <div style="font-size: 1.8rem;">💼</div>
                <div style="font-weight: 700; color: #F9FAFB; margin: 6px 0;">Real-World Applications</div>
                <div style="font-size: 0.82rem; color: #9CA3AF;">Mortgage underwriting, commercial property acquisition, portfolio advisory, and home sellers.</div>
            </div>
        ''', unsafe_allow_html=True)

# ------------------------------------------------------------
# WORKFLOW
# ------------------------------------------------------------
with st.container(border=True):
    st.markdown("### 🔄 End-to-End Analytics Workflow")
    st.markdown('''
        <div style="display: flex; flex-wrap: wrap; justify-content: space-between; align-items: center; gap: 8px; margin-top: 12px;">
            <div style="flex: 1; background: #090D16; color: #F9FAFB; padding: 14px; border-radius: 12px; text-align: center; border: 1px solid #1F2937;">
                <div style="font-size: 1.1rem;">📁</div>
                <div style="font-weight: 600; font-size: 0.82rem; color: #F9FAFB;">1. Dataset</div>
            </div>
            <div style="color: #F59E0B; font-weight: bold;">➔</div>
            <div style="flex: 1; background: #0D9488; color: white; padding: 14px; border-radius: 12px; text-align: center;">
                <div style="font-size: 1.1rem;">🧹</div>
                <div style="font-weight: 600; font-size: 0.82rem; color: #FFFFFF;">2. Profiling</div>
            </div>
            <div style="color: #F59E0B; font-weight: bold;">➔</div>
            <div style="flex: 1; background: #090D16; color: #F9FAFB; padding: 14px; border-radius: 12px; text-align: center; border: 1px solid #1F2937;">
                <div style="font-size: 1.1rem;">📈</div>
                <div style="font-weight: 600; font-size: 0.82rem; color: #F9FAFB;">3. EDA</div>
            </div>
            <div style="color: #F59E0B; font-weight: bold;">➔</div>
            <div style="flex: 1; background: #0D9488; color: white; padding: 14px; border-radius: 12px; text-align: center;">
                <div style="font-size: 1.1rem;">🤖</div>
                <div style="font-weight: 600; font-size: 0.82rem; color: #FFFFFF;">4. ML Training</div>
            </div>
            <div style="color: #F59E0B; font-weight: bold;">➔</div>
            <div style="flex: 1; background: #090D16; color: #F9FAFB; padding: 14px; border-radius: 12px; text-align: center; border: 1px solid #1F2937;">
                <div style="font-size: 1.1rem;">🏡</div>
                <div style="font-weight: 600; font-size: 0.82rem; color: #F9FAFB;">5. Prediction</div>
            </div>
            <div style="color: #F59E0B; font-weight: bold;">➔</div>
            <div style="flex: 1; background: #F59E0B; color: #0F172A; padding: 14px; border-radius: 12px; text-align: center;">
                <div style="font-size: 1.1rem;">🎯</div>
                <div style="font-weight: 700; font-size: 0.82rem; color: #0F172A;">6. Valuation</div>
            </div>
        </div>
    ''', unsafe_allow_html=True)

# ------------------------------------------------------------
# FEATURE CARDS
# ------------------------------------------------------------
st.markdown("### ✨ Key Platform Features")
f1, f2, f3, f4 = st.columns(4)

with f1:
    st.markdown('''
        <div class="kpi-card" style="border-left-color: #14B8A6; height: 160px;">
            <div style="font-size: 1.5rem;">📊</div>
            <div style="font-weight: 700; color: #F9FAFB; margin: 4px 0;">Dataset Insights</div>
            <div style="font-size: 0.78rem; color: #9CA3AF;">Automated data quality scoring, missingness profile, and summary statistics.</div>
        </div>
    ''', unsafe_allow_html=True)

with f2:
    st.markdown('''
        <div class="kpi-card" style="border-left-color: #F59E0B; height: 160px;">
            <div style="font-size: 1.5rem;">📈</div>
            <div style="font-weight: 700; color: #F9FAFB; margin: 4px 0;">Interactive EDA</div>
            <div style="font-size: 0.78rem; color: #9CA3AF;">Plotly price distribution, correlation heatmaps, and property feature relationships.</div>
        </div>
    ''', unsafe_allow_html=True)

with f3:
    st.markdown('''
        <div class="kpi-card" style="border-left-color: #3B82F6; height: 160px;">
            <div style="font-size: 1.5rem;">🤖</div>
            <div style="font-weight: 700; color: #F9FAFB; margin: 4px 0;">Model Comparison</div>
            <div style="font-size: 0.78rem; color: #9CA3AF;">Evaluate Linear Regression, Decision Tree, Random Forest, and XGBoost side-by-side.</div>
        </div>
    ''', unsafe_allow_html=True)

with f4:
    st.markdown('''
        <div class="kpi-card" style="border-left-color: #14B8A6; height: 160px;">
            <div style="font-size: 1.5rem;">🏡</div>
            <div style="font-weight: 700; color: #F9FAFB; margin: 4px 0;">Property Estimator</div>
            <div style="font-size: 0.78rem; color: #9CA3AF;">Instant market value estimation with feature influence breakdowns & PDF reports.</div>
        </div>
    ''', unsafe_allow_html=True)

# ------------------------------------------------------------
# SUPPORTED MODELS & TECH STACK
# ------------------------------------------------------------
col_left, col_right = st.columns([1.2, 1])

with col_left:
    with st.container(border=True):
        st.markdown("### 🤖 Supported Regression Algorithms")
        
        st.markdown('''
            <div style="margin-bottom: 12px;">
                <span style="font-weight: 700; color: #14B8A6;">1. Linear Regression</span>
                <p style="font-size: 0.82rem; color: #D1D5DB; margin: 2px 0;">Baseline linear mathematical modeling establishing direct coefficient weights per property feature.</p>
            </div>
            <div style="margin-bottom: 12px;">
                <span style="font-weight: 700; color: #F59E0B;">2. Decision Tree Regressor</span>
                <p style="font-size: 0.82rem; color: #D1D5DB; margin: 2px 0;">Non-linear rule-based split model isolating property feature thresholds.</p>
            </div>
            <div style="margin-bottom: 12px;">
                <span style="font-weight: 700; color: #3B82F6;">3. Random Forest Regressor</span>
                <p style="font-size: 0.82rem; color: #D1D5DB; margin: 2px 0;">Ensemble bagger combining multiple decision trees to minimize prediction variance.</p>
            </div>
            <div style="margin-bottom: 12px;">
                <span style="font-weight: 700; color: #14B8A6;">4. XGBoost Regressor</span>
                <p style="font-size: 0.82rem; color: #D1D5DB; margin: 2px 0;">Gradient boosting framework optimized for enterprise speed and predictive accuracy.</p>
            </div>
        ''', unsafe_allow_html=True)

with col_right:
    with st.container(border=True):
        st.markdown("### 🛠️ Technology Stack")
        
        st.markdown('''
            <div style="display: flex; flex-wrap: wrap; gap: 8px;">
                <span class="badge-emerald">Python 3.10+</span>
                <span class="badge-gold">Streamlit</span>
                <span class="badge-emerald">Pandas</span>
                <span class="badge-gold">NumPy</span>
                <span class="badge-emerald">Scikit-Learn</span>
                <span class="badge-gold">XGBoost</span>
                <span class="badge-emerald">Plotly</span>
                <span class="badge-gold">Joblib</span>
            </div>
            <hr style="margin: 15px 0; border-color: #374151;">
            <div style="font-size: 0.82rem; color: #9CA3AF;">
                Designed following modern luxury software architecture, responsive UI components, and full explainable AI standards.
            </div>
        ''', unsafe_allow_html=True)

# ------------------------------------------------------------
# FOOTER
# ------------------------------------------------------------
st.divider()
st.markdown('''
    <div style="text-align: center; color: #6B7280; font-size: 0.82rem; padding: 10px 0;">
        <strong>HomeValue AI</strong> — AI-Powered Property Valuation Platform | Developed for Commercial Real Estate Intelligence | v1.0
    </div>
''', unsafe_allow_html=True)
