import requests
from pprint import pprint

url = f"https://api.boerse-frankfurt.de/v1/data/dividend_information"

payload = {
    "isin": "DE000A1EWWW0",
    'limit': 5
}

header = {
    "authority":"api.boerse-frankfurt.de",
    "method":"GET",
    "path":"/v1/data/master_data_bond?isin=XS0216072230",
    "scheme":"https",
    "accept":"application/json, text/plain, */*",
    "accept-encoding":"gzip, deflate, br",
    "accept-language":"en-US,en;q=0.6",
    "client-date":"2022-08-26T18:35:26.470Z",
    "origin":"https://www.boerse-frankfurt.de",
    "referer":"https://www.boerse-frankfurt.de/",
    "x-client-traceid":"21eb43fb86f0065542ba9a34b7f2fa93",
    "x-security":"14407a81ab4670847d3d55b0d74a3aea",
}

response = requests.get(url, headers=header)

print(response.json())


#Can not able to get data through this api