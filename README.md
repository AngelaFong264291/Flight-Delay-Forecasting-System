# ✈️ Flight Delay Forecasting System

## 📌 Project Overview

This project develops a **macro-level predictive forecasting system** for U.S. commercial flight delays. Instead of predicting whether an individual flight will be delayed, the system forecasts the **average delay minutes per flight** for a specific airline at a specific airport in a given month.

The goal is to support **strategic decision-making** in the aviation industry by anticipating delay severity in advance.

---

## 🌍 Background & Context

Flight delays are a major operational challenge in the aviation industry, costing airlines billions of dollars annually and negatively impacting customer satisfaction.

While delays can be triggered by unpredictable events such as weather or mechanical issues, **macro-level trends**—including seasonal weather patterns, airport congestion, and airline-specific inefficiencies—can be modeled using historical data.

This project leverages these patterns to provide **forward-looking delay forecasts**.

---

## 🎯 Project Objective

The objective of this project is to build a **machine learning forecasting model** that predicts:

> **Average delay minutes per flight**
> for a given airline, airport, and month.

This shifts the focus from:

* ❌ "Will a specific flight be delayed?"

To:

* ✅ "How severe will delays be at a system level?"

---

## 📊 Dataset

### Source

U.S. Bureau of Transportation Statistics (BTS)

### Data Scope

* **Timeframe:** August 2013 – August 2023
* **Granularity:** Year, Month, Carrier, Airport
* **Type:** Monthly aggregated airline performance data

### Features Included

* Number of arriving flights (`arr_flights`)
* Total arrival delay minutes (`arr_delay`)
* Delays over 15 minutes
* Cancellation counts
* Diversion counts
* Delay causes:

  * Carrier delays
  * Weather delays
  * NAS (National Airspace System)
  * Security delays
  * Late aircraft delays

---

## 🎯 Target Variable

The model predicts:

```text
Average Delay Minutes per Flight = arr_delay / arr_flights
```

### Why this metric?

* Normalizes delay across airports of different sizes
* Avoids bias toward large hub airports
* Provides a **clear, interpretable measure of delay severity**

### Interpretation

> "On average, how many minutes of delay should be expected per flight?"

---

## 🧠 Methodology

### Workflow

1. Data Cleaning & Preprocessing
2. Exploratory Data Analysis (EDA)
3. Feature Engineering
4. Target Variable Creation
5. Model Training
6. Model Evaluation
7. Forecasting & Interpretation

---

## 🤖 Model Selection

Multiple models were evaluated, including:

* XGBoost
* LightGBM
* CatBoost

### ✅ Final Model:

**CatBoost Regressor**

Chosen for its:

* Strong performance on tabular data
* Ability to handle categorical variables
* Robust generalization

---

## 📈 Model Performance

* **Metric:** Mean Absolute Error (MAE)
* **Test Period:** 2022–2023
* **Final MAE:** **≈ 5.8 minutes**

### Interpretation

On average, the model’s prediction error is **less than 6 minutes per flight**.

---

## 🔍 Real-World Case Study

**Airline:** Delta Airlines (DL)
**Airport:** Atlanta (ATL)
**Month:** July 2022

* Predicted Delay: **12.27 minutes**
* Actual Delay: **14.13 minutes**
* Error: **1.86 minutes**

### 💡 Insight

The model provides **highly accurate early warnings**, enabling airlines to prepare for operational stress in advance.

---

## 💼 Business Value

### 1. Resource Optimization

* Adjust staffing levels in advance
* Improve airport operations planning

### 2. Airline Benchmarking

* Compare performance across airlines
* Identify operational inefficiencies

### 3. Strategic Scheduling

* Add buffer time for high-delay periods
* Reduce disruptions

### 4. Root-Cause Insights

Understand whether delays are driven by:

* Weather
* Airline operations
* Airspace congestion
* Late aircraft

---

## 🔑 Key Insights

* Delay patterns are **predictable at a macro level**
* Seasonal trends significantly impact delays
* Airline-airport combinations behave differently
* Machine learning enables **actionable forecasting**

---

## 🛠️ Tools & Technologies

* Python
* Jupyter Notebook
* Pandas
* NumPy
* Matplotlib / Seaborn
* Scikit-learn
* CatBoost
* XGBoost / LightGBM

---

## 📁 Project Structure

```bash
Flight-Delay-Forecasting-System/
│
├── README.md
├── flight_delay_forecasting.ipynb
├── data/
│   └── flight_delay_data.csv
├── outputs/
│   ├── figures/
│   └── models/
└── requirements.txt
```

---

## 🚀 How to Run

1. Clone the repository:

```bash
git clone https://github.com/AngelaFong264291/Flight-Delay-Forecasting-System.git
```

2. Navigate to the folder:

```bash
cd Flight-Delay-Forecasting-System
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Open Jupyter Notebook:

```bash
jupyter notebook
```

---

## 📌 Conclusion

This project demonstrates that **historical aviation data can be transformed into accurate, actionable forecasts**.

With an MAE of approximately **5.8 minutes**, the model provides meaningful insights into future delay conditions.

More importantly, it serves as a **strategic tool** that helps aviation stakeholders:

* anticipate operational challenges
* optimize resources
* improve efficiency
* enhance passenger experience

---

## 👤 Author

**Angela Fong**

---

## 📄 License

This project is for educational and analytical purposes.
