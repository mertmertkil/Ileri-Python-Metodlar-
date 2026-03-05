# map func : bir fonksiyonu bir listenin her bir ögesine uygulayarak yeni bir liste oluşturur.

sayilar = [1,2,3,4,5]
kareleri = []

for kare in sayilar:
    kareleri.append(kare ** 2)

print(kareleri) # 1,4,9,16,25

# bunu map func sayesinde daha kolay yapabiliriz.

def kupAl(sayi):
    return sayi ** 3

sonuc = map(kupAl, sayilar)
print(sonuc) # <map object at 0x1026db1c0>  adres verdi ama çıktı üretmedi. bunun için list fonksiyonu da kullanıyoruz.

sonuc = list(sonuc) # bunu direkt 16.satırda map'i kapsayacak şekilde de yazabilirim. list(map(kupAl, sayilar))
print(sonuc) # 1,8, 27,64,125

# bunu lambda ile birleştirerek daha da kolay yapabiliriz.

bes_kat = list(map(lambda a: a * 5, sayilar))
print(bes_kat) # 5,10,15,20,25

# map fonksiyonunda ilk parametre olarak hazır func'ta verebiliriz.

str_sayilar = ["1","2","3","4","5"]
print(str_sayilar) #'1', '2', '3', '4', '5']

int_sayilar = list(map(int, str_sayilar)) # doğrudan int'e çevirir.
print(int_sayilar) #1, 2, 3, 4, 5]
