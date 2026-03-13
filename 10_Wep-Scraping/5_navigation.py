from bs4 import BeautifulSoup

with open("index.html", encoding="utf-8") as file:
    html = file.read()

obj = BeautifulSoup(html, "html.parser")

sonuc = obj.body.div.contents # contents: bir etiketin alt ögelerini döndürür.
sonuc = obj.body.div.children # <generator object Tag.children.<locals>.<genexpr> at 0x102546e00>
# bunları yakaladık ama listeye almak için döngüye sokmam lazım.

for s in sonuc:
    print(s)

# print(sonuc)