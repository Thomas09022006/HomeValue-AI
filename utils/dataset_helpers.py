import os
import pandas as pd
import numpy as np
import streamlit as st

@st.cache_data
def load_default_housing_dataset() -> pd.DataFrame:
    """
    Loads the default housing dataset from data/housing.csv.
    """
    filepath = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "housing.csv")
    if os.path.exists(filepath):
        df = pd.read_csv(filepath)
    else:
        # Fallback synthetic dataset generator if file is missing
        np.random.seed(42)
        n = 200
        areas = np.random.randint(1500, 10000, size=n)
        bedrooms = np.random.randint(1, 6, size=n)
        bathrooms = np.random.randint(1, 4, size=n)
        stories = np.random.randint(1, 4, size=n)
        prices = areas * 800 + bedrooms * 150000 + bathrooms * 250000 + np.random.randint(-100000, 100000, size=n)
        df = pd.DataFrame({
            "price": prices,
            "area": areas,
            "bedrooms": bedrooms,
            "bathrooms": bathrooms,
            "stories": stories,
            "mainroad": np.random.choice(["yes", "no"], size=n),
            "guestroom": np.random.choice(["yes", "no"], size=n),
            "basement": np.random.choice(["yes", "no"], size=n),
            "hotwaterheating": np.random.choice(["yes", "no"], size=n),
            "airconditioning": np.random.choice(["yes", "no"], size=n),
            "parking": np.random.randint(0, 3, size=n),
            "prefarea": np.random.choice(["yes", "no"], size=n),
            "furnishingstatus": np.random.choice(["furnished", "semi-furnished", "unfurnished"], size=n)
        })
    return df

def calculate_memory(df: pd.DataFrame) -> str:
    """
    Calculates memory usage of a DataFrame in KB or MB string format.
    """
    bytes_used = df.memory_usage(deep=True).sum()
    if bytes_used < 1024 * 1024:
        return f"{bytes_used / 1024:.2f} KB"
    return f"{bytes_used / (1024 * 1024):.2f} MB"

def get_feature_description(feature_name: str) -> str:
    """
    Returns standard human-readable descriptions for real estate features.
    """
    descriptions = {
        "price": "Market listing / target property price (in ₹)",
        "area": "Total property footprint floor space (in sq.ft)",
        "bedrooms": "Total number of bedroom spaces",
        "bathrooms": "Total number of full bathrooms",
        "stories": "Number of architectural building floors/levels",
        "mainroad": "Direct accessibility connection to main arterial road",
        "guestroom": "Availability of designated guest quarters",
        "basement": "Presence of finished/unfinished basement foundation space",
        "hotwaterheating": "Dedicated central hot water heating infrastructure",
        "airconditioning": "Integrated central HVAC air conditioning system",
        "parking": "Designated garage/driveway parking spaces count",
        "prefarea": "Located in prime/preferred neighborhood zone",
        "furnishingstatus": "Furnishing level (furnished, semi-furnished, unfurnished)"
    }
    return descriptions.get(feature_name.lower(), "Property attribute variable")
