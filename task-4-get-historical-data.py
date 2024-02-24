# {   
#     c:[190.89999389648438, 197.7899932861328, 193.80999755859375], 
#     h:[193.75, 200.47999572753906, 198.60000610351562, 194.1999969482422],
#     l:[186.00999450683594, 192.8800048828125, 192.3000030517578],
#     o:[186.74000549316406, 194.7899932861328, 198.5399932861328],
#     s:"ok",
#     t:[1677715200, 1677801600, 1678060800],
#     v:[181979152, 154193280, 128100104],
#     vo:[0, 0, 0]
# }

import requests
import pandas as pd

def get_historical_candle_data(symbol, resolution, from_timestamp, to_timestamp):
    url = "https://tvc4.investing.com/77bef8329b3909a0f927950e8277da53/1708769421/1/1/8/history"
    payload = {
        "symbol": symbol,
        "resolution": resolution,
        "from": from_timestamp,
        "to": to_timestamp
    }

    response = requests.get(url, payload)
    print(response)
    if response.status_code == 200:
        return response.json()


symbol = 13994 
resolution = 60  
from_timestamp = 1703585774
to_timestamp = 1708769834  

api_response = get_historical_candle_data(symbol, resolution, from_timestamp, to_timestamp)

if api_response:
    df = pd.DataFrame(api_response)
    # Convert timestamps to datetime
    df['t'] = pd.to_datetime(df['t'], unit='s')



