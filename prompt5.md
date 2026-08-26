# Prompt 5 – House Price Estimator

You are continuing the project:

🏠 HomeValue AI – AI-Powered House Price Prediction Platform

Completed Modules

✅ Home Dashboard

✅ Dataset Insights

✅ Real Estate Market Analysis

✅ AI Model Training & Comparison

Before writing any code

1. Read the existing project structure.
2. Reuse helper functions.
3. Never rewrite previous modules.
4. Maintain the HomeValue AI UI.
5. Follow modular architecture.
6. Only create files required for this module.

Do NOT create the Summary page.

Only build the House Price Estimator module.

Stop after completion.

------------------------------------------------------------

OBJECTIVE

Create a premium AI-powered Property Valuation page.

Users should enter property details.

The trained model predicts the estimated market value.

Display prediction in a beautiful property valuation dashboard.

This page should look like a commercial real estate platform.

------------------------------------------------------------

PAGE TITLE

🏡 House Price Estimator

Subtitle

Estimate the market value of your property using Artificial Intelligence.

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

Cards

White

Dark Sidebar

#0F172A

Rounded Corners

22px

Soft Shadows

Responsive

------------------------------------------------------------

PAGE LAYOUT

Progress Stepper

↓

Property Details Form

↓

AI Prediction

↓

Property Summary

↓

Price Influencing Factors

↓

Investment Recommendation

↓

Download Valuation Report

------------------------------------------------------------

PROGRESS

Display

✅ Home

✅ Dataset Insights

✅ Market Analysis

✅ Model Training

🟢 House Price Estimator

⚪ Summary

------------------------------------------------------------

PROPERTY DETAILS FORM

Organize into sections.

SECTION 1

🏠 Basic Information

Area (sq.ft)

Bedrooms

Bathrooms

Stories

Parking

------------------------------------------------------------

SECTION 2

📍 Property Information

Main Road Access

Guest Room

Basement

Hot Water Heating

Air Conditioning

Preferred Area

Furnishing Status

------------------------------------------------------------

SECTION 3

⚙ Additional Features

Input validation

Default values

Reset button

------------------------------------------------------------

PREDICT BUTTON

Button

🏠 Estimate Property Value

Run prediction only when clicked.

------------------------------------------------------------

AI PREDICTION RESULT

Display a premium prediction card.

Example

═══════════════════════════════════════

🏠 Estimated Market Value

₹82,45,000

Model Used

Random Forest Regressor

Prediction Confidence

★★★★★

Generated Successfully

═══════════════════════════════════════

------------------------------------------------------------

PROPERTY SUMMARY

Display

Area

Bedrooms

Bathrooms

Parking

Stories

Predicted Price

Price per sq.ft

Prediction Time

------------------------------------------------------------

PRICE INFLUENCING FACTORS

Load feature importance from trained model.

Display

Top 10 most important features.

Interactive horizontal bar chart.

If model is Linear Regression

Display coefficients.

------------------------------------------------------------

PROPERTY VALUE METER

Create a gauge chart.

Ranges

Budget

Affordable

Premium

Luxury

Highlight predicted value.

------------------------------------------------------------

INVESTMENT RECOMMENDATION

Generate rule-based recommendations.

Examples

Excellent investment opportunity.

Property has premium features.

Large area contributes significantly to price.

Parking increases market value.

Good resale potential.

No AI.

Rule-based only.

------------------------------------------------------------

PROPERTY REPORT

Generate a professional report card.

Display

═══════════════════════════════

PROPERTY VALUATION REPORT

Estimated Price

Property Features

Model Used

Prediction Confidence

Generated Date

Recommendation

═══════════════════════════════

------------------------------------------------------------

DOWNLOAD

Allow users to download

Property Report (PDF)

Prediction Summary (CSV)

------------------------------------------------------------

VISUALIZATIONS

Plotly only.

Generate

Feature Importance

Gauge Chart

Property Summary Card

Prediction Card

------------------------------------------------------------

BUTTONS

Previous

↓

Model Training

Next

↓

Project Summary

------------------------------------------------------------

FOLDER STRUCTURE

pages/

5_House_Price_Estimator.py

modules/

prediction.py

valuation.py

report_generator.py

recommendation.py

utils/

prediction_helpers.py

------------------------------------------------------------

CREATE REUSABLE FUNCTIONS

load_saved_model()

preprocess_input()

predict_price()

calculate_price_per_sqft()

generate_recommendation()

generate_property_report()

download_pdf_report()

download_csv()

------------------------------------------------------------

SESSION STATE

Store

Prediction

Property Details

Model Name

Prediction Time

Recommendation

Report

Reuse on Summary page.

------------------------------------------------------------

PERFORMANCE

Load model once.

Cache model.

Fast prediction.

------------------------------------------------------------

ERROR HANDLING

Handle

Model Missing

Invalid Inputs

Prediction Failure

Missing Features

Never crash.

Display friendly messages.

------------------------------------------------------------

CODING STANDARDS

PEP8

Type Hints

Reusable Components

Responsive Design

Professional UI

------------------------------------------------------------

ACCEPTANCE CRITERIA

Prediction works.

Property summary displayed.

Feature importance displayed.

Gauge chart displayed.

Recommendation generated.

PDF report downloadable.

Responsive design.

Premium real estate UI.

Do NOT create Summary page.

Stop after completion.

Wait for Prompt 6.