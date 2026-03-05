# List Comprehension: var olan bir listedeki elemanları başka bir listeye taşımak.
# Bunu yaparken, lsitenin özelliklerini de değiştirebilirim.

# bu şekilde yazmak yerine;

sayilar = []

for i in range(5):
    sayilar.append(i)

print(sayilar) # [0,1,2,3,4]

# Tek satırda da halledebilirim. İkisi de aynı çıktıyı verecektir.

sayilar2 = [i for i  in range(5)]

print(sayilar2) # [0,1,2,3,4]

# İ'nin özelliğini de değiştirebilirim:

sayilar3 = [i*3 for i in range(5)] # sayıları 3 ile çarparak listeyi oluşturacaktır.

print(sayilar3) # [0,3,6,9,12]

#

kurum = "btk akademi"

for i in kurum:
    print(i.upper()) # burada alt alta yazacakken;

kurum2 = "14 eylül ilkokulu"

sonuc = [i.upper() for i in kurum2]
print(sonuc) # burada ise bir liste haline getirerek tek satırda halledebilirim.