
# SalesPulse AI — Project Overview

## 1. Project Name

SalesPulse AI — Sales Intelligence and Demand Forecasting Platform

## 2. Project Objective

The objective of this project is to analyze historical retail sales data, identify sales trends and patterns, and develop a machine learning model for demand forecasting.

The project will combine data analytics, SQL, Python, machine learning, and interactive dashboards.

## 3. Business Problem

Retail businesses need to understand product demand and sales performance to support inventory planning and business decisions.

This project aims to analyze historical sales data and estimate future product demand.

## 4. Technologies

- Python
- Pandas
- NumPy
- SQL/MySQL
- Scikit-learn
- Streamlit
- Plotly
- Git and GitHub

## 5. Main Project Modules

1. Data collection and validation
2. Data cleaning and preprocessing
3. Exploratory Data Analysis (EDA)
4. SQL-based sales analysis
5. Feature engineering
6. Demand forecasting
7. Interactive dashboard
8. Documentation and reporting

## 6. Expected Outcome

The project will provide sales insights, product and store performance analysis, and demand forecasts through an interactive application.

Actual model performance metrics and business findings will be added after completing the analysis.

## 7. Project Status

Current Status: Project setup

Last Updated: 2026-09-21

## Initial Dataset Inspection

### Calendar Dataset

- File Name: calendar.csv
- Number of Rows: 1,969
- Number of Columns: 14
- Dataset Shape: (1969, 14)
- Business Purpose: Provides date, event, and SNAP-related information.
- Date Range: To be verified.
- Missing Values: Missing values were found in event-related columns.
- Data Types: To be reviewed in detail.

### Initial Findings

1. The calendar dataset contains 1,969 rows and 14 columns.
2. It includes date information, weekday details, event information, and SNAP indicators.
3. The event-related columns contain missing values.
4. Missing event values may be expected because not every date has an event.
5. Further checks are required before deciding how to handle missing values.

### Inspection Status

Initial inspection completed using Pandas.

Next Step: Check data types, date range, duplicate records, and the complete missing-value report.


## Data Type and Missing Value Findings

### Data Types

The calendar dataset contains 14 columns:

- 7 integer columns
- 7 string columns

The date column is currently stored as a string and should be converted to a datetime format for date-based analysis.

The weekday and event-related columns are stored as strings because they contain categorical or text information.

### Missing Value Findings

Missing values were identified in the following columns:

| Column | Missing Values |
| event_name_1 | 1,807 |
| event_type_1 | 1,807 |
| event_name_2 | 1,964 |
| event_type_2 | 1,964 |

The missing values are concentrated in event-related columns. They may represent dates without events. The handling method will be decided after further analysis.

### Data Quality Observation

The calendar dataset contains complete values for the date, weekday, week, month, year, and SNAP indicator columns based on the initial non-null count inspection.


## Date Validation Findings

### Date Conversion

The original date column was stored as a string. It was converted into a datetime format using Pandas.

- Invalid date values: 0
- Date conversion status: Successful

### Date Range

- Minimum date: 2011-01-29
- Maximum date: 2016-06-19
- Total unique dates: 1,969

### Duplicate Date Check

- Duplicate dates: 0
- Result: Each date appears once in the calendar dataset.

### Conclusion

The date column passed the initial date validation checks. No invalid or duplicate dates were identified.