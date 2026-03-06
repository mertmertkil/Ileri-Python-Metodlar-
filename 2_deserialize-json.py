with open("product.json") as file:
    data = file.read()

print(data) # içeriği alabilirim ama string sınıfında.
print(type(data)) # class str
# print(data["title"]) # bunu alamam. çünkü str sınıfına indexle erişilir, bu şekilde key value olarak erişemem.

# deserialize etmem gerek yani => decode etmek, uygulamada kullanabileceğim şekle sokmak.

import json

with open("product.json") as file:
    data = json.load(file)

print(data)
print(type(data)) # class dictinary
print(data["title"]) # yanıtı aldım macbook pro
print(data["price"]) 
print(data["category"]) 

# bir de loads metodu var. o da, uygulama içindeki bir str ifadeyi kullanmak istediğimde kullanılıyor.

