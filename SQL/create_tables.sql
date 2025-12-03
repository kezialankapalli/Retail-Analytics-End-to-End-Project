-- Create DB
CREATE DATABASE IF NOT EXISTS retail_analytics
  DEFAULT CHARACTER SET utf8mb4
  DEFAULT COLLATE utf8mb4_0900_ai_ci;
USE retail_analytics;

-- Create a RAW landing table (wide, to avoid truncation)
DROP TABLE IF EXISTS raw_transactions;
CREATE TABLE raw_transactions (
  Invoice      VARCHAR(20),
  StockCode    VARCHAR(30),
  Description  TEXT,
  Quantity     INT,
  InvoiceDate  DATETIME,
  Price        DECIMAL(10,2),
  CustomerID   INT,
  Country      VARCHAR(80)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
