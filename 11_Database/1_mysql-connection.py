import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Sql132313",
    database = "shopdb" #  sonra, çalışacağımız db yi de ekledik.
)

# print(db) # bağlantı kontrolü için yazıldı.

cursor = db.cursor() # cursor, imleç demek aslında. bağlantı kapıyı açar, cursor ise içeri girip raflar arasında gezmemizi sağlar.

# cursor.execute("SHOW DATABASES") # cursor aracığı ile SQL sorgumu buradan yazabiliyorum. 

# for i in cursor: # yoruma alıyorum allta bir db yaratıp yeniden sorgulayacağım.
#     print(i)

# cursor.execute("CREATE DATABASE ornekdb")
# cursor.execute("SHOW DATABASES")

# for i in cursor:
#     print(i)

# cursor.execute("DROP DATABASE ornekdb")
# cursor.execute("SHOW DATABASES")

# for i in cursor:
#     print(i)

cursor.execute("SHOW TABLES")
for i in cursor:
    print(i)