# Prompt 4 – AI Model Training & Comparison

You are continuing the project:

🏠 HomeValue AI – AI-Powered House Price Prediction Platform

Completed Modules

✅ Home Dashboard

✅ Dataset Insights

✅ Real Estate Market Analysis

Before writing any code

1. Read the existing project structure.
2. Reuse helper functions.
3. Never rewrite previous modules.
4. Maintain the HomeValue AI UI.
5. Follow modular architecture.
6. Only create files required for this module.

Do NOT implement Prediction.

Do NOT implement Summary Page.

Only build the AI Model Training & Comparison module.

Stop after completion.

------------------------------------------------------------

OBJECTIVE

Create a complete Machine Learning dashboard for House Price Prediction.

Train multiple Regression models.

Compare their performance.

Automatically identify the best-performing model.

Save the trained model.

This module should demonstrate a complete Regression workflow.

------------------------------------------------------------

PAGE TITLE

🤖 AI Model Training

Subtitle

Train, evaluate and compare multiple regression algorithms for accurate property valuation.

------------------------------------------------------------

UI THEME

Continue HomeValue AI Theme.

Premium Real Estate Platform

Glassmorphism

Luxury

Modern

Professional

Primary

Emerald Green

#0F766E

Secondary

Royal Gold

#D4A017

Accent

Sky Blue

#3B82F6

Background

#F8FAFC

Rounded Cards

22px

Dark Sidebar

#0F172A

Responsive

------------------------------------------------------------

PAGE LAYOUT

Progress Stepper

↓

Dataset Summary

↓

Training Configuration

↓

Regression Models

↓

Train Models

↓

Training Progress

↓

Model Comparison

↓

Evaluation Metrics

↓

Prediction Accuracy

↓

Residual Analysis

↓

Feature Importance

↓

Best Model

↓

Save Model

↓

Continue to Prediction

------------------------------------------------------------

PROGRESS

Display

✅ Home

✅ Dataset Insights

✅ Market Analysis

🟢 Model Training

⚪ House Price Estimator

⚪ Summary

------------------------------------------------------------

DATASET SUMMARY

Display KPI Cards

Training Samples

Testing Samples

Features

Target Variable

Missing Values

Dataset Ready

------------------------------------------------------------

TRAINING CONFIGURATION

Display

Train-Test Split

80 / 20

Random State

42

Cross Validation

5 Fold

Evaluation Metrics

MAE

MSE

RMSE

R² Score

Display as beautiful cards.

------------------------------------------------------------

SUPPORTED MODELS

Allow users to choose models.

Checkboxes

☑ Linear Regression

☑ Decision Tree Regressor

☑ Random Forest Regressor

☑ XGBoost Regressor

All selected by default.

------------------------------------------------------------

TRAIN BUTTON

Button

🚀 Train Selected Models

Train only when clicked.

------------------------------------------------------------

TRAINING PROGRESS

Display

Progress Bar

Current Model

Elapsed Time

Training Completed

------------------------------------------------------------

MODEL COMPARISON TABLE

Columns

Model

MAE

MSE

RMSE

R² Score

Training Time

Sort by Highest R² Score.

Highlight Best Model.

------------------------------------------------------------

MODEL PERFORMANCE

For every model

Display

MAE

MSE

RMSE

R² Score

Cross Validation Score

------------------------------------------------------------

PREDICTED vs ACTUAL

Generate

Interactive Scatter Plot

X Axis

Actual Price

Y Axis

Predicted Price

Include Perfect Prediction Line.

------------------------------------------------------------

RESIDUAL ANALYSIS

Generate

Residual Plot

Residual Distribution Histogram

Interpretation Card

Explain

Good models have residuals centered around zero.

------------------------------------------------------------

FEATURE IMPORTANCE

Decision Tree

Random Forest

XGBoost

Display

Top 15 Features

Interactive Horizontal Bar Chart

For Linear Regression

Display Coefficients

Label clearly.

------------------------------------------------------------

BEST MODEL

Automatically select

Highest R² Score

Display

Model Name

R² Score

RMSE

Reason Selected

Training Time

------------------------------------------------------------

PROPERTY VALUATION SCORE

Create a beautiful card.

Example

Prediction Reliability

★★★★★

High Confidence Regression Model

------------------------------------------------------------

SAVE MODEL

Automatically save

Best Model

Scaler

Preprocessor

Feature Names

Use Joblib.

Display

Model Saved Successfully.

------------------------------------------------------------

DOWNLOAD

Allow users to download

Model Performance CSV

Evaluation Metrics CSV

Best Model (.joblib)

------------------------------------------------------------

BUTTONS

Previous

↓

Market Analysis

Next

↓

House Price Estimator

------------------------------------------------------------

VISUALIZATIONS

Use Plotly only.

Generate

Model Comparison Bar Chart

Actual vs Predicted Scatter Plot

Residual Plot

Residual Histogram

Feature Importance Chart

R² Score Comparison

Training Time Comparison

------------------------------------------------------------

FOLDER STRUCTURE

pages/

4_Model_Training.py

modules/

training.py

evaluation.py

comparison.py

feature_importance.py

save_model.py

utils/

training_helpers.py

------------------------------------------------------------

CREATE REUSABLE FUNCTIONS

train_linear_regression()

train_decision_tree()

train_random_forest()

train_xgboost()

evaluate_model()

compare_models()

plot_actual_vs_predicted()

plot_residuals()

plot_feature_importance()

select_best_model()

save_best_model()

------------------------------------------------------------

SESSION STATE

Store

Models

Best Model

Evaluation Metrics

Residual Data

Feature Importance

Training Summary

Saved Model Path

Reuse across pages.

------------------------------------------------------------

PERFORMANCE

Cache trained models.

Avoid retraining.

Train only when user clicks button.

------------------------------------------------------------

ERROR HANDLING

Handle

Missing Dataset

Training Errors

Missing Target Column

XGBoost Not Installed

Model Save Errors

Never crash.

Display friendly messages.

------------------------------------------------------------

CODING STANDARDS

PEP8

Type Hints

Docstrings

Reusable Components

Professional UI

Responsive Layout

------------------------------------------------------------

ACCEPTANCE CRITERIA

Regression models trained.

Comparison table generated.

Evaluation metrics displayed.

Residual analysis completed.

Predicted vs Actual plot generated.

Feature importance displayed.

Best model selected.

Best model saved.

Professional UI.

Responsive.

Do NOT create Prediction.

Do NOT create Summary.

Stop after completion.

Wait for Prompt 5.