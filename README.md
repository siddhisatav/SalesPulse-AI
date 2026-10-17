# 📈 SalesPulse AI — Retail Sales Forecasting & Analytics

**SalesPulse AI** is an interactive retail sales forecasting application built with Python, Machine Learning, and Streamlit. It analyzes historical retail sales patterns and predicts aggregate daily unit sales for a selected future period.

🔗 **Live Demo:** https://salespulse-ai.streamlit.app/  
💻 **GitHub Repository:** https://github.com/siddhisatav/SalesPulse-AI

## ✨ Project Highlights

- Forecast aggregate daily unit sales for 1–28 days, subject to available calendar coverage.
- Analyze historical sales data from the M5 retail dataset.
- Engineer date-based, lag, rolling-average, and event-related features.
- Compare five regression algorithms using MAE, RMSE, and R².
- Explore forecasts through an interactive dashboard, charts, and summary cards.
- Deploy the application using Streamlit Community Cloud.

## 🛠️ Tech Stack

- **Language:** Python
- **Data Analysis:** Pandas, NumPy
- **Machine Learning:** Scikit-learn
- **Dashboard:** Streamlit
- **Interactive Visualization:** Plotly
- **Model Storage:** Joblib / serialized model artifacts
- **Version Control:** Git and GitHub

## 📊 Dataset

The project uses the M5 retail sales dataset, including historical unit sales and calendar information.

The sales data is aggregated across the included products and stores by date.

**Forecast target:** `total_sales` — total units sold per day, not revenue in rupees.

## ⚙️ Workflow

1. **Data inspection:** Examine sales and calendar data for structure, missing values, duplicates, and sales patterns.
2. **Data preparation:** Aggregate product-store sales into daily total unit sales.
3. **Feature engineering:** Create calendar features, event indicators, historical lags, and rolling averages.
4. **Model training and comparison:** Evaluate Linear Regression, K-Nearest Neighbors, Decision Tree, Random Forest, and Gradient Boosting regressors.
5. **Model evaluation:** Compare models using Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), and R².
6. **Forecast generation:** Predict one day at a time and use each prediction to construct historical features for the next forecast day.
7. **Dashboard development:** Display forecast results, summary statistics, and model comparisons in Streamlit.

## 🧠 Feature Engineering

The forecasting pipeline uses the following feature groups:

**Calendar features**
- Year, month, day, day of week, and week of year
- Event-day indicator

**Historical sales features**
- Lag features: 1, 7, 14, and 28 days
- Rolling means: 7 and 28 days

Lag features capture earlier sales values, while rolling means summarize recent sales patterns. Historical features must be calculated without using future actual sales.

## 🤖 Models Evaluated

The project compares five regression models:

| Model | Purpose |
|---|---|
| Linear Regression | Establish a simple regression baseline |
| K-Nearest Neighbors | Compare predictions based on similar observations |
| Decision Tree | Capture nonlinear patterns |
| Random Forest | Combine multiple decision trees |
| Gradient Boosting | Build an ensemble sequentially to improve predictions |

**Final forecasting model:** Linear Regression in the current application.

The dashboard displays the evaluation metrics for the compared models. Lower MAE and RMSE generally indicate smaller prediction errors, while a higher R² generally indicates a better fit on the evaluated dataset.

## 📉 Dashboard Features

### Sales Forecast
- Select a forecasting horizon.
- Choose a supported forecast start date.
- Generate predicted daily unit sales.
- Review average, maximum, and total forecast values.
- Explore forecast results in a table and interactive chart.

### Model Performance
- Compare the five evaluated regression models.
- Review MAE, RMSE, and R².
- Explore the R² comparison chart.

## 🚀 Run Locally

### Prerequisites
- Python installed
- Git installed

### Installation

Clone the repository:

```bash
git clone https://github.com/siddhisatav/SalesPulse-AI.git
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

The application should open in your browser. The model artifacts and required data files must be present at the paths expected by the application.

## 📁 Project Structure

The repository contains the following main areas:

- `app/` — Streamlit application
- `data/raw/` — Raw sales and calendar data
- `data/processed/` — Processed daily sales data
- `final_models/` — Saved model and feature artifacts
- `notebooks/` — Dataset inspection, analysis, and model development notebooks
- `docs/` — Project documentation
- `requirements.txt` — Python dependencies

## ⚠️ Limitations
- Forecast dates are limited by the calendar data available to the application.
- Aggregate forecasts do not identify which individual product or store will generate the sales.

## 🔮 Future Improvements

- Evaluate performance across additional chronological test periods.
- Add forecast uncertainty estimates.
- Explore stronger seasonal and event-related features.
- Add store-level and product-level forecasting.
- Expand the dashboard with additional business insights.

## 👩‍💻 What I Learned

Through this project, I practiced data inspection, time-series feature engineering, regression model comparison, evaluation using multiple metrics, recursive forecasting, interactive dashboard development, and GitHub-based project deployment.

## Disclaimer

The forecasts are estimates based on historical data and available features. They are not guaranteed future sales.

---

**Built by Siddhi Satav**  
Computer Engineering Graduate | Data Analytics & Machine Learning
