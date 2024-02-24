import requests
import json
import pandas as pd
from pprint import pprint

symbol = "NIFTY"
url = f'https://www.nseindia.com/api/option-chain-indices?symbol={symbol}'

headers={'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}
response = requests.get(url, headers=headers, timeout=10)

response_text=response.text
json_object = json.loads(response_text)

#print(json_object)

# with open("OC.json", "w") as outfile:
#     outfile.write(response_text)

data = json_object['records']['data']
print(type(data))

e_date=json_object['records']['expiryDates']

oc_data = []
for ed in e_date:
    for di in range(len(data)):
        if data[di]['expiryDate'] == ed:
            call_data = data[di].get('CE', {})
            put_data = data[di].get('PE', {})
            
            row_data = {
                'OI Calls': call_data.get('openInterest', ''),
                'Chng in OI Calls': call_data.get('changeinOpenInterest', ''),
                'Volume Calls': call_data.get('totalTradedVolume', ''),
                'IV Calls': call_data.get('impliedVolatility', ''),
                'LTP Calls': call_data.get('lastPrice', ''),
                'Chng Calls': call_data.get('changeinOpenInterest', ''),
                'Bid Qty Calls': call_data.get('bidQty', ''),
                'Bid Calls': call_data.get('bidprice', ''),
                'Ask Calls': call_data.get('askPrice', ''),
                'Ask Qty Calls': call_data.get('askQty', ''),
                'Strike Calls': call_data.get('strikePrice', ''),
                'Bid Qty Puts': put_data.get('bidQty', ''),
                'Bid Puts': put_data.get('bidprice', ''),
                'Ask Puts': put_data.get('askPrice', ''),
                'Ask Qty Puts': put_data.get('askQty', ''),
                'Chng Puts': put_data.get('changeinOpenInterest', ''),
                'LTP Puts': put_data.get('lastPrice', ''),
                'IV Puts': put_data.get('impliedVolatility', ''),
                'Volume Puts': put_data.get('totalTradedVolume', ''),
                'Chng in OI Puts': put_data.get('changeinOpenInterest', ''),
                'OI Puts': put_data.get('openInterest', ''),
            }
            oc_data.append(row_data)

df = pd.DataFrame(oc_data)
df.to_excel("option_chain_data.xlsx", index=False)
# pprint(oc_data)