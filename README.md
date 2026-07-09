# 📊 N100 Financial Intelligence Platform

A production-grade financial analytics platform for all **92 Nifty 100 companies**. The project provides ETL pipelines, financial data processing, KPI computation, screening, health scoring, peer comparison, reporting, and an interactive dashboard.

---

## 🚀 Project Overview

The **N100 Financial Intelligence Platform** is designed to analyze financial statements of all Nifty 100 companies and generate actionable investment insights through automated data pipelines, validation, reporting, and visualization.

---

## 🎯 Sprint Progress

| Sprint | Status |
|---------|--------|
| ✅ Day 1 – Environment Setup | Completed |
| ✅ Day 2 – Excel Loader & Data Normalisation | Completed |
| ⏳ Day 3 – Schema Validator (DQ Rules) | In Progress |
| ⏳ Day 4 – SQLite Database Schema | Pending |
| ⏳ Day 5 – Full ETL Data Load | Pending |
| ⏳ Day 6 – Data Quality Review | Pending |
| ⏳ Day 7 – Sprint Wrap-up | Pending |

---

# 📂 Project Structure

```
N100-Financial-Intelligence/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── output/
│
├── database/
│
├── docs/
│
├── notebooks/
│
├── reports/
│
├── scripts/
│
├── sql/
│
├── src/
│   └── etl/
│       ├── loader.py
│       ├── normaliser.py
│       └── validator.py (Coming Soon)
│
├── tests/
│   └── etl/
│       └── test_normaliser.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

# 📈 Datasets

The project currently loads **12 Excel datasets**.

- companies.xlsx
- profitandloss.xlsx
- balancesheet.xlsx
- cashflow.xlsx
- analysis.xlsx
- documents.xlsx
- prosandcons.xlsx
- sectors.xlsx
- stock_prices.xlsx
- financial_ratios.xlsx
- market_cap.xlsx
- peer_groups.xlsx

---

# ⚙️ Technologies Used

- Python 3.13
- Pandas
- NumPy
- SQLite (Upcoming)
- OpenPyXL
- PyTest
- Git & GitHub

---

# ✅ Completed Features

### Environment Setup

- Virtual Environment
- Requirements File
- Git Repository
- GitHub Repository
- Project Structure

---

### ETL Loader

- Automatic loading of all 12 Excel datasets
- Dynamic file discovery
- Dataset summary generation
- Error handling

---

### Data Normalisation

Implemented helper functions:

- normalize_year()
- normalize_ticker()

---

### Unit Testing

Implemented **35 Unit Tests** using PyTest.

✔ normalize_year()

✔ normalize_ticker()

```
35 Tests Passed
0 Failed
```

---

# 📊 Current Progress

| Module | Status |
|----------|--------|
| Environment Setup | ✅ |
| Folder Structure | ✅ |
| Excel Loader | ✅ |
| Data Normalisation | ✅ |
| Unit Testing | ✅ |
| SQLite Schema | ⏳ |
| Data Validation | ⏳ |
| Financial KPI Engine | ⏳ |
| Dashboard | ⏳ |

---

# 🎯 Upcoming Modules

- SQLite Database
- 16 Data Quality Rules
- Financial Ratio Engine
- Investment Screener
- Health Score (0–100)
- Sector Analytics
- Peer Comparison
- Streamlit Dashboard
- PDF Report Generator
- Excel Report Generator

---

# 📌 Current Sprint

Sprint 1 – Data Foundation

### Completed

- Environment Setup
- Excel Loader
- Data Normalisation
- Unit Testing

### In Progress

- Schema Validator (DQ-01 to DQ-16)

---

# 👨‍💻 Developer

**Dadi Srinivas**

B.Tech – Computer Science & Engineering

Sanketika Vidya Parishad Engineering College

GitHub:
https://github.com/dadisrinivas0513

LinkedIn:
https://www.linkedin.com/in/dadi-srinivas-05m032005

---

# ⭐ Repository Status

Current Version:

**Sprint 1 – Day 2 Completed**

Last Updated:
**09 July 2026**

---

## 📜 License

This project is developed for educational and portfolio purposes as part of the **N100 Financial Intelligence Capstone Project**.
