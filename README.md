
# SalesPulse AI – Retail Sales Forecasting

 **Live App:** https://salespulse-ai.streamlit.app/

 **GitHub Repository:** https://github.com/siddhisatav/SalesPulse-AI

## 1. Project Overview

SalesPulse AI is a machine-learning-based retail sales forecasting application that predicts future daily sales using historical retail data.

The project demonstrates the complete workflow of a forecasting solution, including data preparation, feature engineering, model training, model evaluation, and interactive visualization using Streamlit.

## 2. Objectives

- Analyze historical retail sales patterns.
- Calculate total daily sales across products and stores.
- Create meaningful date-based and historical-sales features.
- Train and compare multiple regression models.
- Forecast future daily sales for a selected period.
- Display forecasts and model performance through an interactive dashboard.

## 3. Technology Stack

- **Programming language:** Python
- **Data analysis:** Pandas, NumPy
- **Machine learning:** Scikit-learn
- **Visualization:** Streamlit and the charting library used in the application
- **Data format:** CSV
- **Model storage:** Pickle (`.pkl`)

## 4. Dataset

The project uses the M5 retail sales dataset.

The relevant data files include:

- `sales_train_evaluation.csv` — historical unit sales for product-store combinations.
- `calendar.csv` — dates and calendar or event information.

The sales data is aggregated by date to calculate total daily sales across the included products and stores.

**Target variable:** `total_sales`

The target represents units sold, not sales revenue in currency.

## 5. Data Processing and Feature Engineering

The project uses 12 input features:

### Date-based features

- `year`
- `month`
- `day`
- `day_of_week`
- `week_of_year`
- `is_event_day`

### Historical-sales features

- `lag_1`
- `lag_7`
- `lag_14`
- `lag_28`
- `rolling_mean_7`
- `rolling_mean_28`

Date-based features capture calendar patterns. Lag features represent sales from earlier periods, while rolling means summarize recent historical sales.

Historical features should use only information available before the date being predicted.

## 6. Machine Learning Models

The project evaluates the following regression algorithms:

- Linear Regression
- K-Nearest Neighbors (KNN) Regressor
- Decision Tree Regressor
- Random Forest Regressor
- Gradient Boosting Regressor

Linear Regression is used as the saved final model in the current version of the project.

## 7. Model Evaluation

The models are evaluated using:

- **MAE (Mean Absolute Error):** measures the average absolute difference between actual and predicted sales.
- **RMSE (Root Mean Squared Error):** penalizes larger prediction errors more heavily.
- **R² Score:** measures the variation in sales explained by the model relative to a mean-prediction baseline.

Lower MAE and RMSE values generally indicate better predictions. An R² score closer to 1 generally indicates a better fit on the evaluated data.

The final reported metrics should be taken from the same evaluation run used by the deployed application.

## 8. Forecasting Approach

The application generates forecasts for a selected number of days, subject to the available calendar data.

It predicts one day at a time. Each prediction is added to the history used to calculate features for the next day. This is called recursive forecasting.

Because later predictions depend on earlier predictions, forecasting errors can accumulate over longer horizons.

## 9. Streamlit Application

The application provides two main sections:

### Sales Forecast

- Select the forecasting horizon.
- Choose a supported forecast start date.
- Generate daily sales predictions.
- View predicted sales in a table and chart.
- Review summary statistics for the forecast period.

### Model Performance

- Compare the evaluated regression models.
- Review MAE, RMSE, and R² scores.
- View model performance through a chart.

## 10. Project Structure

```text
SalesPulse-AI/
├── app/
│   └── app.py
├── data/
│   └── raw/
│       ├── calendar.csv
│       └── sales_train_evaluation.csv
├── models/
│   ├── salespulse_final_model.pkl
│   └── salespulse_features.pkl
├── notebooks/
├── README.md
├── requirements.txt
└── .gitignore
```

## 11. Installation and Execution

### Prerequisites

- Python
- Git (for repository management)
- Required packages listed in `requirements.txt`

### Setup

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd SalesPulse-AI
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application from the project root:

```bash
streamlit run app/app.py
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with the actual repository URL.

## 12. Limitations

- Forecasts depend on the quality and date coverage of the available data.
- Recursive forecasting can accumulate errors across multiple days.
- Predictions may not capture unexpected market changes or future events not represented in the input features.
- The current calendar coverage limits the dates that the application can forecast.

## 13. Future Improvements

- Evaluate the model across additional chronological test periods.
- Improve handling of seasonal patterns and special events.
- Add additional model diagnostics and forecast uncertainty estimates.
- Extend the application with more detailed store-level or product-level analysis where appropriate.

## 14. Conclusion

SalesPulse AI demonstrates an end-to-end retail sales forecasting workflow using Python, feature engineering, regression models, and Streamlit. It combines historical sales analysis with an interactive application for exploring future sales estimates.

## 15. Disclaimer

Forecasts are estimates based on historical patterns and available features. They should not be treated as guaranteed future sales.
