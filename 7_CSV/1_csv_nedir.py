import csv

# csv dosyası: virgüllerle ayrılmış dosya tipi.

with open("onlinefoods.csv") as file:
    csv_reader = csv.reader(file)

    # print(list(csv_reader)[0]) # listeye çevirip başlıkları almak ne kadar kolay. 
    next(csv_reader) # ilk satırı atlamak için kullandım.
    #yaşı 23 ten küçük olanları getirelim.

    for i in csv_reader:
        i[0] = int(i[0])
        if i[0] < 23 :
            print(i)

    