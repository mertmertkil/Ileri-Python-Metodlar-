# aggregate fonksiyonları: hesaplama fonksiyonları olarak karşımıza çıkıyor.

# yine db bağlantımızı yapalım.

import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Sql132313",
    database = "shopdb" 
)

cursor = db.cursor()

# sql = "SELECT COUNT(*) FROM products" # Count: satır sayısını sayıyor.
# sql = "SELECT AVG(price) FROM products" # AVG: ortalamasını alır
# sql = "SELECT SUM(price) FROM products" # SUM: toplamını bulur.
# sql = "SELECT MIN(price) FROM products" # MIN: EN düşük fiyatı bulur.
sql = "SELECT name,price FROM products WHERE price = (SELECT MAX(price) FROM products)" # MIN: EN düşük fiyatı bulur.



cursor.execute(sql)
result = cursor.fetchone()

# print(f"Veri tabanımızda toplam {result} adet ürün bulunmaktadır.")
# print(f"Veri tabanımızdaki ürünlerin fiyatının ortalaması {result}' dır")
# print(f"Veri tabanımızdaki ürünlerin fiyatının toplamı {result}' dır")
# print(f"Veri tabanımızdaki ürünlerin en ucuzu fiyatı {result}' dır")
print(f"Veri tabanımızdaki en pahalı ürünün adı ve fiyatı {result}' dır")




# sql ="ALTER TABLE products MODIFY price DECIMAL(10,2);" # price ı varchar yapmışız onu değiştirdik.
# cursor.execute("DESCRIBE products")
# for column in cursor.fetchall():
#     print(column)