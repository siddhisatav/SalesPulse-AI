import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.express as px

st.set_page_config(
    page_title="SalesPulse AI",
    page_icon="📈",
    layout="wide"
)

# -----------------------------
# Page configuration
# -----------------------------

# -----------------------------
# Sidebar
# -----------------------------

with st.sidebar:

    st.title("SalesPulse AI")

    st.caption(
        "Retail Sales Forecasting & Analytics"
    )

    st.divider()

    # Navigation
    page = st.radio(
        "Navigation",
        [
            "Sales Forecast",
            "Model Performance"
        ]
    )

    st.divider()

    # Project Information
    st.subheader("Project Info")

    st.write("**Dataset:** M5 Retail Sales")

    st.write(
        "**Goal:** Predict future retail sales "
        "using machine learning."
    )

    st.write(
        "**Models:** Linear Regression, KNN, "
        "Decision Tree, Random Forest, "
        "Gradient Boosting"
    )

    st.write(
        "**Features:** Date features, lag features, "
        "rolling statistics and event indicators."
    )

    st.write(
        "**Metrics:** MAE, RMSE and R²"
    )

    st.write(
        "**Technology:** Python, Pandas, NumPy, "
        "Scikit-learn, Joblib, Streamlit"
    )

    st.divider()

    st.caption(
        "SalesPulse AI | Machine Learning Project"
    )



st.markdown("""
<style>

    /* =========================
       GLOBAL APP
       ========================= */

    .stApp {
        background: #0b1120;
        color: #e5e7eb;
    }

    .main {
        background: #0b1120;
    }

    /* =========================
       MAIN TITLE
       ========================= */

    .main-title {
        font-size: 42px;
        font-weight: 750;
        color: #f8fafc;
        margin-bottom: 4px;
    }

    .subtitle {
        font-size: 16px;
        color: #94a3b8;
        margin-bottom: 30px;
    }

    /* =========================
       SECTION TITLES
       ========================= */

    .section-title {
        font-size: 24px;
        font-weight: 650;
        color: #f8fafc;
        margin-top: 28px;
        margin-bottom: 18px;
    }

    /* =========================
       SIDEBAR
       ========================= */

    section[data-testid="stSidebar"] {
        background: #070d1a;
        border-right: 1px solid #1e293b;
    }

    section[data-testid="stSidebar"] > div {
        background: #070d1a;
    }

    section[data-testid="stSidebar"] * {
        color: #e5e7eb;
    }

    /* Sidebar title */

    section[data-testid="stSidebar"] h1 {
        color: #f8fafc;
    }

    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3 {
        color: #f8fafc;
    }

    /* =========================
       CARDS
       ========================= */

    .info-card {
        background: #111827;
        padding: 22px;
        border-radius: 14px;
        border: 1px solid #1f2937;
        box-shadow: 0 4px 15px rgba(0,0,0,0.25);
        margin-bottom: 15px;
    }

    .card-title {
        font-size: 14px;
        color: #94a3b8;
        margin-bottom: 8px;
    }

    .card-value {
        font-size: 28px;
        font-weight: 700;
        color: #f8fafc;
    }

    /* =========================
       INPUT BOXES
       ========================= */

    div[data-baseweb="input"] {
        background-color: #111827;
        border: 1px solid #334155;
        border-radius: 9px;
    }

    div[data-baseweb="input"] input {
        color: #f8fafc;
    }

    div[data-baseweb="select"] > div {
        background-color: #111827;
        border: 1px solid #334155;
        border-radius: 9px;
    }

    /* =========================
        BUTTON
        ========================= */
    .stButton > button {
        width: 100%;
        background: linear-gradient(90deg, #6366f1, #06b6d4);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 12px 20px;
        font-weight: 650;
        font-size: 15px;
        transition: all 0.2s ease;
        box-shadow: 0 4px 14px rgba(99, 102, 241, 0.2);
    }

    .stButton > button:hover {
        background: linear-gradient(90deg, #4f46e5, #0891b2);
        color: white;
        border: none;
        transform: translateY(-2px);
        box-shadow: 0 6px 18px rgba(6, 182, 212, 0.25);
    }

    .stButton > button:hover {
        background: #4f46e5;
        color: white;
        border: none;
    }

    /* =========================
       SUCCESS MESSAGE
       ========================= */

    div[data-testid="stAlert"] {
        border-radius: 10px;
    }

    /* =========================
       DATAFRAME
       ========================= */

    div[data-testid="stDataFrame"] {
        border: 1px solid #1f2937;
        border-radius: 10px;
        overflow: hidden;
    }

    /* =========================
       METRICS
       ========================= */

        
    div[data-testid="stMetric"] {
        background: linear-gradient(145deg, #172338, #111827);
        border: 1px solid #334155;
        padding: 22px 20px;
        border-radius: 16px;
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.18);
        transition: all 0.2s ease;
    }

    div[data-testid="stMetricLabel"] {
        color: #94a3b8 !important;
        font-size: 14px;
    }

    div[data-testid="stMetricValue"] {
        color: #38bdf8 !important;
        font-size: 28px;
        font-weight: 700;
    }

    div[data-testid="stMetricLabel"] {
        color: #94a3b8;
    }

    div[data-testid="stMetricValue"] {
        color: #f8fafc;
    }

    /* =========================
       RADIO BUTTONS
       ========================= */

    div[role="radiogroup"] label {
        color: #cbd5e1;
    }

    /* =========================
       DIVIDERS
       ========================= */

    hr {
        border-color: #1e293b;
    }

</style>
""", unsafe_allow_html=True)
# st.title(" SalesPulse AI")
# st.write("Retail Sales Forecasting System")

# st.success("SalesPulse AI is running!")


from pathlib import Path
import joblib
import pandas as pd

# Find the main SalesPulse-AI folder
BASE_DIR = Path(__file__).resolve().parent.parent

# File paths
MODEL_PATH = BASE_DIR / "final_models" / "salespulse_final_model.pkl"
FEATURES_PATH = BASE_DIR / "final_models" / "salespulse_features.pkl"
SALES_PATH = BASE_DIR / "data" / "processed" / "daily_sales.csv"
CALENDAR_PATH = BASE_DIR / "data" / "raw" / "calendar.csv"

# Load model and features
final_model = joblib.load(MODEL_PATH)
features = joblib.load(FEATURES_PATH)

# Load data
sales = pd.read_csv(SALES_PATH)
sales["date"] = pd.to_datetime(sales["date"])

daily_sales = sales[["date", "total_sales"]].copy()
daily_sales = daily_sales.sort_values("date").reset_index(drop=True)

calendar = pd.read_csv(CALENDAR_PATH)


calendar["is_event_day"] = (
    calendar["event_name_1"].notna() |
    calendar["event_name_2"].notna()
).astype(int)



# daily_sales = daily_sales.merge(
#     calendar,
#     on="d",
#     how="left"



def forecast_future_sales(start_date, days):

    history = daily_sales[
        ["date", "total_sales"]
    ].copy()

    history = history.sort_values(
        "date"
    ).reset_index(drop=True)

    start_date = pd.to_datetime(start_date)

    future_dates = pd.date_range(
        start=start_date,
        periods=days,
        freq="D"
    )

    predictions = []

    for future_date in future_dates:

        # Get calendar information
        calendar_row = calendar[
            calendar["date"] == future_date
        ]

        if calendar_row.empty:
            raise ValueError(
                f"No calendar information available for {future_date.date()}"
            )

        is_event_day = int(
            calendar_row["is_event_day"].iloc[0]
        )

        # Calendar features
        year = future_date.year
        month = future_date.month
        day = future_date.day
        day_of_week = future_date.dayofweek
        week_of_year = int(
            future_date.isocalendar().week
        )

        # Lag features
        lag_1 = history["total_sales"].iloc[-1]
        lag_7 = history["total_sales"].iloc[-7]
        lag_14 = history["total_sales"].iloc[-14]
        lag_28 = history["total_sales"].iloc[-28]

        # Rolling features
        rolling_mean_7 = (
            history["total_sales"]
            .iloc[-7:]
            .mean()
        )

        rolling_mean_28 = (
            history["total_sales"]
            .iloc[-28:]
            .mean()
        )

        # Model input
        input_row = pd.DataFrame([{
            "year": year,
            "month": month,
            "day": day,
            "day_of_week": day_of_week,
            "week_of_year": week_of_year,
            "is_event_day": is_event_day,
            "lag_1": lag_1,
            "lag_7": lag_7,
            "lag_14": lag_14,
            "lag_28": lag_28,
            "rolling_mean_7": rolling_mean_7,
            "rolling_mean_28": rolling_mean_28
        }])

        # Keep exactly the training feature order
        input_row = input_row[features]

        # Prediction
        prediction = final_model.predict(
            input_row
        )[0]

        # Sales cannot be negative
        prediction = max(0, prediction)

        predictions.append({
            "date": future_date,
            "predicted_sales": prediction,
            "is_event_day": is_event_day
        })

        # Add prediction to history
        history.loc[len(history)] = [
            future_date,
            prediction
        ]

    return pd.DataFrame(predictions)


model_performance = pd.DataFrame({
    "Model": [
        "Linear Regression",
        "KNN",
        "Decision Tree",
        "Random Forest",
        "Gradient Boosting"
    ],
    "MAE": [
        2250.102672,
        3964.482517,
        4261.209790,
        2665.684476,
        2467.506393
    ],
    "RMSE": [
        3035.748428,
        4864.606859,
        5482.494442,
        3498.349726,
        3322.776623
    ],
    "R2": [
        0.805433,
        0.500389,
        0.365410,
        0.741618,
        0.766902
    ]
})

st.markdown("""
<div class="main-title">📈 SalesPulse AI</div>
<div class="subtitle">
    Retail Sales Forecasting & Analytics
    <br>
    Turn historical sales data into actionable insights.
</div>
""", unsafe_allow_html=True)




if page == "Sales Forecast":

        st.markdown(
            '<div class="section-title">Sales Forecast</div>',
            unsafe_allow_html=True
                )
        # Last date with actual sales
        daily_sales["date"] = pd.to_datetime(
            daily_sales["date"], errors="coerce"
        )
        sales_dates = pd.to_datetime(
            daily_sales["date"], errors="coerce"
        ).dropna()
        # Last date available in calendar
        calendar["date"] = pd.to_datetime(
            calendar["date"], errors="coerce"
        )
        calendar_dates = calendar["date"].dropna()

      
        sales_last_date = sales_dates.max().date()
        calendar_last_date = calendar_dates.max().date()

        # Forecast horizon
        forecast_days = st.number_input(
            "Forecast horizon (days)",
            min_value=1,
            max_value=28,
            value=7,
            step=1
        )


        # Earliest possible forecast date
        min_forecast_date = (
            sales_last_date + pd.Timedelta(days=1)
        )


        # Latest possible start date
        max_forecast_date = (
            calendar_last_date
            - pd.Timedelta(days=int(forecast_days) - 1)
        )


        if max_forecast_date < min_forecast_date:

            st.error(
                "The selected forecast horizon cannot be "
                "supported by the available calendar data."
            )

        else:

            forecast_date = st.date_input(
                "Select forecast start date",
                value=min_forecast_date,
                min_value=min_forecast_date,
                max_value=max_forecast_date
            )


       
        if st.button("Generate Forecast", use_container_width=True):

            forecast_start = pd.to_datetime(forecast_date)

            sales_last_date = daily_sales["date"].max()
            calendar_last_date = calendar["date"].max()

            forecast_end = (
                forecast_start
                + pd.Timedelta(days=int(forecast_days) - 1)
            )

            if forecast_start <= sales_last_date:

                st.error(
                    f"Please select a date after "
                    f"{sales_last_date.date()}."
                )

            elif forecast_end > calendar_last_date:

                st.error(
                    f"The selected forecast extends beyond "
                    f"the available M5 calendar data. "
                    f"Please choose fewer forecast days."
                )

            else:

                try:

                    forecast_result = forecast_future_sales(
                        forecast_date,
                        int(forecast_days)
                    )

                    st.success(
                        "Forecast generated successfully!"
                    )
                    
                    st.markdown(
                        '<div class="section-title">Forecast Summary</div>',
                        unsafe_allow_html=True
                    )

                    avg_sales = forecast_result["predicted_sales"].mean()
                    max_sales = forecast_result["predicted_sales"].max()
                    total_sales = forecast_result["predicted_sales"].sum()

                    col1, col2, col3 = st.columns(3)

                    with col1:
                        st.markdown(
                            f"""
                            <div class="info-card">
                                <div class="card-title">Average Forecast</div>
                                <div class="card-value">{avg_sales:,.0f}</div>
                            </div>
                            """,
                            unsafe_allow_html=True
                        )

                    with col2:
                        st.markdown(
                            f"""
                            <div class="info-card">
                                <div class="card-title">Maximum Forecast</div>
                                <div class="card-value">{max_sales:,.0f}</div>
                            </div>
                            """,
                            unsafe_allow_html=True
                        )

                    with col3:
                        st.markdown(
                            f"""
                            <div class="info-card">
                                <div class="card-title">Total Forecast</div>
                                <div class="card-value">{total_sales:,.0f}</div>
                            </div>
                            """,
                            unsafe_allow_html=True
                        )
                        
                    st.markdown(
                            '<div class="section-title">Forecast Results</div>',
                            unsafe_allow_html=True
                        )
                    st.dataframe(
                        forecast_result,
                        use_container_width=True
                    )
                                
                    st.markdown(
                        '<div class="section-title">Sales Forecast Trend</div>',
                        unsafe_allow_html=True
                    )

                                    
                    fig = px.line(
                        forecast_result,
                        x="date",
                        y="predicted_sales",
                        markers=True,
                        title="Predicted Daily Sales"
                    )

                    fig.update_traces(
                        line=dict(color="#38bdf8", width=3),
                        marker=dict(size=7, color="#22d3ee"),
                        hovertemplate=(
                            "<b>Date:</b> %{x|%d %b %Y}<br>"
                            "<b>Predicted Sales:</b> %{y:,.0f}"
                            "<extra></extra>"
                        )
                    )

                    fig.update_layout(
                        template="plotly_dark",
                        paper_bgcolor="#0b1120",
                        plot_bgcolor="#111827",
                        font=dict(color="#e5e7eb"),
                        title=dict(
                            text="Predicted Daily Sales",
                            font=dict(size=22)
                        ),
                        xaxis_title="Forecast Date",
                        yaxis_title="Predicted Units Sold",
                        hovermode="x unified",
                        margin=dict(l=20, r=20, t=65, b=20)
                    )

                    st.plotly_chart(fig, use_container_width=True)

                                        
                   

                except Exception as e:

                    st.error(
                        f"Unable to generate forecast: {e}"
                    )
                    
   
elif page == "Model Performance":

    st.header("Model Performance Comparison")

    
    st.markdown("""
    <p style="color:#94a3b8; font-size:15px; line-height:1.7;">
    Compare the models using three evaluation metrics:
    <br>
    <strong style="color:#38bdf8;">MAE</strong> — Average prediction error.
    <br>
    <strong style="color:#38bdf8;">RMSE</strong> — Gives more weight to larger errors.
    <br>
    <strong style="color:#38bdf8;">R² Score</strong> — Shows how well the model explains
    the variation in sales; a higher score is generally better.
    </p>
    """, unsafe_allow_html=True)


    st.dataframe(
        model_performance.style.format({
            "MAE": "{:,.2f}",
            "RMSE": "{:,.2f}",
            "R2": "{:.3f}"
        }),
        use_container_width=True
    )

        
    st.subheader("R² Comparison")

    fig = px.bar(
        model_performance.sort_values("R2", ascending=True),
        x="R2",
        y="Model",
        orientation="h",
        text="R2",
        title="Model Performance Comparison",
        color="R2",
        color_continuous_scale=["#334155", "#06b6d4", "#6366f1"]
    )

    fig.update_traces(
        texttemplate="%{text:.3f}",
        textposition="outside",
        hovertemplate="<b>%{y}</b><br>R² Score: %{x:.3f}<extra></extra>"
    )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="#0b1120",
        plot_bgcolor="#111827",
        font=dict(color="#e5e7eb"),
        xaxis_title="R² Score",
        yaxis_title="Model",
        xaxis=dict(range=[0, 1]),
        coloraxis_showscale=False,
        margin=dict(l=20, r=50, t=65, b=20)
    )

    st.plotly_chart(fig, use_container_width=True)


st.markdown("""
<hr style="border-color:#1e293b; margin-top:40px;">

<div style="text-align:center; color:#64748b; font-size:13px; padding:10px;">
    📈 <strong>SalesPulse AI</strong>
    <br>
    Retail Sales Forecasting & Analytics
    <br>
    Built with Python, Streamlit & Machine Learning
</div>
""", unsafe_allow_html=True)
