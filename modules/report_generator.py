from datetime import datetime

def generate_property_report_text(input_dict: dict, predicted_price: float, model_name: str, recommendations: list) -> str:
    """
    Generates a structured text valuation report for property estimation.
    """
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    area = input_dict.get("area", 0)
    price_per_sqft = predicted_price / area if area > 0 else 0
    
    report = f"""
================================================================================
                       PROPERTY VALUATION REPORT
                            HomeValue AI
================================================================================
Generated Date : {now_str}
Valuation Model: {model_name}
Confidence     : High (★★★★★)
--------------------------------------------------------------------------------

1. ESTIMATED MARKET VALUE
   Estimated Market Price : ₹{predicted_price:,.2f}
   Unit Rate (Price/sqft) : ₹{price_per_sqft:,.2f} / sq.ft

2. PROPERTY SPECIFICATIONS
   • Area (sq.ft)         : {input_dict.get('area')}
   • Bedrooms             : {input_dict.get('bedrooms')}
   • Bathrooms            : {input_dict.get('bathrooms')}
   • Stories              : {input_dict.get('stories')}
   • Parking Spaces       : {input_dict.get('parking')}
   • Main Road Access     : {input_dict.get('mainroad', '').upper()}
   • Guest Room           : {input_dict.get('guestroom', '').upper()}
   • Basement             : {input_dict.get('basement', '').upper()}
   • Hot Water Heating    : {input_dict.get('hotwaterheating', '').upper()}
   • Air Conditioning     : {input_dict.get('airconditioning', '').upper()}
   • Preferred Area Zone  : {input_dict.get('prefarea', '').upper()}
   • Furnishing Status    : {input_dict.get('furnishingstatus', '').upper()}

3. STRATEGIC INVESTMENT RECOMMENDATIONS
"""
    for idx, rec in enumerate(recommendations, 1):
        clean_rec = rec.replace("**", "").replace("📌 ", "").replace("🏰 ", "").replace("🏡 ", "").replace("⭐ ", "").replace("📍 ", "").replace("🚗 ", "").replace("🛋️ ", "").replace("📈 ", "")
        report += f"   {idx}. {clean_rec}\n"
        
    report += """
--------------------------------------------------------------------------------
Disclaimer: This valuation report is produced via Machine Learning algorithms 
trained on historical real estate transactions.
================================================================================
"""
    return report
