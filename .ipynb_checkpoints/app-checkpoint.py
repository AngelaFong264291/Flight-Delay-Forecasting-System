import streamlit as st
import pandas as pd
import numpy as np
import joblib
from datetime import datetime

# --- 1. LOAD MODEL AND DATA ---

# Load the trained CatBoost model
model = joblib.load('catboost_flight_delay_model.joblib')

# Load the cleaned dataset to get historical data for feature engineering
# We need to parse dates so we can filter by them correctly
try:
    df = pd.read_csv('flight_delay_data_cleaned.csv', parse_dates=['date'])
except FileNotFoundError:
    st.error("Error: The file 'flight_delay_data_cleaned.csv' was not found. Please run the Jupyter Notebook to generate it.")
    st.stop()


# --- 2. DEFINE THE USER INTERFACE (UI) ---

st.set_page_config(page_title="Flight Delay Forecaster", page_icon="✈️", layout="wide")

st.title("✈️ U.S. Flight Delay Forecaster")
st.markdown("Select a carrier, airport, and date to predict the average arrival delay per flight.")

# Create columns for a cleaner layout
col1, col2, col3 = st.columns(3)

# Get unique, sorted lists for dropdowns
carrier_options = sorted(df['carrier'].unique())
airport_options = sorted(df['airport'].unique())

with col1:
    selected_carrier = st.selectbox("Carrier Code", carrier_options, index=carrier_options.index('DL')) # Default to Delta

with col2:
    selected_airport = st.selectbox("Airport Code", airport_options, index=airport_options.index('ATL')) # Default to Atlanta

with col3:
    selected_date = st.date_input("Target Date", value=datetime(2022, 7, 1))

# Create a button to trigger the prediction
predict_button = st.button("Predict Average Delay")


# --- 3. BACKEND LOGIC: FEATURE ENGINEERING & PREDICTION ---

if predict_button:
    # Anchor the date to the first of the month, as our model was trained on monthly data
    target_date = pd.to_datetime(selected_date).replace(day=1)

    st.write("---") # Separator
    st.subheader(f"Forecasting for {selected_carrier} at {selected_airport} on {target_date.strftime('%B %Y')}...")

    # --- Recreate the EXACT same features the model was trained on ---
    
    # 1. Cyclical Time Features
    month = target_date.month
    month_sin = np.sin(2 * np.pi * month / 12)
    month_cos = np.cos(2 * np.pi * month / 12)

    # 2. COVID-19 Era Flag
    year = target_date.year
    is_covid_era = 1 if (year == 2020 and month >= 3) or (year == 2021) else 0

    # 3. Lag and Rolling Features (This is the most critical part!)
    # We need to find the most recent historical data for the selected carrier/airport
    # to derive the lag features from.
    
    # Lag 1 features come from the previous month
    lag_1_date = target_date - pd.DateOffset(months=1)
    
    # Lag 12 features come from the previous year
    lag_12_date = target_date - pd.DateOffset(years=1)
    
    # Rolling features need data from the past 3-6 months
    rolling_start_date = target_date - pd.DateOffset(months=6)

    # Filter the historical data for this specific carrier-airport pair
    historical_data = df[
        (df['carrier'] == selected_carrier) &
        (df['airport'] == selected_airport) &
        (df['date'] < target_date) # Only use data BEFORE the prediction date
    ].sort_values('date', ascending=False)
    
    if historical_data.empty:
        st.error(f"Not enough historical data for {selected_carrier} at {selected_airport} to make a prediction.")
        st.stop()

    # Get Lag 1 features from the most recent available month
    latest_data = historical_data.iloc[0]
    target_lag_1 = latest_data['target_avg_delay_per_flight']
    flights_lag_1 = latest_data['arr_flights']
    
    # Get Lag 12 feature
    lag_12_data = historical_data[historical_data['date'] == lag_12_date]
    if lag_12_data.empty:
        target_lag_12 = historical_data['target_avg_delay_per_flight'].mean() # Fallback to overall average
        st.warning("12-month lag data not available. Using historical average as a fallback.")
    else:
        target_lag_12 = lag_12_data['target_avg_delay_per_flight'].values[0]

    # Calculate Rolling Averages
    rolling_data = historical_data[historical_data['date'] >= rolling_start_date]
    rolling_3m_avg_delay = rolling_data['target_avg_delay_per_flight'].head(3).mean()
    rolling_6m_avg_delay = rolling_data['target_avg_delay_per_flight'].head(6).mean()

    # --- 4. ASSEMBLE FEATURES AND PREDICT ---
    
    # The order MUST match the `features` list from your notebook!
    features_list = [
        selected_carrier, selected_airport,
        month_sin, month_cos, is_covid_era,
        target_lag_1, target_lag_12, flights_lag_1,
        rolling_3m_avg_delay, rolling_6m_avg_delay
    ]
    
    # Create a DataFrame for the model input
    input_df = pd.DataFrame([features_list], columns=model.feature_names_)
    
    # Ensure categorical features have the correct type for the model
    input_df['carrier'] = input_df['carrier'].astype('category')
    input_df['airport'] = input_df['airport'].astype('category')

    # Make the prediction
    prediction = model.predict(input_df)[0]
    
    # --- 5. DISPLAY THE RESULT ---
    st.success(f"**Predicted Average Delay:**")
    st.metric(label="Minutes per Flight", value=f"{prediction:.2f}")
    
    st.info("This prediction is based on historical trends including seasonality, recent operational performance, and past flight volumes.")