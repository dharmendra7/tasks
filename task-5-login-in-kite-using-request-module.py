import requests
from pprint import pprint

url = f"https://kite.zerodha.com/api/login"
user_id = "AB0001"
password = "123456"

payload = {
    "user_id" : user_id,
    "password": password
}

response = requests.post(url, payload)

print(response.json())