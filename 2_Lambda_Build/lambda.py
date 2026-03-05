#lambda arguments : expression

# normal fonksiyon yapısı:

def kareAl(i):
    return i ** 2

print(kareAl(9))

# lambda fonk yapısı:

sonuc = (lambda a : a ** 2)(3)
print(sonuc)

toplama = (lambda a,b,c : a+b+c)
print(toplama(1,2,3))