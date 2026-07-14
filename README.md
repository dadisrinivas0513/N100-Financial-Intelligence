# 📈 N100 Financial Intelligence

A complete ETL (Extract–Transform–Load) pipeline for processing and validating financial datasets of Nifty 100 companies. This project automates data ingestion from multiple Excel files, performs data quality validation, and stores the cleaned datasets into an SQLite database for analytics and reporting.

---

# 📌 Project Overview

The N100 Financial Intelligence project is designed to build a robust data engineering pipeline capable of:

- Loading multiple Excel datasets
- Cleaning and standardizing column names
- Performing data quality validation
- Detecting inconsistencies
- Generating validation reports
- Loading processed datasets into SQLite
- Preparing data for analytics dashboards

---

# 🎯 Objectives

- Build a reusable ETL pipeline.
- Validate financial datasets using predefined Data Quality (DQ) rules.
- Store all cleaned datasets inside SQLite.
- Generate validation reports.
- Create a scalable project structure for future analytics.

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
│
├── logs/
│   └── pipeline.log
│
├── notebooks/
│
├── output/
│   └── validation_failures.csv
│
├── reports/
│
├── sql/
│
├── src/
│   ├── pipeline.py
│   ├── logger.py
│   │
│   └── etl/
│       ├── loader.py
│       ├── validator.py
│       ├── dq_rules.py
│       ├── inspect_datasets.py
│       └── normalizer.py
│
├── tests/
│
├── requirements.txt
├── README.md
└── inspection_report.txt
```

---

# 📊 Datasets

The project processes the following datasets:

| Dataset | Description |
|----------|-------------|
| companies | Company master data |
| profitandloss | Profit & Loss statements |
| balancesheet | Balance Sheet |
| cashflow | Cash Flow Statement |
| financial_ratios | Financial Ratios |
| market_cap | Market Capitalization |
| stock_prices | Historical Stock Prices |
| sectors | Sector Information |
| peer_groups | Peer Comparison |
| documents | Annual Reports |
| analysis | Growth Analysis |
| prosandcons | Company Pros & Cons |

---

# ⚙ ETL Workflow

## Step 1 – Extract

- Read all Excel datasets.
- Detect extra title/header rows.
- Standardize column names.

---

## Step 2 – Transform

- Clean column names.
- Normalize text.
- Normalize company IDs.
- Normalize years.
- Normalize numeric values.
- Normalize boolean values.

---

## Step 3 – Validate

Data Quality rules are executed before loading.

Current rules include:

- Missing values
- Duplicate records
- Foreign key consistency
- Invalid numeric values
- Year validation
- Business rule validation

Validation failures are exported to:

```
output/validation_failures.csv
```

---

## Step 4 – Load

Cleaned datasets are loaded into

```
database/n100.db
```

using SQLite.

---

# 🗄 SQLite Database

The following tables are created:

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

# 🛠 Technologies Used

- Python 3.13
- Pandas
- SQLite
- OpenPyXL
- SQLAlchemy
- Git
- GitHub

---

# 📈 Data Quality Validation

Validation Rules Implemented:

- DQ-01 Missing Values
- DQ-02 Duplicate Records
- DQ-03 Foreign Key Validation
- DQ-04 Numeric Validation
- DQ-05 Year Validation
- DQ-06 Business Rule Validation

Validation report generated automatically.

---

# ▶ How to Run

## Clone Repository

```bash
git clone <repository-url>
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

---

## Activate Environment

Windows

```bash
venv\Scripts\activate
```

---

## Install Requirements

```bash
pip install -r requirements.txt
```

---

## Run Loader

```bash
python src/etl/loader.py
```

---

## Run Validator

```bash
python src/etl/validator.py
```

---

## Run Complete Pipeline

```bash
python src/pipeline.py
```

---

# 📁 Output Files

Generated during execution:

```
database/n100.db

output/validation_failures.csv

logs/pipeline.log
```

---

# 📌 Features

- Automated Excel Loader
- Automatic Header Detection
- Column Standardization
- SQLite Integration
- Validation Report Generation
- Modular ETL Design
- Reusable Utility Functions

---

# 🚀 Future Enhancements

- PostgreSQL Support
- MySQL Support
- Streamlit Dashboard
- REST API
- Airflow Scheduling
- Docker Deployment
- CI/CD Pipeline
- Cloud Deployment (AWS)

---

# 👨‍💻 Author

**Dadi Srinivas**

B.Tech Computer Science & Engineering

Sanketika Vidya Parishad Engineering College

Visakhapatnam, Andhra Pradesh

GitHub:
https://github.com/dadisrinivas0513

LinkedIn:
https://www.linkedin.com/in/dadi-srinivas-05m032005

Portfolio:
https://dadisrinivas.vercel.app

---

# 📄 License

This project was developed as part of a Data Engineering Internship for educational and learning purposes.

---

⭐ If you found this project useful, consider giving it a star on GitHub.