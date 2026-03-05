# min-max: bir liste üzerindeki min ve max değerleri alır
isimler = ["ali", "ahmet","sena", "yiğit"]
sayilar = [1,4,6,65,54,32]

sonuc = min(sayilar)
sonuc2 = max(sayilar)
print(sonuc) # 1
print(sonuc2) # 65


sonuc = max(isimler, key = lambda isim: len(isim))
sonuc = min(isimler, key = lambda isim: len(isim))
print(sonuc)

urunler = [
    {"title": "samsung s23", "price": 70000},
    {"title": "samsung s24", "price": 90000},
    {"title": "samsung s14", "price": 40000}
]

sonuc = min(urunler, key= lambda urun: urun["price"])["title"]
print(sonuc)