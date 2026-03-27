import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Sql132313",
    database = "shopdb" 
)

cursor = db.cursor() 

# sql = "DELETE FROM products WHERE id=4"
# cursor.execute(sql)
# db.commit()

sql2 = "INSERT INTO products (id, name, price, imageUrl, description) VALUES(%s,%s,%s,%s,%s)"
values = (3,"Iphone 16", 70000, "3.jpg", "güzel telefon")
cursor.execute(sql2, values)
db.commit()