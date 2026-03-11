# queryString; http isteğinin sonunda, filtreleme yapmamı sağlayan key-value değeri. htttps://btkakademi.gov.tr?python sa

import requests
import json

response = requests.get("https://jsonplaceholder.typicode.com/todos?userId=1&completed=true")

todos = response.json()

sonuc = todos

print(sonuc)