# 📊 N100 Financial Intelligence

A professional **ETL (Extract – Transform – Load) pipeline** for processing and validating financial datasets of **Nifty 100 companies**.

The project automates data ingestion from Excel files, performs data quality validation, normalizes financial data, and stores it in an SQLite database for analytics.

---

# 🚀 Features

- Automated Excel Loader
- Data Normalization
- Data Quality Validation (DQ Rules)
- SQLite Database Loader
- Logging Support
- End-to-End ETL Pipeline
- SQL Query Support
- Validation Report Generation
- Modular Project Structure

---

# 📂 Project Structure

```text
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
│   ├── etl/
│   │   ├── loader.py
│   │   ├── validator.py
│   │   ├── dq_rules.py
│   │   ├── normalizer.py
│   │   └── inspect_datasets.py
│   │
│   └── utils/
│       ├── logger.py
│       └── __init__.py
│
├── tests/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 📁 Datasets

The ETL pipeline processes the following datasets:

| Dataset | Description |
|----------|-------------|
| analysis | Company growth analysis |
| balancesheet | Balance Sheet |
| cashflow | Cash Flow Statement |
| companies | Company Master |
| documents | Annual Reports |
| financial_ratios | Financial Ratios |
| market_cap | Market Capitalization |
| peer_groups | Peer Group Mapping |
| profitandloss | Profit & Loss Statement |
| prosandcons | Pros & Cons |
| sectors | Sector Information |
| stock_prices | Historical Stock Prices |

---

# ⚙️ ETL Workflow

## 1. Extract

- Load Excel datasets
- Detect headers
- Clean column names

## 2. Transform

- Normalize company IDs
- Normalize dates
- Normalize years
- Normalize numeric values
- Normalize text
- Normalize boolean values

## 3. Validate

The validator executes multiple Data Quality Rules:

- DQ-01 Missing Values
- DQ-02 Duplicate Records
- DQ-03 Foreign Key Validation
- DQ-04 Numeric Validation
- DQ-05 Year Validation
- DQ-06 Business Rule Validation

Validation results are exported to:

```
output/validation_failures.csv
```

---

## 4. Load

All validated datasets are stored in:

```
database/n100.db
```

---

# 🗄 Database Tables

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

# 📋 Technologies Used

- Python 3.13
- Pandas
- SQLite
- OpenPyXL
- SQLAlchemy
- Git
- GitHub

---

# ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/dadisrinivas0513/N100-Financial-Intelligence.git
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Individual Modules

Load Data:

```bash
python src/etl/loader.py
```

Validate Data:

```bash
python src/etl/validator.py
```

Run Complete Pipeline:

```bash
python src/pipeline.py
```

---

# 📄 Output Files

Generated automatically:

- database/n100.db
- output/validation_failures.csv
- logs/pipeline.log

---

# 📈 Current Progress

| Module | Status |
|---------|--------|
| Folder Structure | ✅ |
| Excel Loader | ✅ |
| SQLite Loader | ✅ |
| Data Validation | ✅ |
| DQ Rules | ✅ |
| Logger | ✅ |
| SQL Queries | ✅ |
| Pipeline | ✅ |
| Sprint 1 | ✅ Completed |

---

# 🚀 Future Enhancements

- PostgreSQL Support
- MySQL Support
- Streamlit Dashboard
- Financial KPI Engine
- Investment Health Score
- Sector Analytics
- Peer Comparison
- Docker Deployment
- CI/CD Integration
- Cloud Deployment (AWS)

---

# 👨‍💻 Author

**Dadi Srinivas**

B.Tech – Computer Science & Engineering

Sanketika Vidya Parishad Engineering College

📍 Visakhapatnam, Andhra Pradesh

---

## 🌐 Connect With Me

**GitHub**

https://github.com/dadisrinivas0513

**LinkedIn**

https://www.linkedin.com/in/dadi-srinivas-05m032005

**Portfolio**

https://dadisrinivas.vercel.app

---

# 📜 License

This project was developed as part of a Data Engineering internship and is intended for educational and portfolio purposes.

---

⭐ If you found this project useful, consider giving it a star on GitHub!