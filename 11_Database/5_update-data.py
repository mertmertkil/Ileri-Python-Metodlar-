import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Sql132313",
    database = "shopdb" 
)

cursor = db.cursor() 

sql = "UPDATE products SET name ='Samsung S25-update' WHERE id=1"
cursor.execute(sql) 

try:
    db.commit()
    print(f"{cursor.rowcount} tane kayıt güncellndi.")
except mysql.connector.Error as err:
    print(err)
finally:
    db.close()
    cursor.close()
