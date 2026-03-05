# all : tüm koşullar true ise true döner. and operatörü gibi.
# any : herhangi bir koşul true ise true döner. or operatorü gibi

# sayilar = [1,3,5,6,7,52,0]

# sonuc = all([bool(sayi) for sayi in sayilar])
# sonuc = any([bool(sayi) for sayi in sayilar])
# sonuc = any([sayi for sayi in sayilar if sayi %2 ==0])
# print(sonuc)

users = ["ahmet", "çınar", "ali"]
sonuc = [user[0] == "a" for user in users]
print(sonuc)