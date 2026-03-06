import json

data = [
    {
        "id" : 1,
        "title": "Macbook Pro",
        "price": 80000
    },
    {
        "id" : 2,
        "title": "Macbook Air",
        "price": 70000
    }    
]

# with open("products.json", "w", encoding="utf-8") as file:
#     json.dump(data, file, ensure_ascii=False, indent=2) # diğer parametreler düzenli yazması için.
    
    #yukarıdaki işlemi yaptık, yorum satırına aldık.
    # yeni ürün nasıl eklerim:

# yeni bir ürün var

product = {
    "id": 3,
    "title": "Samsung S23",
    "price": 50000
}

with open("products.json") as file:
    products = json.load(file) # dosayadaki bilgileri pythonun veri formatına çevirdim.
    
products.append(product)

with open("products.json", "w", encoding="utf-8") as file:
    json.dump(products, file, ensure_ascii=False, indent=2)