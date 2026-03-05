# US ALMA:

# def usalma(taban):
#     def inner(us):
#         return taban ** us
    
#     return inner

# sonuc = usalma(2)(4) # ikinci parantezde içteki fonksiyonun parametresi
# print(sonuc) 

# ya da :

# fn = usalma(2)
# sonuc2 = fn(4) # bu şekilde de kullanabiliriz.

# print(sonuc2)

# YETKİ SORGULAMA:
# def yetki_sorgulama(sayfa):
#     def inner(role):
#         if role == "Admin":
#             return f"{role} rolü {sayfa} sayfasına erişebilir."
#         else:
#             return f"{role} rolü {sayfa} sayfasına erişemez.."
        
#     return inner
        
# sorgu = yetki_sorgulama("Giriş paneli")
# onay = sorgu("Admin")
# red = sorgu("kullancı")

# print(onay)
# print(red)


# 4 İŞLEM:
def islem(islem_adi):

    def toplam(*args):
        toplam = 0
        for i in args:
            toplam += i
        return toplam

    def carpma(*args):
        carpim = 1
        for i in args:
            carpim *= i
        return carpim
    
    if islem_adi == "toplama":
        return toplam
    else:
        islem_adi == "carpma"
        return carpma

    
    
toplama = islem("toplama")
carpma = islem("carpma")

print(toplama(10,34,34,5,6,7,5,35,243))
print(carpma(34,5,6,7,6,54,32,3))

