def get_project_architecture_tree() -> str:
    """
    Returns text folder tree structure of HomeValue AI.
    """
    return """
HomeValue-AI/
├── app.py
├── data/
│   └── housing.csv
├── pages/
│   ├── 1_Home.py
│   ├── 2_Dataset_Insights.py
│   ├── 3_EDA.py
│   ├── 4_Model_Training.py
│   ├── 5_House_Price_Estimator.py
│   └── 6_Project_Summary.py
├── modules/
│   ├── dataset_profile.py
│   ├── dataset_validation.py
│   ├── summary.py
│   ├── eda.py
│   ├── visualizations.py
│   ├── market_analysis.py
│   ├── insights.py
│   ├── training.py
│   ├── evaluation.py
│   ├── comparison.py
│   ├── feature_importance.py
│   ├── save_model.py
│   ├── prediction.py
│   ├── valuation.py
│   ├── report_generator.py
│   ├── recommendation.py
│   ├── deployment.py
│   └── project_info.py
├── utils/
│   ├── dataset_helpers.py
│   ├── eda_helpers.py
│   ├── training_helpers.py
│   ├── prediction_helpers.py
│   ├── summary_helpers.py
│   └── ui_helpers.py
├── models/
│   └── best_model.joblib
├── README.md
└── requirements.txt
"""
