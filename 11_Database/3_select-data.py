import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Sql132313",
    database = "shopdb" 
)

cursor = db.cursor() 

sql = "SELECT * FROM products"

cursor.execute(sql)
products = cursor.fetchall() # tüm satırları çekip liste halinde alır.

for p in products:
    print(p)
