# Prompt 3 – Exploratory Data Analysis

You are continuing the project:

🏠 HomeValue AI – AI-Powered House Price Prediction Platform

Completed Modules

✅ Home Dashboard

✅ Dataset Insights

Before writing any code

1. Read the existing project structure.
2. Never rewrite previous modules.
3. Reuse helper functions.
4. Maintain the same UI design.
5. Follow modular architecture.
6. Only create files required for this module.

Do NOT implement Model Training.

Do NOT implement Prediction.

Only build the Exploratory Data Analysis module.

Stop after completion.

------------------------------------------------------------

OBJECTIVE

Create a premium Real Estate Analytics Dashboard.

This page should help users understand housing price patterns before building machine learning models.

Do NOT make this page look like a generic EDA notebook.

It should resemble professional business intelligence dashboards used by real estate companies.

------------------------------------------------------------

PAGE TITLE

📈 Real Estate Market Analysis

Subtitle

Analyze housing trends, property characteristics, feature relationships, and market insights before training machine learning models.

------------------------------------------------------------

UI THEME

Continue HomeValue AI Theme.

Design Style

Premium Real Estate Platform

Glassmorphism

Luxury

Modern

Professional

Color Palette

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

Sidebar

#0F172A

Rounded Corners

22px

Soft Shadows

Responsive

------------------------------------------------------------

PAGE LAYOUT

Progress Stepper

↓

Market Overview

↓

Price Distribution

↓

Property Feature Analysis

↓

Correlation Analysis

↓

Feature Relationships

↓

Outlier Detection

↓

Market Insights

↓

Summary

↓

Continue to Model Training

------------------------------------------------------------

PROGRESS

Display

✅ Home

✅ Dataset Insights

🟢 Market Analysis

⚪ Model Training

⚪ House Price Estimator

⚪ Summary

------------------------------------------------------------

MARKET OVERVIEW

Beautiful KPI Cards

Display

Average House Price

Median Price

Highest Price

Lowest Price

Average Area

Average Bedrooms

Average Bathrooms

------------------------------------------------------------

PRICE DISTRIBUTION

Interactive Plotly Histogram

Include

Mean Line

Median Line

Hover Information

Interpretation Card

Example

Most houses are priced between ₹40L and ₹70L.

------------------------------------------------------------

PROPERTY FEATURE ANALYSIS

Interactive Charts

Area Distribution

Bedroom Distribution

Bathroom Distribution

Stories Distribution

Parking Distribution

Use

Histograms

Bar Charts

Donut Charts

------------------------------------------------------------

PRICE vs FEATURES

Create Scatter Plots

Price vs Area

Price vs Bedrooms

Price vs Bathrooms

Price vs Stories

Price vs Parking

Include Trend Line

------------------------------------------------------------

CORRELATION ANALYSIS

Generate

Interactive Correlation Heatmap

Highlight

Strong Positive Correlations

Strong Negative Correlations

Display Top 5 Correlated Features.

------------------------------------------------------------

FEATURE RELATIONSHIPS

Generate

Pair Plot Alternative

Interactive Bubble Charts

Relationship Matrix

Feature Comparison Selector

Allow users to compare any two numerical features.

------------------------------------------------------------

OUTLIER DETECTION

Detect outliers using

IQR Method

Display

Outlier Count

Percentage

Interactive Box Plots

Highlight extreme values.

------------------------------------------------------------

MARKET INSIGHTS

Automatically generate rule-based insights.

Examples

Larger houses generally have higher prices.

Area has the strongest relationship with price.

Parking has a moderate influence.

Some luxury properties are clear outliers.

No Generative AI.

Rule-based only.

------------------------------------------------------------

PROPERTY PRICE SEGMENTS

Automatically classify properties into

Budget

Mid-Range

Premium

Luxury

Display

Pie Chart

Percentage

Average Price per Segment

------------------------------------------------------------

FEATURE IMPORTANCE PREVIEW

Using correlation only

Display

Top 10 features influencing price.

This is NOT machine learning feature importance.

Label it clearly as

Correlation-Based Importance.

------------------------------------------------------------

DATA QUALITY SUMMARY

Display

Missing Values

Duplicates

Outliers

Ready for Training

------------------------------------------------------------

VISUALIZATIONS

Use Plotly only.

Generate

Histogram

Scatter Plot

Correlation Heatmap

Box Plot

Pie Chart

Bar Chart

Bubble Chart

Donut Chart

All charts should follow the HomeValue AI color palette.

------------------------------------------------------------

BUTTONS

Previous

↓

Dataset Insights

Next

↓

Model Training

------------------------------------------------------------

FOLDER STRUCTURE

pages/

3_EDA.py

modules/

eda.py

visualizations.py

market_analysis.py

insights.py

utils/

eda_helpers.py

------------------------------------------------------------

CREATE REUSABLE FUNCTIONS

plot_price_distribution()

plot_feature_distribution()

plot_scatter_relationship()

generate_heatmap()

detect_outliers()

segment_properties()

generate_market_insights()

calculate_correlations()

------------------------------------------------------------

SESSION STATE

Store

Correlation Matrix

Outlier Summary

Market Insights

Price Segments

Visualization Data

Reuse across pages.

------------------------------------------------------------

PERFORMANCE

Cache expensive visualizations.

Avoid recalculating statistics.

------------------------------------------------------------

ERROR HANDLING

Handle

Missing Dataset

Invalid Columns

Empty Dataset

Visualization Errors

Never crash.

Display user-friendly messages.

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

Interactive market dashboard completed.

Price distribution visualized.

Feature relationships analyzed.

Correlation heatmap generated.

Outliers detected.

Market insights generated.

Price segmentation completed.

Responsive UI.

Professional real estate appearance.

Do NOT create Model Training.

Do NOT create Prediction.

Stop after completion.

Wait for Prompt 4.