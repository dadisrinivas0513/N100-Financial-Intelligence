# Sprint 1 Report

## Project
N100 Financial Intelligence

---

## Objective

Build a robust ETL pipeline capable of:

- Loading Excel datasets
- Validating data quality
- Normalizing values
- Storing datasets into SQLite
- Logging execution
- Creating validation reports

---

## Work Completed

### Project Structure

Created modular project folders:

- data/
- database/
- docs/
- logs/
- notebooks/
- output/
- reports/
- sql/
- src/
- tests/

---

### ETL Loader

Implemented loader.py

Features:

- Reads all Excel files
- Cleans headers
- Loads into SQLite
- Creates n100.db

---

### Data Validation

Implemented validator.py

Checks:

- Missing IDs
- Duplicate IDs
- Invalid Company IDs
- Negative Financial Values
- Invalid Years
- Missing Company References

Generated:

output/validation_failures.csv

---

### Normalization

Implemented:

- Company ID normalization
- Year normalization
- Numeric normalization
- Date normalization
- Text normalization
- Boolean normalization

---

### Database

SQLite Database:

database/n100.db

Tables Created:

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

### Logging

Created

logs/pipeline.log

Captures:

- Loader execution
- Validator execution
- Pipeline completion

---

### SQL

Created SQL queries for

- Companies
- Profit & Loss
- Balance Sheet
- Financial Ratios
- Market Cap
- Stock Prices
- Sectors

---

### Testing

Implemented unit testing for

normalizer.py

---

## Technologies Used

Python

Pandas

SQLite

OpenPyXL

Pytest

Logging

Git

GitHub

VS Code

---

## Sprint Status

Sprint 1 Completed Successfully

---

Prepared By

Dadi Srinivas

B.Tech CSE

Sanketika Vidya Parishad Engineering College