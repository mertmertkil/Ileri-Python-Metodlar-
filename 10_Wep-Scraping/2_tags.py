from bs4 import BeautifulSoup

with open("index.html") as file:
    html = file.read()

obj = BeautifulSoup(html, "html.parser")

sonuc= obj
sonuc = obj.prettify() # html formatına uygun yazar. yani tag altındaki tgler bir satır içinde okunaklı halde döndürür.
sonuc = obj.title
sonuc = obj.body
sonuc = obj.body.h1 # <h1 id="header"> Python Kursu </h1> 
sonuc = obj.body.h1.string #  Python Kursu  sadece içerik.
 # bu yöntem karşılaştığı ilk uygun şeyi bulur ve döndürür.

 


print(sonuc) 



