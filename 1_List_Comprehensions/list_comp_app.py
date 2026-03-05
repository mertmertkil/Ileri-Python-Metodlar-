# 1-100 arası sayılardan 12'ye bölülenlerle yeni liste oluştur.

list = [bolunenler for bolunenler in range(1,100) if bolunenler %12 ==0]

print(f"1 ile 100 arasında 12'ye tam bölünen sayılar: {list}") # 1 ile 100 arasında 12'ye tam bölünen sayılar: [12, 24, 36, 48, 60, 72, 84, 96]

# Verilen text içerisinde rakamları içeren bir liste oluştur.

rakamlar = range(0,10)

text = "Hello world 12345 world"

rakam_list = [rakam for rakam in text if rakam.isdigit()]

print(rakam_list)

# Sıcaklıklar listesinde bulunan her hava sıcaklık bilgisine göre 4derecenin altında buzlanma tehlikesi yaz.

sicakliklar = [20,15,0,-5,-2]

buzlanma = [buz if buz>4 else f"buzlanma tehlikesi" for buz in sicakliklar ]

print(buzlanma)

# öğrecilen ve notlar listelerindeki notu 50'den fazla olanları dict verisinde yadzır:

ogrenciler = ["ali", "ahmet", "canan"]
notlar = [50,60,80]

not_list = [(ogrenciler[i], notlar[i]) for i in range(0,len(ogrenciler))]
print(not_list)

list_dict ={key:value for key,value in not_list if value>50}
print(list_dict)

# for döngüsüyle yazılan işlemi list comp formatında yaz:

end = []

for x in range(3):
    for y in range(3):
        end.append((x,y))
print(end)

end_comp = [(x,y) for x in range(3) for y in range(3)]
print(end_comp)