import threading
import time
from pybit.unified_trading import HTTP

def symbol_data(symbol, start_timestamp, end_timestamp):
    session = HTTP(testnet=True)
    result = session.get_kline(
        category="inverse",
        symbol=symbol,
        interval=15,  
        start=start_timestamp,
        end=end_timestamp,
    )
    print(f"Data for {symbol}: {result}")

def get_data_for_symbols(symbols, start_timestamp, end_timestamp):
    threads = []

    for symbol in symbols:
        thread = threading.Thread(
            target=symbol_data,
            args=(symbol, start_timestamp, end_timestamp),
        )
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

#date range (1st Jan 2021 to 31st Dec 2022)
start_date = "2021-01-01"
end_date = "2022-12-31"
start_timestamp = int(time.mktime(time.strptime(start_date, "%Y-%m-%d"))) * 1000
end_timestamp = (int(time.mktime(time.strptime(end_date, "%Y-%m-%d"))) + 24 * 60 * 60) * 1000

symbols = ["BTCUSD", "ETHUSD", "BITUSD", "SOLUSD", "XRPUSD"]
get_data_for_symbols(symbols, start_timestamp, end_timestamp)
