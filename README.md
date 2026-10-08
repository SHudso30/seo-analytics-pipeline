# Automated SEO & Growth Analytics Pipeline

A cloud-native data engineering pipeline designed to ingest raw search marketing logs, process text data using Pandas, structure rows into a relational SQLite database, and execute automated validation queries via SQL.

- **Primary Source Code Script:** [pipeline.py](./pipeline.py)

---

## Step-by-Step Architecture Walkthrough

### Step 1: Library Ingestion & Environment Setup
To build the foundation of the ETL pipeline, I import three core Python modules to handle structural data wrangling, relational database storage, and random data simulation.

<img width="582" height="61" alt="step1" src="https://github.com/user-attachments/assets/35fc65a4-cd1b-4281-b850-7c791748ab46" />

- `pandas`: Utilized for high-performance data manipulation, text normalization, and structural cleaning loops.
- `sqlite3`: A serverless, zero-configuration SQL database engine used to build relational schemas completely within the container workspace.
- `random`: Used to simulate organic variance in web metrics (such as missing values or erratic text sizing) to mimic noisy real-world data feeds.

---

### Step 2: Data Ingestion & Noisy Simulation
Real-world web logs and API streams are rarely clean. Here, I define an array containing target search phrases and simulate 100 messy transactional entries to establish our raw ingestion environment.

<img width="787" height="511" alt="phase1" src="https://github.com/user-attachments/assets/4850dd29-344a-434b-8c9f-345c53ebecfa" />

- **Technical Intent:** By intentionally injecting erratic string padding (` KEYWORDS `) and `NONE` (NULL) parameter into the data generation script, I demonstrate how data pipelines handle uncurated source streams.

---

### Step 3: Pandas Transformation & Feature Engineering
Once raw data is captured into the DataFrame model, I run text normalization scripts to guarantee structural data integrity, isolate duplicates, and build computed efficiency models.

<img width="750" height="250" alt="phase2" src="https://github.com/user-attachments/assets/80294c29-4c13-412d-a37e-6a9c833c17cb" />

- **Technical Intent:** This block showcases critical exploratory data preparation metrics: text alignment via `.str.strip()`, statistical patching via median imputation, and dynamic calculation metrics via vectorized array division.

---

### Step 4: Relational SQL Schema & Database Storage
With the Pandas structure cleaned and verified, I spin up an active database loop, establish a structured table layout via structured Data Definition Language (DDL), and load my clean table into production storage.

<img width="638" height="404" alt="phase3" src="https://github.com/user-attachments/assets/0061ca99-c007-46aa-9e69-d97eb9bc3749" />

- **Technical Intent:** Relational stability is vital for enterprise applications. This segment proves proficiency in configuring active engine cursors )`sqlite3.connect`), compiling explicit table properties, and executing bulk loading tasks natively via Python.

### Step 5: Verification & Analytical Data Extraction
To verify database truth and capture high-value target keywords, I execute a structured SQL extraction query using data filtering, sorting, and row isolation arguments.

<img width="771" height="316" alt="phase4" src="https://github.com/user-attachments/assets/ba7ff0a5-bd31-4aaa-9199-faef14eac783" />

- **Technical Intent:** Writing crisp SQL strings wrapped in Pandas `.read_sql_query()` validates that I understand how to converse seamlessly between data frames and database server engines to extract business insights.


