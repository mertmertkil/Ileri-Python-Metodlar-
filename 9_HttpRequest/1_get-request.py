import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts")

sonuc = response # response 200 | bir response cevabı döndü, 200 koduyla
sonuc = type(response) # class
sonuc = response.text # ile içeriği alabilirim. ama işlemek için bir önceki ünitede olduğu gibi deserialize yapmak lazım.

print(sonuc)
