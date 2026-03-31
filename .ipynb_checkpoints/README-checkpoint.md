# ✈️ Flight Delay Forecasting System

## 📌 Project Overview

This repository contains an end-to-end data science project that forecasts **macro-level U.S. commercial flight delays**.

The system predicts the **average delay minutes per flight** for a specific airline at a specific airport in a given month, serving as a **strategic planning tool** for aviation stakeholders.

The final **CatBoost Regressor** model achieves a **Mean Absolute Error (MAE) of ≈ 5.8 minutes**, demonstrating strong predictive performance and real-world applicability.

---

## 💡 Key Results & Visualizations

### 📊 Model Performance Comparison

CatBoost consistently outperformed other models (XGBoost, LightGBM), achieving the lowest error.

```md
![Model Comparison](images/mae_comparison.png)
```

---

### 📈 Feature Importance

The model is primarily driven by:

* **12-month lag feature** → captures seasonality
* **3-month rolling average** → captures recent trends

```md
![Feature Importance](images/feature_importance.png)
```

---

## 🚀 Getting Started

### ✅ Option 1: Run the Interactive Web App (Recommended)

```bash
git clone https://github.com/AngelaFong264291/Flight-Delay-Forecasting-System.git
cd Flight-Delay-Forecasting-System
pip install -r requirements.txt
streamlit run app.py
```

👉 Your browser will open an interactive dashboard where you can generate predictions.

---

### 📓 Option 2: Run the Jupyter Notebook

```bash
jupyter notebook
```

Open:

```
flight_predict.ipynb
```

This contains:

* full EDA
* feature engineering
* model training process

---

## ⚙️ Methodology & Technical Details

### 1. 📊 Data Source & Target Variable

* **Source:** U.S. Bureau of Transportation Statistics (BTS)
* **Timeframe:** Aug 2013 – Aug 2023

**Target Variable:**

```text
Average Delay Minutes per Flight = total_arr_delay / total_arr_flights
```

✔ Normalizes across airport size
✔ Provides a clear delay severity metric

---

### 2. 🧠 Feature Engineering

#### Cyclical Features

* Month → transformed using sine & cosine

#### Lag Features

* 1-month lag → recent performance
* 12-month lag → seasonal patterns

#### Rolling Features

* 3-month rolling average → short-term trend
* 6-month rolling average → long-term trend

---

### 3. 🦠 Handling COVID-19 Anomaly

* Created feature: `is_covid_era`
* Covers: March 2020 – Dec 2021
* Helps model isolate abnormal behavior

---

### 4. 🤖 Model Training & Evaluation

* **Train Set:** up to Dec 2021
* **Test Set:** Jan 2022 – Aug 2023
* **Models Compared:**

  * XGBoost
  * LightGBM
  * CatBoost

✅ **Best Model:** CatBoost
📉 **MAE:** ≈ 5.8 minutes

---

## 📂 Repository Structure

```bash
Flight-Delay-Forecasting-System/
│
├── app.py
├── flight_predict.ipynb
├── airline_delay.csv
├── flight_delay_data_cleaned.csv
├── catboost_flight_delay_model.joblib
├── images/
│   ├── mae_comparison.png
│   └── feature_importance.png
└── README.md
```

---

## 💼 Business Value

This forecasting system provides actionable insights for the aviation industry:

### ✈️ Resource Optimization

* Adjust staffing levels in advance
* Improve operational efficiency

### 📊 Strategic Scheduling

* Add buffer time during high-delay periods
* Reduce cascading delays

### 🏆 Airline Benchmarking

* Compare airline performance
* Identify inefficiencies

### 😊 Passenger Experience

* Reduce delays proactively
* Improve satisfaction

---

## 🛠️ Tools & Technologies

* Python
* Jupyter Notebook
* Pandas & NumPy
* Matplotlib / Seaborn
* Scikit-learn
* CatBoost, XGBoost, LightGBM
* Streamlit

