from bs4 import BeautifulSoup

with open("index.html", encoding="utf-8") as file:
    html = file.read()

obj = BeautifulSoup(html, "html.parser")

sonuc = obj.find("div") # find'ta ilk eşleşeni getirir.
sonuc = obj.find_all("div") # tüm divleri getirir.
sonuc = obj.find_all("div")[1] # 2.div i getirir.
sonuc = obj.find_all("div")[1].h2.a.string


for div in obj.find_all("div"):
    print(div.h2)