# serialize, deserialize'nin tersi. uygulama tarafında yazdığım bir ifadeyi dosyaya yazılacak hale metin haline getirme.

product = {
    "id": 2,
    "title": "Macbook Pro",
    "price": 90000,
    "rating": 4.5,
    "category": "Bilgisayar",
    "color": ["Red", "Blue"],
}

print(product)
print(type(product)) # class dictinary

import json

sonuc = json.dumps(product) # eğer veriyi json stringe çevireceksek dumps metodunu kullanıyoruz.
print(product["title"])

# eğer doprudan json formatında dosyaya yazacksak dump metodunu kullanıyoruz.

with open("product.json","w") as file:
    json.dump(product, file)
