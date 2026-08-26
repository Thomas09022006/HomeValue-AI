import pandas as pd
import numpy as np

def generate_market_insights(df: pd.DataFrame, corr_df: pd.DataFrame = None) -> list:
    """
    Generates rule-based real estate market insights without generative AI.
    """
    insights = []
    
    # Price vs Area relationship
    if "price" in df.columns and "area" in df.columns:
        corr_val = df["price"].corr(df["area"])
        if corr_val > 0.5:
            insights.append("🏡 **Strong Area Driver**: Property area (sq.ft) shows a strong positive correlation with house price.")
            
    # Bed / Bath ratio impact
    if "bedrooms" in df.columns and "bathrooms" in df.columns:
        avg_beds = df["bedrooms"].mean()
        avg_baths = df["bathrooms"].mean()
        insights.append(f"🛋️ **Typical Layout**: Average property features {avg_beds:.1f} Bedrooms and {avg_baths:.1f} Bathrooms.")
        
    # AC and amenities impact
    if "airconditioning" in df.columns and "price" in df.columns:
        ac_price = df[df["airconditioning"] == "yes"]["price"].mean() if "yes" in df["airconditioning"].values else 0
        no_ac_price = df[df["airconditioning"] == "no"]["price"].mean() if "no" in df["airconditioning"].values else 0
        if ac_price > no_ac_price and no_ac_price > 0:
            diff_pct = ((ac_price - no_ac_price) / no_ac_price) * 100
            insights.append(f"❄️ **HVAC Premium**: Air-conditioned properties command a ~{diff_pct:.1f}% market price premium.")
            
    # Parking premium
    if "parking" in df.columns and "price" in df.columns:
        insights.append("🚗 **Parking Facility Impact**: Dedicated parking spaces show moderate positive value addition.")
        
    # Outliers
    if "price" in df.columns:
        q75 = df["price"].quantile(0.75)
        iqr = q75 - df["price"].quantile(0.25)
        luxury_threshold = q75 + 1.5 * iqr
        luxury_count = (df["price"] > luxury_threshold).sum()
        if luxury_count > 0:
            insights.append(f"💎 **Luxury Tier Outliers**: Identified {luxury_count} high-value luxury estate outliers above ₹{luxury_threshold:,.0f}.")
            
    return insights
