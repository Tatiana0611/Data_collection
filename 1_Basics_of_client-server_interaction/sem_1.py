import requests
import os
from dotenv import load_dotenv
import json
from pprint import pprint

dotenv_path = "../.env"
#dotenv_path = os.path.join(os.path.dirname(__file__), '.env')

if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

url = "https://api.giphy.com/v1/gifs/search"

params = {
    "api_key": os.getenv("API_KEY"),
    "q": "programming",
    "limit": 5,
    "offset": 0,
    "rating": "pg-13",
    "lang": "ru",
    "bundle": "messaging_non_clips",
}

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0",
           "Accept": "*/*",
}

response = requests.get(url, params=params, headers=headers)

j_data = response.json()

with open('gif.json', 'w') as f:
    json.dump(j_data, f)

for gif in j_data.get('data'):
    print(gif.get('images').get('original').get('url'))

pprint(j_data)

# print(response)
#
# response.headers
# response.status_code
# response.text
# response.content
#
# if response.ok:
#     print("Do something")
# else:
#     pass

