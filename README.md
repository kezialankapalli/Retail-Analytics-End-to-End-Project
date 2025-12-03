📊 Retail Analytics – End-to-End SQL, Python & Tableau Project
This repository contains a complete Retail Analytics portfolio project built using:
* SQL (data cleaning, modeling, aggregated views)
* Python (preprocessing & exporting analytical datasets)
* Tableau Public (3 fully interactive dashboards)
The project replicates real-world retail analytics work, including KPI monitoring, product return quality analysis, and RFM customer segmentation.

🗂️ Repository Structure

Retail_Project/

├── data_raw/                 # Original raw data
├── data_processed/           # Cleaned datasets used in SQL/Tableau
├── Python/                   # Python scripts for data preparation
├── SQL/                      # SQL schema + data modeling
├── Tableau/                  # Final Tableau dashboards
├── images/                   # Dashboard screenshots (for GitHub preview)
├── .gitignore
└── README.md

📁 Datasets
Raw Data (Not Modified)
* online_retail_II.xlsx — original dataset
* zipped archive backup
Processed Data (Used in Tableau)
* daily_sales.csv
* online_retail_clean.csv
* return_rate_product.csv
* rfm.csv

🛠️ Python Scripts
00_prepare_data.py
* Cleans online retail dataset
* Removes invalid records
* Fixes descriptions
* Removes whitespace and special characters
* Outputs cleaned CSV for SQL/Tableau
views_csv.py
* Generates analytical datasets (daily sales, product returns, RFM tables)
* Exports CSVs into the data_processed/ folder

🧮 SQL Files
create_tables.sql
* Creates base schema
* Creates fact & dimension tables
* Loads cleaned CSV data
create_views.sql
Creates reusable analytical views:
* Daily sales view
* Return rate per product
* RFM view
These views power Tableau dashboards.

📊 Tableau Dashboards (3)
Stored in /Tableau/:
1️⃣ Retail Analytics – KPIs, Revenue & Invoice Volumes
* Total Sales
* Total Returns
* Monthly trends
* Invoice volume analysis
2️⃣ Retail Analytics – Product Return Analysis & Quality Insights
* Return rate by product
* Return segmentation
* Identifying defective or high-return products
3️⃣ Retail Analytics – Customer Segmentation & RFM Insights
* RFM Scatter Plot (Frequency vs Monetary)
* RFM Heatmap
* Filters: Recency Score, Frequency Score
* Interpretation text
Screenshots included in /images/.

🎯 Project Goals
This project demonstrates real analytics workflows:
* Cleaning and preparing complex retail data
* Building analytical datasets using SQL & Python
* Creating business dashboards with Tableau
* Understanding retail KPIs, customer behavior & return patterns
* Creating a unified portfolio project with multiple dashboards

🚀 How to Run the Project
1️⃣ Clone the repository
git clone <your GitHub repo link>
cd Retail_Project
2️⃣ Load raw data into MySQL (optional)
Run:
create_tables.sql
create_views.sql
3️⃣ Run Python preprocessing (if needed)
python Python/00_prepare_data.py
python Python/views_csv.py
4️⃣ Open Tableau files
Open .twbx files from the Tableau/ folder in Tableau Public Desktop.

📬 Contact / Portfolio
* Tableau Public:https://public.tableau.com/app/profile/kezialankapalli/vizzes




