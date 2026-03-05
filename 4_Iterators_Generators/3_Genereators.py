# generator : bize iterator oluşturan bir fonksiyon

def counter(max):
    sayi = 1
    sayilar = []

    while sayi <= max:
        sayilar.append(sayi)
        sayi += 1

    return sayilar

sonuc = counter(20)

print(sonuc) # bu şekilde liste alabilirim. ancak büyük verilerde bu bellek kaybı anlamına gelir.

def sayac(max):
    sayi = 1
    while sayi <= max:
        yield sayi
        sayi +=1

sonuc2 = sayac(20)
print(sonuc2) # generator object sayac at 0x104... bellek gösteriyor. next metoduyla verilerle tek tek erişebilirim.

print(next(sonuc2)) # 1
print(next(sonuc2)) # 2
print(next(sonuc2)) # 3