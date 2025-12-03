USE retail_analytics;

-- Daily Sales Summary
CREATE OR REPLACE VIEW v_daily_sales AS
SELECT
  InvoiceDateDate AS dt,
  SUM(CASE WHEN IsReturn=0 THEN LineAmount ELSE 0 END) AS SalesAmount,
  SUM(CASE WHEN IsReturn=1 THEN ABS(LineAmount) ELSE 0 END) AS ReturnAmount,
  (SUM(CASE WHEN IsReturn=0 THEN LineAmount ELSE 0 END)
   - SUM(CASE WHEN IsReturn=1 THEN ABS(LineAmount) ELSE 0 END)) AS NetRevenue,
  COUNT(DISTINCT Invoice) AS NumInvoices
FROM fact_sales
GROUP BY dt;

-- Product Return Rate
CREATE OR REPLACE VIEW v_return_rate_product AS
SELECT
  StockCode,
  TRIM(Description) AS Description,
  SUM(CASE WHEN IsReturn=1 THEN ABS(Quantity) ELSE 0 END) / NULLIF(SUM(ABS(Quantity)),0) AS ReturnRate,
  SUM(ABS(Quantity)) AS TotalUnits
FROM fact_sales
GROUP BY 1,2;

-- Customer Recency, Frequency, Monetary (RFM)
CREATE OR REPLACE VIEW v_customer_rfm AS
SELECT
  CustomerID,
  DATEDIFF((SELECT MAX(InvoiceDateDate) FROM fact_sales), MAX(InvoiceDateDate)) AS RecencyDays,
  COUNT(DISTINCT Invoice) AS Frequency,
  SUM(CASE WHEN IsReturn=0 THEN LineAmount ELSE 0 END) AS Monetary
FROM fact_sales
WHERE CustomerID IS NOT NULL
GROUP BY 1;

SELECT COUNT(*) FROM v_daily_sales;
SELECT * FROM v_daily_sales LIMIT 5;

SELECT COUNT(*) FROM v_return_rate_product;
SELECT * FROM v_return_rate_product LIMIT 5;

SELECT COUNT(*) FROM v_customer_rfm;
SELECT * FROM v_customer_rfm LIMIT 5;
