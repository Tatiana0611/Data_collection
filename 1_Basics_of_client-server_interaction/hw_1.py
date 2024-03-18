# Сценарий Foursquare
# Напишите сценарий на языке Python, который предложит пользователю ввести интересующую его категорию (например, кофейни, музеи, парки и т.д.).
# Используйте API Foursquare для поиска заведений в указанной категории.
# Получите название заведения, его адрес и рейтинг для каждого из них.
# Скрипт должен вывести название и адрес и рейтинг каждого заведения в консоль.

import requests
import os
from dotenv import load_dotenv
import json

dotenv_path = "../.env"

if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

url = "https://api.foursquare.com/v3/places/search"

query = input("Введите категории для поиска: ")
near = input("Введите ближайший населенный пункт: ")

params = {
    "query": query,
    "fields": "name,location,rating",
    "near": near
}

headers = {
    "accept": "application/json",
    "Authorization": os.getenv("API_FOURSQUARE")
}

response = requests.get(url, headers=headers, params=params)
j_data = response.json()

with open('foursquare.json', 'w') as f:
    json.dump(j_data, f)

if response.ok:
    for i in j_data['results']:
        print('Название: ', i.get('name'))
        print('Адрес: ', i.get('location').get('formatted_address'))
        
        print('Рейтинг: ', i.get('rating'))
        print()
else:
    print("Запрос не может быть выполнен")
