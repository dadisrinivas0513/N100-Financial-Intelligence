# 📈 N100 Financial Intelligence

A professional Data Engineering project that builds a complete ETL (Extract–Transform–Load) pipeline for analyzing financial data of Nifty 100 companies. The project ingests multiple Excel datasets, validates data quality, stores cleaned data into SQLite, and prepares the foundation for financial analytics dashboards.

---

# 🚀 Project Overview

The N100 Financial Intelligence Platform is designed to automate financial data processing using Python and SQLite.

The pipeline performs:

- Data Extraction
- Data Cleaning
- Data Validation
- Data Normalization
- Database Loading
- Reporting
- Logging

The project is developed following modular Data Engineering practices.

---

# 🎯 Sprint 1 Objectives

- ✔ Load multiple Excel datasets
- ✔ Standardize column names
- ✔ Normalize financial data
- ✔ Perform Data Quality validation
- ✔ Store datasets into SQLite
- ✔ Generate validation reports
- ✔ Build reusable ETL pipeline
- ✔ Implement logging

---

# 📂 Project Structure

```
N100-Financial-Intelligence/

│
├── data/
│   ├── raw/
│   └── processed/
│
├── database/
│   └── n100.db
│
├── docs/
│   └── Sprint_Report.md
│
├── logs/
│   └── pipeline.log
│
├── output/
│   └── validation_failures.csv
│
├── sql/
│   └── queries.sql
│
├── src/
│   ├── pipeline.py
│   │
│   ├── utils/
│   │     logger.py
│   │
│   └── etl/
│         loader.py
│         validator.py
│         dq_rules.py
│         normalizer.py
│         inspect_datasets.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 📊 Datasets

The ETL pipeline processes:

- companies
- balancesheet
- cashflow
- profitandloss
- stock_prices
- market_cap
- financial_ratios
- sectors
- documents
- peer_groups
- analysis
- prosandcons

---

# ⚙ ETL Pipeline

## Step 1 — Extract

- Read Excel datasets
- Detect headers
- Standardize columns

## Step 2 — Transform

- Normalize Company IDs
- Normalize Years
- Normalize Numbers
- Normalize Text
- Normalize Boolean values

## Step 3 — Validate

Current Validation Rules

- Missing Values
- Duplicate Records
- Invalid Years
- Business Rule Validation
- Numeric Validation
- Foreign Key Validation

Validation Report

```
output/validation_failures.csv
```

## Step 4 — Load

All cleaned datasets are loaded into

```
database/n100.db
```

---

# 🗄 SQLite Database

Created Tables

- analysis
- balancesheet
- cashflow
- companies
- documents
- financial_ratios
- market_cap
- peer_groups
- profitandloss
- prosandcons
- sectors
- stock_prices

---

# 📈 Logging

Pipeline logs are generated automatically.

```
logs/pipeline.log
```

---

# 🛠 Technologies Used

- Python 3.13
- Pandas
- SQLite
- SQLAlchemy
- OpenPyXL
- Git
- GitHub

---

# ▶ Running the Project

Create Environment

```bash
python -m venv venv
```

Activate

```bash
venv\Scripts\activate
```

Install Packages

```bash
pip install -r requirements.txt
```

Run Loader

```bash
python src/etl/loader.py
```

Run Validator

```bash
python src/etl/validator.py
```

Run Pipeline

```bash
python src/pipeline.py
```

---

# 📄 Outputs

Generated automatically

- SQLite Database
- Validation Report
- Pipeline Logs

---

# 📌 Sprint 1 Status

| Module | Status |
|----------|--------|
| ETL Loader | ✅ |
| SQLite Loader | ✅ |
| Data Validation | ✅ |
| Normalization | ✅ |
| Logger | ✅ |
| SQL Queries | ✅ |
| Documentation | ✅ |

---

# 🚀 Sprint 2

Upcoming Features

- KPI Engine
- Company Ranking
- Financial Health Score
- Sector Analysis
- Streamlit Dashboard
- Investment Screener
- API Development

---

# 👨‍💻 Author

**Dadi Srinivas**

B.Tech Computer Science & Engineering

Sanketika Vidya Parishad Engineering College

Visakhapatnam, Andhra Pradesh

GitHub

https://github.com/dadisrinivas0513

LinkedIn

https://www.linkedin.com/in/dadi-srinivas-05m032005

Portfolio

https://dadisrinivas.vercel.app

---

⭐ Developed as part of a Financial Data Engineering Internship Project.