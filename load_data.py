import pandas as pd
import sqlite3

# Load CSVs
ad_sales = pd.read_csv("data/ad_sales.csv")
eligibility = pd.read_csv("data/eligibility.csv")
total_sales = pd.read_csv("data/total_sales.csv")

# Connect to SQLite DB
conn = sqlite3.connect("ecommerce.db")

# Save tables
ad_sales.to_sql("ad_sales", conn, if_exists="replace", index=False)
eligibility.to_sql("eligibility", conn, if_exists="replace", index=False)
total_sales.to_sql("total_sales", conn, if_exists="replace", index=False)

print("✅ Database loaded successfully.")
conn.close()
