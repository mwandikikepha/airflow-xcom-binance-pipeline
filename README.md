# Binance ETL Pipeline with Apache Airflow (XComs)

A fully automated **ETL data pipeline** built with **Apache Airflow** that extracts real-time Binance ticker data, transforms it for analytics, and loads it into a PostgreSQL database.  
The pipeline uses **XComs** to share data between tasks.

---

##  Project Overview

This ETL pipeline performs three key stages:

1. **Extract** – Fetches live ticker data from the Binance API  
2. **Transform** – Cleans and converts the raw data (e.g., timestamps, numeric types)  
3. **Load** – Inserts the cleaned data into a PostgreSQL database table (`binance_ticker`)

The process is fully orchestrated using **Apache Airflow**, allowing for scheduling, monitoring, and task dependency management.

---

## ⚙️ Tech Stack

- **Apache Airflow** – Workflow orchestration  
- **Python (3.12)** – Core ETL logic  
- **PostgreSQL** – Target database  
- **Pandas** – Data transformation  
- **Requests** – API data extraction  

---

##  Workflow Diagram

```

Extract (Binance API)
↓
Transform (Pandas)
↓
Load (PostgreSQL Table)

```


Each stage communicates via **Airflow XComs**, ensuring smooth in-memory data passing between tasks without writing to disk.

---

##  Setup Instructions

### 1️ Clone the repository

```
git clone https://github.com/mwandikikepha/airflow-xcom-binance-pipeline.git

cd airflow-xcom-binance-pipeline

```

2️ **Create and activate a virtual environment**

```
python3 -m venv mainenv

source mainenv/bin/activate
```


3️ **Install dependencies**

```pip install -r requirements.txt```

4️ **Initialize Airflow**
```

airflow db init
airflow users create \
  --username admin \
  --firstname Kepha \
  --lastname Mwandiki \
  --role Admin \
  --email you@example.com \
  --password admin
```


5️⃣ **Start Airflow**
```

airflow webserver 
airflow scheduler
```

**Project Structure**

```

airflow-xcom-binance-pipeline/
│
├── dags/
│   ├── binance_etl_dag.py            # Defines the Airflow DAG & tasks
│   └── binance_etl/
│       ├── __init__.py
│       ├── extract.py                # Fetch data from Binance API
│       ├── transform.py              # Clean and format data
│       └── load.py                   # Load data into PostgreSQL
│
├── .gitignore
├── requirements.txt
└── README.md

```

**Dependencies (requirements.txt)**
```

apache-airflow
pandas
requests
sqlalchemy
psycopg2-binary
```

## Author

**Kepha Mwandiki**  

- Full-stack Data Engineer & Python Developer  
- Experienced in building ETL pipelines, workflow orchestration with Airflow, and data visualization  
- Expertise in data architecture, analytics, and working with diverse datasets across multiple domains  
- Passionate about creating scalable, production-ready data solutions  
- GitHub: [mwandikikepha](https://github.com/mwandikikepha)  
- Email: `mwandikikepha7@gmail.com`  













































