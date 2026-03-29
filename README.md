# Flight-Delay-Forecasting-System

## Project Overview
This project develops a **macro-level predictive forecasting system** for U.S. commercial flight delays. Instead of predicting whether an individual flight will be delayed, the system forecasts the **average delay minutes per flight** for a specific airline at a specific airport in a given month.

The goal is to help aviation stakeholders anticipate operational challenges in advance and make better strategic decisions around staffing, scheduling, and performance management.

---

## Background & Context
Flight delays create major operational and financial challenges in the aviation industry. They increase costs for airlines, reduce efficiency at airports, and negatively affect passenger satisfaction.

Although some delays are caused by unpredictable events such as sudden weather changes or mechanical issues, larger patterns can still be observed over time. Seasonal weather, congestion at major hubs, and airline-specific operational inefficiencies often repeat and can be modeled using historical data.

This project uses those historical patterns to build a forecasting system that supports long-term planning.

---

## Project Objective
The objective of this project is to build a **machine learning forecasting system** that predicts future flight delay severity at the monthly level.

Rather than answering:

- “Will this specific flight be late?”

the project answers:

- “How severe are delays likely to be for this airline at this airport next month or season?”

This makes the system more useful for **strategic planning** rather than real-time flight tracking.

---

## Dataset
The dataset comes from the **U.S. Bureau of Transportation Statistics (BTS)** and contains monthly aggregated airline performance data.

### Data Scope
- **Timeframe:** August 2013 – August 2023
- **Granularity:** Year, Month, Carrier, Airport
- **Coverage:** U.S. commercial flight arrivals and delays
- **Data Type:** Monthly aggregated operational records

### Features Available
The dataset includes variables such as:
- Number of arriving flights
- Total arrival delay minutes
- Delays over 15 minutes
- Cancellation counts
- Diversion counts
- Delay minutes attributed to:
  - Carrier
  - Weather
  - National Airspace System (NAS)
  - Security
  - Late aircraft arrivals

---

## Target Variable
To make the prediction standardized and comparable across both small and large airports, the target variable is defined as:

```text
Average Delay Minutes per Flight = arr_delay / arr_flights
