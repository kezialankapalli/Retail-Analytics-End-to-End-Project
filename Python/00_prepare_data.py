import os, sys
import pandas as pd

# === Update these if your path/name is different ===
XLSX = "/Users/kezia/Retail_Project/online_retail_II.xlsx"
OUT  = "/Users/kezia/Retail_Project/online_retail_clean.csv"

print("🔎 Looking for file:", XLSX)
print("   Exists? -->", os.path.exists(XLSX))

if not os.path.exists(XLSX):
    print("❌ File not found. Check spelling/capitalization and path.")
    sys.exit(1)

try:
    # List sheet names so we can see exact spelling
    xls = pd.ExcelFile(XLSX)
    print("📄 Sheets found:", xls.sheet_names)

    # Try flexible matching in case sheet names differ slightly
    # (e.g., 'Year 2009-2010' / 'Year 2010-2011')
    def pick(name_hint):
        for s in xls.sheet_names:
            if name_hint.lower() in s.lower():
                return s
        return None

    s1 = pick("2009-2010") or pick("2009") or xls.sheet_names[0]
    s2 = pick("2010-2011") or pick("2010") or xls.sheet_names[-1]
    print(f"✅ Using sheets: {s1!r} and {s2!r}")

    df1 = pd.read_excel(XLSX, sheet_name=s1)
    df2 = pd.read_excel(XLSX, sheet_name=s2)
    print(f"   Rows: {s1}={len(df1)}, {s2}={len(df2)}")

    # Basic cleaning
    required = ['Invoice', 'InvoiceDate', 'Price', 'Quantity']
    missing = [c for c in required if c not in df1.columns or c not in df2.columns]
    if missing:
        print("❌ Missing expected columns:", missing)
        print("   Columns in file:", df1.columns.tolist())
        sys.exit(1)

    df = pd.concat([df1, df2], ignore_index=True)
    before = len(df)

    df = df.dropna(subset=['Invoice', 'InvoiceDate'])
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], errors='coerce')
    df = df.dropna(subset=['InvoiceDate'])
    df = df[df['Price'] > 0]
    df = df[df['Quantity'] != 0]
    after = len(df)

    print(f"🧹 Cleaned rows: kept {after} of {before} ({after/before:.1%})")

    df.to_csv(OUT, index=False)
    print("✅ Wrote CSV:", OUT)

except Exception as e:
    import traceback
    print("❌ Error while processing:")
    traceback.print_exc()
    sys.exit(1)
