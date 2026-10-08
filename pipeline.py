import pandas as pd 
import sqlite3
import random

# ==================================================================
# PHASE 1: DATA INGESTION (Simulating Raw Scraped Web/API Data)
# ==================================================================
print("Phase 1: Initiating data ingestion process...")

raw_keywords = [
    "data analyst remote", "python for beginners", "learn sql online",
    "marketing analytics tools", "seo strategy 2026", "power bi dashboard examples",
    "pandas data cleaning", "github student pack", "boot dev review", "how to learn data science"
]

raw_data = []
for i in range(100):
    keyword = random.choice(raw_keywords)
    if i % 10 == 0:
        keyword = f" {keyword.upper()} " # Messy spacing and casing

    search_volume = random.choice([1200, 5400, 390, 12000, None, 0])
    competition_score = round(random.uniform(0.1, 0.95), 2)
    clicks = random.randint(10, 450)

    raw_data.append({
        "Keyword": keyword,
        "Avg_Monthly_Searches": search_volume,
        "Competition": competition_score,
        "Est_Clicks": clicks
    })

df_raw = pd.DataFrame(raw_data)
print(f"Raw ingestion complete. Shape: {df_raw.shape}")


# =======================================================
# PHASE 2: DATA TRANSFORMATION & CLEANING (Pandas)
# =======================================================
print("\nPhase 2: Running Pandas text normalization and data cleaning pipelines...")

df_cleaned = df_raw.copy()
df_cleaned ["Keyword"] = df_cleaned["Keyword"].astype(str).str.strip().str.lower()
df_cleaned = df_cleaned.drop_duplicates()

median_searches = df_cleaned["Avg_Monthly_Searches"].median()
df_cleaned["Avg_Monthly_Searches"] = df_cleaned["Avg_Monthly_Searches"].fillna(median_searches)

df_cleaned["Click_Through_Efficiency"] = round(
    (df_cleaned["Est_Clicks"] / (df_cleaned["Avg_Monthly_Searches"] + 1)) * 100, 2)

print(f"Transformation complete. Cleaned Shape: {df_cleaned.shape}")


# ==================================================================
# PHASE 3: RELATIONAL STORAGE (SQL Execution via SQLite)
# ==================================================================
print("\nPhase 3: Constructing SQL schema and populating database...")

conn = sqlite3.connect("seo_metrics.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS keyword_analytics (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    keyword TEXT NOT NULL,
    avg_monthly_searches REAL,
    competition REAL,
    est_clicks INTEGER,
    click_through_efficiency REAL
)
""")

cursor.execute("DELETE FROM keyword_analytics")
conn.commit()

df_cleaned.to_sql("keyword_analytics", conn, if_exists="append", index=False)
print("Raw Data successfully structured and mapped to keyword_analytics table.")


# ====================================================================
# PHASE 4: VERIFICATION & DATA ANALYTICS QUERY OVER THE ENGINE
# ====================================================================
print("\nPhase 4: Executing analytical validation SQL query across dataset...")

query = """
SELECT keyword, avg_monthly_searches, competition, click_through_efficiency
FROM keyword_analytics
WHERE competition < 0.60
ORDER BY click_through_efficiency DESC
LIMIT 5
"""

results_df = pd.read_sql_query(query, conn)
print("\nTOP 5 HIGH-EFFICIENCY, LOW-COMPETITION GROWTH SECTOR KEYWORDS FOUND:")
print(results_df.to_string(index=False))

conn.close()
print("\nPipeline process terminated cleanly. Data assets stored locally inside cloud container.")
