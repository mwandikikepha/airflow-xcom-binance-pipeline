import pandas as pd
from .extract import extract_binance_data

def transform_binance_data(df):
    
    df = df[['symbol', 'priceChangePercent', 'lastPrice', 'volume']]
    numeric_cols = ['priceChangePercent', 'lastPrice', 'volume']
    df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric)
    
    print(f'TRabsformed {len(df)} rows.')
    return df
