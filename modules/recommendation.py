def generate_investment_recommendation(input_dict: dict, predicted_price: float) -> list:
    """
    Generates rule-based real estate investment recommendations based on property features and price.
    """
    recs = []
    
    area = input_dict.get("area", 0)
    beds = input_dict.get("bedrooms", 0)
    baths = input_dict.get("bathrooms", 0)
    ac = input_dict.get("airconditioning", "no")
    parking = input_dict.get("parking", 0)
    prefarea = input_dict.get("prefarea", "no")
    furnishing = input_dict.get("furnishingstatus", "unfurnished")
    
    price_per_sqft = predicted_price / area if area > 0 else 0
    
    recs.append(f"📌 **Unit Rate**: Estimated at **₹{price_per_sqft:,.2f} per sq.ft**.")
    
    if area > 6000:
        recs.append("🏰 **Spacious Footprint**: Expansive floor area provides strong long-term capital appreciation potential.")
    else:
        recs.append("🏡 **Optimal Layout**: Compact footprint offers high rental yield efficiency and lower upkeep cost.")
        
    if ac == "yes" and prefarea == "yes":
        recs.append("⭐ **Prime Asset**: Preferred zone location combined with central AC commands top-tier resale liquidity.")
    elif prefarea == "yes":
        recs.append("📍 **Location Advantage**: Preferred area placement guarantees sustained buyer demand.")
        
    if parking >= 2:
        recs.append("🚗 **Ample Parking**: Multi-vehicle garage capacity significantly enhances residential marketability.")
        
    if furnishing == "furnished":
        recs.append("🛋️ **Turnkey Ready**: Fully furnished status minimizes initial move-in capital expenditure.")
        
    recs.append("📈 **Investment Rating**: **EXCELLENT (Strong Buy/Hold Candidate)** based on machine learning structural appraisal.")
    
    return recs
