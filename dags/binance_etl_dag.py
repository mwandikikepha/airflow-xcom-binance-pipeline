from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
import sys
import os

sys.path.append(os.path.dirname(__file__))

from binance_etl.extract import extract_binance_data
from binance_etl.transform import transform_binance_data
from binance_etl.load import load_data

import pandas as pd

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'retries': 1,
}

with DAG(
    dag_id='binance_etl_dag',
    default_args=default_args,
    schedule= '@daily',
    start_date=datetime(2025, 10, 10),
    catchup=False,
) as dag:
    
    def extract_task(**context):
        df = extract_binance_data()
        
        if not df.empty:
            context['ti'].xcom_push(key='raw_data', value=df.to_json())
        else:
            raise ValueError("Extracted data is empty.")
        
    def transform_task(**context):
        raw_json = context['ti'].xcom_pull(key='raw_data', task_ids='extract_task')
        df_raw = pd.read_json(raw_json)
        df_clean = transform_binance_data(df_raw)
        context['ti'].xcom_push(key='clean_data', value=df_clean.to_json())
        
    def load_task(**context):
        clean_json = context['ti'].xcom_pull(key='clean_data', task_ids='transform_task')
        df_clean = pd.read_json(clean_json)
        load_data(df_clean)
        
    extract = PythonOperator(
        task_id='extract_task',
        python_callable=extract_task,
        
    )
    
    transform = PythonOperator(
        task_id='transform_task',
        python_callable=transform_task,
        
    )
     
    load = PythonOperator(
        task_id='load_task',
        python_callable=load_task,
        
    )
      
    extract >> transform >> load
      
        
      
