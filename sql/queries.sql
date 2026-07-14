-- ============================================
-- N100 Financial Intelligence
-- Sprint 1 SQL Queries
-- ============================================

-- View Companies
SELECT *
FROM companies;

-- Count Companies
SELECT COUNT(*)
FROM companies;

-- Profit and Loss Data
SELECT *
FROM profitandloss
LIMIT 10;

-- Balance Sheet
SELECT *
FROM balancesheet
LIMIT 10;

-- Financial Ratios
SELECT *
FROM financial_ratios
LIMIT 10;

-- Market Cap
SELECT company_id,
       market_cap_crore
FROM market_cap
ORDER BY market_cap_crore DESC;

-- Top 10 Stock Prices
SELECT *
FROM stock_prices
LIMIT 10;

-- Companies with ROE > 20
SELECT company_name,
       roe_percentage
FROM companies
WHERE roe_percentage > 20;

-- Peer Groups
SELECT *
FROM peer_groups;

-- Sectors
SELECT *
FROM sectors;