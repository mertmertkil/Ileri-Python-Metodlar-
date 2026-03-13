from bs4 import BeautifulSoup

with open("index.html") as file:
    html = file.read()

obj = BeautifulSoup(html, "html.parser")

sonuc = obj.find(id="item1")
sonuc = obj.find(id="item2").h2.a.string
sonuc = obj.find(class_="item")

sonuc = obj.select(".item") # select uyan tüm eşleşmeleri alır ve dizi döndürür. 

# burada css kurallarına benziyor. class için nokta, id içi # işareti kullanılır.


print(sonuc)