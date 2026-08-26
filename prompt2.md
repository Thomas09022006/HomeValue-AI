# Prompt 2 – Dataset Insights

You are continuing the HomeValue AI – AI-Powered House Price Prediction Platform.

Completed Modules

✅ Home Dashboard

Before writing any code:

1. Read the existing project structure.
2. Never rewrite previous modules.
3. Maintain the same UI theme.
4. Follow modular architecture.
5. Only create files required for this module.

Do NOT implement EDA.

Do NOT implement Model Training.

Do NOT implement Prediction.

Only build the Dataset Insights module.

Stop after completion.

------------------------------------------------------------

OBJECTIVE

Create a beautiful Dataset Insights page.

This page should help users understand the housing dataset before any machine learning begins.

This is NOT an EDA page.

Only perform data profiling.

------------------------------------------------------------

PAGE TITLE

📊 Dataset Insights

Subtitle

Explore and understand the housing dataset before training machine learning models.

------------------------------------------------------------

DESIGN REQUIREMENTS

Continue using the HomeValue AI design language.

Theme

Premium Real Estate Platform

Primary

Emerald Green (#0F766E)

Secondary

Royal Gold (#D4A017)

Accent

Sky Blue (#3B82F6)

Background

#F8FAFC

Cards

White Glassmorphism

Sidebar

Dark Slate (#0F172A)

Rounded Corners

22px

Professional Icons

Soft Shadows

Modern Layout

Responsive

------------------------------------------------------------

PAGE LAYOUT

Progress Stepper

↓

Dataset Upload

↓

Dataset Status

↓

Dataset Overview

↓

Data Quality

↓

Feature Information

↓

Statistics

↓

Target Variable

↓

Sample Data

↓

Recommendations

↓

Continue to EDA

------------------------------------------------------------

PROGRESS

Display

🟢 Home

🟢 Dataset Insights

⚪ Exploratory Data Analysis

⚪ Model Training

⚪ Price Prediction

⚪ Summary

------------------------------------------------------------

DATASET

Allow

CSV Upload

or

Use Default Housing Dataset

Supported

California Housing

or

House Price Dataset

Accept only CSV.

------------------------------------------------------------

AFTER DATASET LOAD

Store dataset in Session State.

Never reload unnecessarily.

------------------------------------------------------------

DATASET STATUS

Beautiful KPI Cards

Display

Total Rows

Total Columns

Missing Values

Duplicate Rows

Memory Usage

Target Variable

------------------------------------------------------------

DATASET OVERVIEW

Display

Dataset Shape

Column Names

Data Types

Categorical Features

Numerical Features

------------------------------------------------------------

DATA QUALITY SCORE

Generate score

Out of

100

Factors

Missing Values

Duplicates

Invalid Data Types

Display

Excellent

Good

Needs Cleaning

------------------------------------------------------------

FEATURE INFORMATION

For every feature

Display

Feature Name

Data Type

Unique Values

Missing Values

Example Value

Description

Scrollable Table

------------------------------------------------------------

SUMMARY STATISTICS

Display

Mean

Median

Minimum

Maximum

Standard Deviation

25%

50%

75%

Interactive Table

------------------------------------------------------------

TARGET VARIABLE

Display

House Price

Minimum Price

Maximum Price

Average Price

Median Price

Price Distribution Summary

------------------------------------------------------------

SAMPLE DATA

Display

First 10 Rows

Scrollable

Read Only

------------------------------------------------------------

SMART RECOMMENDATIONS

Automatically generate recommendations.

Examples

Dataset has no missing values.

Area has high variance.

Price column has outliers.

No duplicate rows found.

Dataset ready for EDA.

Rule-based only.

No AI.

------------------------------------------------------------

DOWNLOAD

Allow

Download Clean Dataset

CSV

------------------------------------------------------------

BUTTONS

Previous

↓

Home

Next

↓

Exploratory Data Analysis

------------------------------------------------------------

FOLDER STRUCTURE

pages/

2_Dataset_Insights.py

modules/

dataset_profile.py

dataset_validation.py

summary.py

utils/

dataset_helpers.py

------------------------------------------------------------

CREATE REUSABLE FUNCTIONS

load_dataset()

validate_dataset()

calculate_memory()

calculate_quality_score()

feature_summary()

summary_statistics()

generate_recommendations()

download_dataset()

------------------------------------------------------------

SESSION STATE

Store

Dataset

Target Column

Feature Names

Numerical Columns

Categorical Columns

Quality Score

Do not recompute after page refresh.

------------------------------------------------------------

PERFORMANCE

Use Streamlit cache.

Avoid repeated dataset loading.

------------------------------------------------------------

ERROR HANDLING

Handle

No Dataset

Invalid CSV

Missing Target Column

Empty Dataset

Corrupted File

Never crash.

Display friendly messages.

------------------------------------------------------------

VISUALIZATIONS

Use Plotly only.

Generate

Missing Values Chart

Feature Type Pie Chart

Price Distribution Histogram

Dataset Composition Chart

------------------------------------------------------------

CODING STANDARDS

PEP8

Type Hints

Reusable Components

Professional UI

Responsive Layout

------------------------------------------------------------

ACCEPTANCE CRITERIA

Dataset loads successfully.

Dataset profiling completed.

Quality score displayed.

Feature summary displayed.

Statistics generated.

Recommendations generated.

Download works.

Responsive design.

Do NOT create EDA.

Do NOT create Model Training.

Do NOT create Prediction.

Stop after completion.

Wait for Prompt 3.