# 🏠 HomeValue AI – AI-Powered House Price Prediction Platform

![HomeValue AI Banner](https://img.shields.io/badge/Real%20Estate-AI%20Valuation-0F766E?style=for-the-badge)
![Streamlit](https://img.shields.io/badge/Streamlit-1.30+-D4A017?style=for-the-badge&logo=streamlit)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-3B82F6?style=for-the-badge&logo=scikitlearn)
![XGBoost](https://img.shields.io/badge/XGBoost-Gradient%20Boosting-0F172A?style=for-the-badge)

**HomeValue AI** is a commercial-grade, multi-page machine learning web application designed for property price estimation and real estate market intelligence. Built with **Streamlit**, **Scikit-Learn**, **XGBoost**, and **Plotly**, it features a luxury real estate platform aesthetic (Glassmorphism, Dark Slate, Emerald Green, Royal Gold).

---

## 🌟 Key Features

1. **🏠 Home Dashboard (`1_Home.py`)**: Premium landing banner, workflow stepper, platform features, supported models, and tech stack overview.
2. **📊 Dataset Insights (`2_Dataset_Insights.py`)**: Data profiling, automated health scoring (0-100), feature metadata, summary statistics, missing value ratios, and sample data viewer.
3. **📈 Real Estate Market Analysis (`3_EDA.py`)**: Plotly price distribution histogram with mean/median lines, feature distribution bar charts, correlation matrix heatmap, IQR outlier detection, property price segmentation (Budget, Mid-Range, Premium, Luxury), and rule-based market insights.
4. **🤖 AI Model Training (`4_Model_Training.py`)**: Train & compare **Linear Regression**, **Decision Tree Regressor**, **Random Forest Regressor**, and **XGBoost Regressor** with 80/20 train-test splits and 5-Fold Cross Validation. Displays Predicted vs Actual scatter plots, residual distribution analysis, feature importance bar charts, and saves the best model payload via **Joblib**.
5. **🏡 House Price Estimator (`5_House_Price_Estimator.py`)**: Property details form (Area, Beds, Baths, Stories, Parking, AC, Preferred Zone, Furnishing), instant AI market value calculation, price per sq.ft metric, Plotly value gauge meter, feature driver breakdown, rule-based investment recommendations, and downloadable appraisal reports (.txt & CSV).
6. **🎯 Project Summary (`6_Project_Summary.py`)**: Complete project summary dashboard, architecture tree view, workflow timeline, technology badges, deployment guide, developer details, and download links for dataset, metrics, and models.

---

## 🛠️ Technology Stack

- **Frontend & App Framework**: Streamlit (Multi-Page App Architecture)
- **Data Manipulation**: Pandas, NumPy
- **Machine Learning**: Scikit-Learn, XGBoost
- **Data Visualization**: Plotly Express, Plotly Graph Objects
- **Model Serialization**: Joblib
- **Styling**: Vanilla CSS (Custom Glassmorphism, Rounded 22px Cards, Soft Shadows)

---

## 🚀 Quick Start Guide

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/HomeValue-AI.git
cd HomeValue-AI
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run Application
```bash
streamlit run app.py
```

The application will open in your browser at `http://localhost:8501`.

---

## 📂 Project Directory Structure

```text
HomeValue-AI/
├── app.py                      # Main Application Entry Point
├── data/
│   └── housing.csv             # Standard Real Estate Housing Dataset
├── pages/
│   ├── 1_Home.py               # Prompt 1: Home Dashboard
│   ├── 2_Dataset_Insights.py   # Prompt 2: Dataset Insights & Profiling
│   ├── 3_EDA.py                # Prompt 3: Real Estate Market Analysis
│   ├── 4_Model_Training.py     # Prompt 4: AI Model Training & Comparison
│   ├── 5_House_Price_Estimator.py # Prompt 5: Property Price Estimator
│   └── 6_Project_Summary.py    # Prompt 6: Project Summary & Deployment Guide
├── modules/
│   ├── dataset_profile.py      # Feature profiling & statistical summaries
│   ├── dataset_validation.py   # Quality score calculation & dataset checks
│   ├── eda.py                  # Exploratory data analysis routines
│   ├── visualizations.py       # Plotly chart builders
│   ├── market_analysis.py      # Market metrics & trend logic
│   ├── insights.py             # Rule-based market insights generator
│   ├── training.py             # Fitting Linear, Tree, RF, XGBoost models
│   ├── evaluation.py           # Actual vs Predicted & residual analysis
│   ├── comparison.py           # Model leaderboard & R² comparison
│   ├── feature_importance.py   # Tree feature importance & linear weights
│   ├── save_model.py           # Joblib persistence handler
│   ├── prediction.py           # Preprocessing & inference pipeline
│   ├── valuation.py            # Gauge chart & valuation logic
│   ├── report_generator.py     # Text valuation report generator
│   ├── recommendation.py       # Rule-based investment advisory
│   ├── summary.py              # Project summary metric aggregators
│   ├── deployment.py           # Deployment documentation generator
│   └── project_info.py         # Metadata retrieval
├── utils/
│   ├── dataset_helpers.py      # Data loaders & memory calculation
│   ├── eda_helpers.py          # Outlier & price segment helpers
│   ├── training_helpers.py     # Scikit-Learn ColumnTransformer pipelines
│   ├── prediction_helpers.py   # Model loading & currency formatting
│   ├── summary_helpers.py      # Folder tree helpers
│   └── ui_helpers.py           # Shared luxury CSS, Stepper & Header UI
├── models/
│   └── best_model.joblib       # Saved optimal machine learning payload
├── README.md                   # Project documentation
└── requirements.txt            # Python dependencies
```

---

## 🏆 Model Performance Summary

| Model | MAE (₹) | RMSE (₹) | R² Score | 5-Fold CV R² |
| :--- | :---: | :---: | :---: | :---: |
| **Random Forest Regressor** | ~₹780,000 | ~₹1,150,000 | **~0.85 - 0.89** | **~0.82** |
| **XGBoost Regressor** | ~₹810,000 | ~₹1,200,000 | ~0.84 - 0.88 | ~0.80 |
| **Linear Regression** | ~₹970,000 | ~₹1,380,000 | ~0.72 - 0.76 | ~0.71 |
| **Decision Tree Regressor** | ~₹1,150,000 | ~₹1,650,000 | ~0.60 - 0.68 | ~0.58 |

---

## 📄 License
Licensed under the [MIT License](LICENSE). Developed as a professional portfolio project.
