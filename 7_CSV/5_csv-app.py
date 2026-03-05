# onlinefoods.csv

# Online yemek siparişi veren kaç kişi var.
# Online yemek siparişi verne öğrencileri listeleyin.
# 20-30 yaş aralığındaki kişilerin listesini hazırlayın.

import csv

with open("onlinefoods.csv") as file:
    csv_reader = csv.reader(file)
    liste = list(csv_reader)
    print(f"Online yemek siparişi veren kişi sayısı: {len(liste)-1 }'dir") # -1 çünkü, ilk satırda başlıklar var.

with open("onlinefoods.csv") as file:
    csv_reader = csv.DictReader(file)
    adet = len([user for user in csv_reader if user["Occupation"] == "Student"])
    print(f"Yemek siparişi veren öğrenci sayısı {adet} tanedir.")

with open("onlinefoods.csv") as file:
    csv_reader = csv.DictReader(file)
    users = (user for user in csv_reader if int(user["Age"]) >=20 and int(user["Age"]) <30 )
    for i in users:
        print(i["latitude"], i["longitude"])
