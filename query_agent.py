import sqlite3
import subprocess
import json

DB_PATH = "ecommerce.db"

def query_llama3(prompt):
    full_prompt = f"""You are a data analyst assistant. Given a user question, write an SQLite query using the schema:
    Tables: ad_sales, total_sales, eligibility

    Then answer the question clearly based on the results.
    
    Question: {prompt}
    
    Output only JSON like:
    {{
        "sql": "...",
        "answer": "..."
    }}
    """

    result = subprocess.run(
        ["ollama", "run", "llama3"],
        input=full_prompt.encode(),
        capture_output=True
    )
    output = result.stdout.decode()

    # Try to extract JSON
    try:
        json_output = json.loads(output[output.find('{'):output.rfind('}')+1])
        return json_output["sql"], json_output["answer"]
    except:
        return None, "❌ Failed to understand or parse the model's response."

def run_sql(sql):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    try:
        cursor.execute(sql)
        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        return columns, rows
    except Exception as e:
        return [], [[str(e)]]
