# [expression for i in liste if(koşul)]


# bu şekilde oluşturuduğum koşullu yapıyı yine tek satırda yazablirim.
sayilar = [3,5,7,6,56,34]
sonuc = []

for sayi in sayilar:
    if(sayi %2 == 0 ):
        sonuc.append(sayi)

print(sonuc) # 6,56,34

# tek satırda list comprehension yapısıyla yapalım:

sonuc_list = [sayi_list for sayi_list in sayilar if (sayi_list %2 == 0)]

print(sonuc_list) # 6,56,34

# else bloğunu da bu yapı içinde kullanmak mümkün:

else_list = [sayi_else if sayi_else %2 ==0 else f"{sayi_else} tek sayıdır" for sayi_else in sayilar]

print(else_list) #'3 tek sayıdır', '5 tek sayıdır', '7 tek sayıdır', 6, 56, 34]

