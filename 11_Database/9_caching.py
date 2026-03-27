# memory caching, veri tabanı trafiğini azaltmak için kullandığımız bir bellekleme yöntemi.
# veriyi belli bir süre hafıza alarak her seferinde db'ye gitmemek için kullanılıyor. 
# yoğun trafiği olan programlarda bu da veri akışını hızlandırıyor.

import mysql.connector
from cachetools import cached, TTLCache
import time

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Sql132313",
    database = "shopdb" 
)

@cached(cache=TTLCache(maxsize=32, ttl=(60*60))) # ne kadar veri tutacağı ve ne kadar tutacağı saniye * 60 = 1 saat dedik
def getProducts():
    cursor = db.cursor()
    sql = "SELECT p.name, c.name FROM products p  inner join categories c on p.categoryid = c.id WHERE c.id=2" 
    cursor.execute(sql)
    print("from sql") # bilginin sqlden geldiğini kontrol edicez.
    return cursor.fetchall()
    
s = time.time()
print(getProducts()) # ilkinde from sql geliyor ama sonrasında metod çalıştırılmıyor. bellekte tutuluyor bu yüzden sonuç geliyor sadece
print("geçen zaman:", time.time()- s)

s = time.time()
print(getProducts())
print("geçen zaman:", time.time() - s)

s = time.time()
print(getProducts())
print("geçen zaman:", time.time()- s)


