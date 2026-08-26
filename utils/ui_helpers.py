import streamlit as st

def apply_custom_css():
    """
    Injects streamlined dark UI theme with responsive layout and clean typography:
    - Page Background: #0B0F17
    - Container Cards: #111827
    - Inner Metric Cards: #1F2937
    - Accents: Emerald Teal (#14B8A6), Warm Gold (#F59E0B)
    """
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
        
        html, body, [class*="css"], .stApp {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            background-color: #0B0F17 !important;
            color: #F9FAFB !important;
        }

        /* Main Workspace Container - Give full width breathing space */
        .main .block-container {
            padding-top: 1.5rem;
            padding-bottom: 2.5rem;
            max-width: 1280px;
        }

        /* Text Contrast Rules */
        h1, h2, h3, h4, h5, h6 {
            color: #F9FAFB !important;
            font-weight: 700 !important;
            letter-spacing: -0.3px;
        }

        p, span, label, li, div {
            color: #E5E7EB;
        }

        .stMarkdown p, .stMarkdown span, .stMarkdown li {
            color: #E5E7EB !important;
        }

        /* Hide 'app' entry from sidebar navigation list */
        [data-testid="stSidebarNav"] ul li:first-child {
            display: none !important;
        }

        /* Clean Dark Sidebar */
        [data-testid="stSidebar"] {
            background-color: #090D16 !important;
            color: #F9FAFB !important;
            border-right: 1px solid rgba(255, 255, 255, 0.08) !important;
        }

        [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, 
        [data-testid="stSidebar"] h3, [data-testid="stSidebar"] span,
        [data-testid="stSidebar"] label, [data-testid="stSidebar"] p {
            color: #F9FAFB !important;
        }

        /* Navigation item hover in sidebar */
        [data-testid="stSidebarNav"] a {
            border-radius: 10px !important;
            margin: 3px 8px !important;
            padding: 9px 12px !important;
            font-weight: 500 !important;
            color: #D1D5DB !important;
            transition: all 0.2s ease !important;
        }

        [data-testid="stSidebarNav"] a:hover {
            background-color: rgba(20, 184, 166, 0.18) !important;
            color: #F59E0B !important;
        }

        [data-testid="stSidebarNav"] a[aria-current="page"] {
            background: #0D9488 !important;
            color: #FFFFFF !important;
            font-weight: 600 !important;
            box-shadow: 0 4px 12px rgba(13, 148, 136, 0.35) !important;
        }

        /* Native Container Border Wrapper Styling */
        [data-testid="stVerticalBlockBorderWrapper"] {
            border-radius: 14px !important;
            border: 1px solid rgba(255, 255, 255, 0.08) !important;
            background: #111827 !important;
            box-shadow: 0 4px 16px rgba(0, 0, 0, 0.3) !important;
            padding: 20px !important;
            margin-bottom: 16px !important;
        }

        /* Inputs & Dropdowns Dark Mode Fix */
        div[data-baseweb="select"] > div {
            background-color: #1F2937 !important;
            color: #F9FAFB !important;
            border-color: #374151 !important;
            border-radius: 10px !important;
        }

        div[data-baseweb="select"] span {
            color: #F9FAFB !important;
        }

        .stNumberInput input, .stTextInput input {
            background-color: #1F2937 !important;
            color: #F9FAFB !important;
            border: 1px solid #374151 !important;
            border-radius: 10px !important;
        }

        div[data-testid="stFileUploader"] {
            background-color: #111827 !important;
            border: 1px dashed #374151 !important;
            border-radius: 12px !important;
            padding: 15px !important;
        }

        /* Page Link Buttons Styling */
        [data-testid="stPageLink-NavLink"] {
            background: #1F2937 !important;
            color: #F9FAFB !important;
            border: 1px solid #374151 !important;
            border-radius: 12px !important;
            padding: 10px 18px !important;
            font-weight: 600 !important;
            transition: all 0.2s ease !important;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2) !important;
        }

        [data-testid="stPageLink-NavLink"]:hover {
            background: #0D9488 !important;
            border-color: #14B8A6 !important;
            color: #FFFFFF !important;
            transform: translateY(-1px) !important;
            box-shadow: 0 4px 14px rgba(20, 184, 166, 0.3) !important;
        }

        [data-testid="stPageLink-NavLink"] p, 
        [data-testid="stPageLink-NavLink"] span {
            color: #FFFFFF !important;
        }

        /* Clean Header Banner */
        .hero-banner {
            background: linear-gradient(135deg, #090D16 0%, #0D9488 100%);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 16px;
            padding: 28px 32px;
            color: #FFFFFF;
            margin-bottom: 22px;
            box-shadow: 0 10px 24px -6px rgba(0, 0, 0, 0.4);
            position: relative;
            overflow: hidden;
        }

        .hero-title {
            font-size: 2rem;
            font-weight: 700;
            color: #FFFFFF !important;
            margin-bottom: 6px;
            letter-spacing: -0.3px;
        }

        .hero-subtitle {
            font-size: 0.95rem;
            color: #E5E7EB !important;
            font-weight: 400;
            margin-bottom: 16px;
            max-width: 720px;
            line-height: 1.5;
        }

        /* Primary Buttons */
        .stButton > button {
            background: #0D9488 !important;
            color: #FFFFFF !important;
            border: none !important;
            border-radius: 10px !important;
            padding: 10px 22px !important;
            font-weight: 600 !important;
            font-size: 0.88rem !important;
            box-shadow: 0 2px 8px rgba(13, 148, 136, 0.3) !important;
            transition: all 0.2s ease !important;
        }

        .stButton > button:hover {
            background: #14B8A6 !important;
            box-shadow: 0 4px 14px rgba(20, 184, 166, 0.4) !important;
            transform: translateY(-1px) !important;
            color: #FFFFFF !important;
        }

        /* Metric / KPI Cards */
        .kpi-card {
            background: #1F2937;
            border-radius: 12px;
            padding: 14px 16px;
            border: 1px solid rgba(255, 255, 255, 0.06);
            border-left: 4px solid #14B8A6;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
            margin-bottom: 12px;
            transition: all 0.2s ease;
        }

        .kpi-card:hover {
            box-shadow: 0 4px 14px rgba(0, 0, 0, 0.3);
            border-color: rgba(255, 255, 255, 0.12);
        }

        .kpi-title {
            font-size: 0.75rem;
            color: #9CA3AF !important;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.4px;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }

        .kpi-value {
            font-size: 1.3rem;
            font-weight: 700;
            color: #F9FAFB !important;
            margin: 4px 0;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }

        .kpi-subtitle {
            font-size: 0.75rem;
            color: #14B8A6 !important;
            font-weight: 500;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }

        /* Badges */
        .badge-gold {
            background: rgba(245, 158, 11, 0.15);
            color: #F59E0B !important;
            padding: 4px 10px;
            border-radius: 10px;
            font-size: 0.75rem;
            font-weight: 600;
            display: inline-block;
            border: 1px solid rgba(245, 158, 11, 0.3);
        }

        .badge-emerald {
            background: rgba(20, 184, 166, 0.15);
            color: #14B8A6 !important;
            padding: 4px 10px;
            border-radius: 10px;
            font-size: 0.75rem;
            font-weight: 600;
            display: inline-block;
            border: 1px solid rgba(20, 184, 166, 0.3);
        }

        /* Stepper UI */
        .stepper-wrapper {
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: #111827;
            padding: 10px 18px;
            border-radius: 12px;
            margin-bottom: 18px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
            border: 1px solid rgba(255, 255, 255, 0.08);
            overflow-x: auto;
        }

        .step-item {
            display: flex;
            align-items: center;
            font-size: 0.8rem;
            font-weight: 500;
            color: #9CA3AF !important;
            white-space: nowrap;
        }

        .step-item.active {
            color: #14B8A6 !important;
            font-weight: 700;
        }

        .step-item.completed {
            color: #F9FAFB !important;
            font-weight: 600;
        }

        .step-icon {
            width: 20px;
            height: 20px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-right: 6px;
            font-size: 0.72rem;
            font-weight: 700;
        }

        .step-item.completed .step-icon {
            background-color: #0D9488;
            color: white;
        }

        .step-item.active .step-icon {
            background-color: #F59E0B;
            color: #0F172A;
        }

        .step-item.pending .step-icon {
            background-color: #1F2937;
            color: #6B7280;
        }

        /* Tabs styling */
        .stTabs [data-baseweb="tab-list"] {
            gap: 8px;
            background-color: transparent;
        }

        .stTabs [data-baseweb="tab"] {
            height: 40px;
            border-radius: 8px;
            background-color: #1F2937;
            border: 1px solid rgba(255, 255, 255, 0.08);
            padding: 0 16px;
            color: #9CA3AF;
            font-weight: 500;
            font-size: 0.85rem;
        }

        .stTabs [aria-selected="true"] {
            background-color: #0D9488 !important;
            color: #FFFFFF !important;
            border-color: #14B8A6 !important;
        }

        /* Plotly Chart Container Background */
        .js-plotly-plot .plotly .main-svg {
            border-radius: 10px;
        }
        </style>
    """, unsafe_allow_html=True)

def render_progress_stepper(current_step: int):
    """
    Renders a responsive, clean progress stepper for 6 steps.
    """
    steps = [
        "Home",
        "Dataset Insights",
        "Market Analysis",
        "Model Training",
        "Price Estimator",
        "Project Summary"
    ]
    
    html = '<div class="stepper-wrapper">'
    for idx, name in enumerate(steps, 1):
        if idx < current_step:
            status = "completed"
            icon = "✓"
        elif idx == current_step:
            status = "active"
            icon = str(idx)
        else:
            status = "pending"
            icon = str(idx)
            
        html += f'''
            <div class="step-item {status}">
                <div class="step-icon">{icon}</div>
                <span>{name}</span>
            </div>
        '''
        if idx < len(steps):
            html += '<div style="margin: 0 6px; color: #4B5563; align-self: center; font-size: 0.75rem;">→</div>'
            
    html += '</div>'
    st.markdown(html, unsafe_allow_html=True)

def render_header(title: str, subtitle: str, icon: str = "🏠"):
    """
    Renders standardized top banner across pages.
    """
    st.markdown(f'''
        <div class="hero-banner">
            <div style="font-size: 1.7rem; font-weight: 700; display: flex; align-items: center; gap: 10px;">
                <span>{icon}</span> <span style="color: #FFFFFF;">{title}</span>
            </div>
            <div class="hero-subtitle">{subtitle}</div>
            <div style="display: flex; gap: 8px; flex-wrap: wrap;">
                <span class="badge-gold">AI Valuation</span>
                <span class="badge-emerald">Real Estate Intelligence</span>
                <span class="badge-gold">Enterprise ML</span>
            </div>
        </div>
    ''', unsafe_allow_html=True)

def render_kpi_card(title: str, value: str, subtitle: str = "", icon: str = "📊", color_theme: str = "#14B8A6"):
    """
    Renders a clean dark KPI metric card with text truncation protection.
    """
    st.markdown(f'''
        <div class="kpi-card" style="border-left-color: {color_theme};">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <span class="kpi-title">{title}</span>
                <span style="font-size: 1.05rem;">{icon}</span>
            </div>
            <div class="kpi-value">{value}</div>
            <div class="kpi-subtitle" style="color: {color_theme};">{subtitle}</div>
        </div>
    ''', unsafe_allow_html=True)

def render_sidebar():
    """
    Renders clean sidebar elements.
    """
    with st.sidebar:
        st.markdown('''
            <div style="text-align: center; padding: 12px 0 18px 0;">
                <div style="font-size: 2.2rem;">🏠</div>
                <div style="font-size: 1.2rem; font-weight: 700; color: #FFFFFF;">HomeValue AI</div>
                <div style="font-size: 0.7rem; color: #F59E0B; font-weight: 600; letter-spacing: 0.5px;">PROPERTY VALUATION ENGINE</div>
            </div>
        ''', unsafe_allow_html=True)
        st.divider()
        st.markdown('''
            <div style="background: rgba(255,255,255,0.04); padding: 12px; border-radius: 10px; margin-bottom: 14px; border: 1px solid rgba(255,255,255,0.08);">
                <div style="font-size: 0.72rem; color: #9CA3AF; font-weight: 600; letter-spacing: 0.5px;">PLATFORM STATS</div>
                <div style="display: flex; justify-content: space-between; margin-top: 8px;">
                    <span style="color: #D1D5DB; font-size: 0.8rem;">Engine</span>
                    <span style="color: #F59E0B; font-weight: 600; font-size: 0.8rem;">Scikit/XGBoost</span>
                </div>
                <div style="display: flex; justify-content: space-between; margin-top: 4px;">
                    <span style="color: #D1D5DB; font-size: 0.8rem;">Dashboard</span>
                    <span style="color: #14B8A6; font-weight: 600; font-size: 0.8rem;">Interactive</span>
                </div>
                <div style="display: flex; justify-content: space-between; margin-top: 4px;">
                    <span style="color: #D1D5DB; font-size: 0.8rem;">Mode</span>
                    <span style="color: #3B82F6; font-weight: 600; font-size: 0.8rem;">AI Explainable</span>
                </div>
            </div>
        ''', unsafe_allow_html=True)
