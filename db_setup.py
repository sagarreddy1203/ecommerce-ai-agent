import pandas as pd
import sqlite3
import os

def create_database():
    db_path = "ecommerce.db"
    if os.path.exists(db_path):
        os.remove(db_path)

    conn = sqlite3.connect(db_path)

    # Load CSVs
    ad_sales = pd.read_csv("csv/ad_sales.csv")
    total_sales = pd.read_csv("csv/total_sales.csv")
    eligibility = pd.read_csv("csv/eligibility.csv")

    # Save to SQLite
    ad_sales.to_sql("ad_sales", conn, index=False)
    total_sales.to_sql("total_sales", conn, index=False)
    eligibility.to_sql("eligibility", conn, index=False)

    conn.commit()
    conn.close()
    print("✅ Database created: ecommerce.db")

if __name__ == "__main__":
    create_database()
