# ben bu verileri, key value şeklidne almak istiyorum.

import csv

with open("onlinefoods.csv") as file:
    csv_reader = csv.DictReader(file)
    for i in csv_reader:
        print(i["Occupation"])