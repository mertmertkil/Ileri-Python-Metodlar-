import csv

# with open("arabalar.csv","w") as file: # arabalar adında yeni bir dosya oluşturdum, writer modunda açtım ve altta da bağlantısını oluşturdum.
#     csv_writer = csv.writer(file)
#     # csv_writer.writerow(["Marka","Model"])
#     # csv_writer.writerow(["Toyota","Corolla"])
#     # csv_writer.writerow(["Mazda","CX-5"])

# # yukarıda tek tek yaptığımız satırları "writerows" ile bir kerede yapabiliriz.

#     csv_writer.writerows([["Marka","Model"], ["Toyota","Corolla"], ["Toyota","Yaris"] ])

 # oluşturduğumuz dosyaya bilgi eklemek için "a" modunda açmalıyız.

# with open("arabalar.csv","a") as file:
#     csv_writer = csv.writer(file)
#     csv_writer.writerow(["Mazda","CX-5"])
 
# şimdi, bir dosyadan diğer dosyaya yazalım.

with open("onlinefoods.csv") as file:
    csv_reader = csv.reader(file)
    with open("new-foods.csv", "w") as f:
        csv_writer = csv.writer(f)
        for food in csv_reader:
            csv_writer.writerow(u.upper() for u in food) # hepsini al büyük yaz.