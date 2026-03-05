# sum : toplama işleminde kullanılıyor.

sayilar = [1,3,4,5,32,56]
sonuc = sum(sayilar)
print(sonuc)

products = [
    {"title": "Iphone 15", "price" : 56000},
    {"title": "Iphone 16", "price" : 66000},
    {"title": "Iphone 17", "price" : 76000}
]

toplamFiyat = sum([urun["price"] for urun in products])
print(toplamFiyat)

ortalama = toplamFiyat / len(products)
print(ortalama)

# round : yuvarlama yapar.

sonuc = round(1.32, 1)

print(sonuc)