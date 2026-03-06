# şu ana kadar bilgileri liste şeklinde sakladık.
# şimdi dictinary şeklinde nasıl saklayacağız, öğrenelim.

data = {
    "2": {
        "title" : "MacbookAir",
        "price": 80000
    },
    "3": {
        "title" : "Samsung S24",
        "price": 50000
    }
}

import json

with open("products.json", "w") as file:
    json.dump(data, file, indent=2)

# sonrasında dosyayı okuyarak key ile doğrudan erişebilirim.

with open("products.json") as file:
    products = json.load(file)

print(products["2"]) # {'title': 'MacbookAir', 'price': 80000}