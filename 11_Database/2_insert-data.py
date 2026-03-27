# oluşturduğumuz tabloya, python üzerinden veri ekleyelim.

import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Sql132313",
    database = "shopdb" 
)

cursor = db.cursor() # veri tabanına girmek için gerekli cursor'u oluşturduk.

sql = "INSERT INTO products (name, price, imageUrl, description) VALUES (%s,%s,%s,%s)"

# insert into, tabloya veri eklemek için kullanılan sql komutu. %s yer tutucu.

# values = ("Iphone 16", 70000, "3.jpg", "iyi bir telefon") # burayı işim bitince yoruma aldım ve altta, birden fazla satır ekliyoruz.

# şimdi tanımladığımız değişkenleri execute ile veri tabanına gönderelim.

# cursor.execute(sql, values) # bu da ilkinin eklemesi. birden fazla satır olduğunda executemany metodu çağrılır.

# values = [
#     ("Iphone 17", 80000, "4.jpg", "iyi bir telefon"),
#     ("Iphone 18", 90000, "5.jpg", "iyi bir telefon"),
#     ("Iphone 19", 100000, "6.jpg", "iyi bir telefon"),    
#     ]

# cursor.executemany(sql, values)


# # şimdi değişiklikleri commit edelim.

# db.commit()

# print(cursor.rowcount, " kayıt eklendi")

### hepsini yoruma alıp yeni kayıt ekleyeceğim ama try bloğu kullanacağım.

values = [
    ("Samsung S25", 35000, "7.jpg"," kore malı"),
    ("Samsung S26", 45000, "8.jpg"," kore malı")
]

cursor.executemany(sql, values)

try:
    db.commit()
    print(cursor.rowcount, " satır eklendi")
    print(f"son eklenen kaydın id'si:{cursor.lastrowid} ")
except mysql.connector.Error as err:
    print("hata: ", err)
finally:
    cursor.close()
    db.close()
    print("bağlantı sonlandı.")