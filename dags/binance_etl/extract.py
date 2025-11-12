import pandas as pd
import requests

def extract_binance_data():
    api_url = "https://api.binance.com/api/v3/ticker/24hr"              
    response = requests.get(api_url)
    data = response.json()
    df = pd.DataFrame(data)
    return df

    