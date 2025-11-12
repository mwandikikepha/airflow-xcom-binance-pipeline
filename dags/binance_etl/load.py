import pandas as pd
from sqlalchemy import create_engine
from .extract import extract_binance_data
from .transform import transform_binance_data

def load_data(df):
    if df.empty:
        print('NO data')
        return
    
    try:
        engine = create_engine("postgresql://airflow_user:airflow_pass@localhost:5432/airflow_db")
        df.to_sql('binance_ticker', engine, if_exists='append', index=False)
        
        print('data loaded successfully(table: binance_ticker)')
    except Exception as e:
        print (f'postgres data failed: {e}')
        
        df.to_csv('backup_csv', index=False)
        

