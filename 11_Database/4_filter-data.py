import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Sql132313",
    database = "shopdb" 
)

cursor = db.cursor() 

# sql = "SELECT * FROM products WHERE id=1"
# cursor.execute(sql)

# result = cursor.fetchone()
# print(result)

# bunu bir fonksiyon haline getirelim.

def getProductById(id):
    sql = "SELECT * FROM products WHERE id=%s"
    params = (id,)
    cursor.execute(sql, params)
    result = cursor.fetchall()
    print(result)

id = int(input("Lütfen öğrenmek istediğiniz ürünün ID'sini girin."))
getProductById(id)
