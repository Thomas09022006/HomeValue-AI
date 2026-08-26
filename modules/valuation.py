import plotly.graph_objects as go

def plot_property_value_gauge(predicted_price: float, min_price: float = 2000000, max_price: float = 15000000):
    """
    Creates a Plotly Gauge chart categorizing the valuation into Budget, Affordable, Premium, Luxury.
    """
    # Ensure min/max bounds encompass prediction
    if predicted_price > max_price:
        max_price = predicted_price * 1.2
    if predicted_price < min_price:
        min_price = predicted_price * 0.8
        
    range_step = (max_price - min_price) / 4
    b_limit = min_price + range_step
    a_limit = min_price + 2 * range_step
    p_limit = min_price + 3 * range_step
    
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = predicted_price,
        number = {'prefix': "₹", 'valueformat': ",.0f", 'font': {'size': 24, 'family': "Inter", 'color': "#F8FAFC"}},
        title = {'text': "<b>Property Value Tier Gauge</b>", 'font': {'size': 18, 'family': "Inter", 'color': "#14B8A6"}},
        gauge = {
            'axis': {'range': [min_price, max_price], 'tickwidth': 1, 'tickcolor': "#94A3B8"},
            'bar': {'color': "#F59E0B", 'thickness': 0.25},
            'bgcolor': "#161F30",
            'borderwidth': 1,
            'bordercolor': "#2A364F",
            'steps': [
                {'range': [min_price, b_limit], 'color': 'rgba(59, 130, 246, 0.35)'},
                {'range': [b_limit, a_limit], 'color': 'rgba(20, 184, 166, 0.35)'},
                {'range': [a_limit, p_limit], 'color': 'rgba(245, 158, 11, 0.35)'},
                {'range': [p_limit, max_price], 'color': 'rgba(139, 92, 246, 0.35)'}
            ]
        }
    ))
    
    fig.update_layout(
        template="plotly_dark",
        font_family="Inter",
        font_color="#F8FAFC",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=30, r=30, t=50, b=30)
    )
    return fig
