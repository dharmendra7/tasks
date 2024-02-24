from pybit.unified_trading import HTTP
import pandas as pd
from datetime import datetime
from pytz import timezone
import pandas_ta as ta


session = HTTP(testnet=True)

start_timestamp = 1609459200000  # 1st Jan 2021, 00:00:00 in milliseconds
end_timestamp = 1640995200000    # 31st Dec 2022, 23:59:59 in milliseconds

interval = 15 

response = session.get_kline(
    category="inverse",
    symbol="BTCUSD",
    interval=interval,
    start=start_timestamp,
    end=end_timestamp,
)

data_list = response.get('result', {}).get('list', [])

columns = ["timestamp", "open", "high", "low", "close", "volume", "quoteVolume"]
df = pd.DataFrame(data_list, columns=columns)
ist_timezone = timezone('Asia/Kolkata')
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
df['timestamp'] = df['timestamp'].dt.tz_localize('UTC').dt.tz_convert(ist_timezone)
df.set_index('timestamp', inplace=True)
df['volume'] = pd.to_numeric(df['volume'], errors='coerce').fillna(0)
# df['vwap'] = ta.vwap(df.high, df.low, df.close, df.volume)
print(df)

