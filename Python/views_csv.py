import pandas as pd
import mysql.connector as mc

# ---- CONNECT ----
conn = mc.connect(
    host="localhost",
    user="root",
    password="Uiop1234@",      # <-- your real MySQL password
    database="retail_analytics"
)

# ---- QUERIES TO EXPORT ----
exports = {
    "daily_sales.csv": "SELECT * FROM v_daily_sales",
    "return_rate_product.csv": "SELECT * FROM v_return_rate_product",
    "rfm.csv": "SELECT * FROM v_customer_rfm"
}

# ---- RUN & SAVE ----
for fname, sql in exports.items():
    df = pd.read_sql(sql, conn)
    out_path = f"/Users/kezia/Retail_Project/{fname}"
    df.to_csv(out_path, index=False)
    print("✅ Exported", out_path)
