# iterable
# iterator

sayilar = [1,2,3,4,5] # bu liste üzerine for döngünüsü ile her elemanı dolaşabiliyoruz.

for i in sayilar:
    print(i) # bu dolaşabilme özelliğine iterable diyoruz.

print(dir(sayilar)) # bu bize, verilen değişkenin hangi metotlara sahip olduğunu söyler. __iter__ metodu dolaşaiblmeye imkan verir. 

sayilar2 = [1,2,3,4,5,6]
#print(next(sayilar2)) # 'list' object is not an iterator hatası alırım. for dönügüsü bunu bizim için iterator yapar. ancak biz elle nasıl yaparız.

_iter_sayilar = iter(sayilar2)
print(next(_iter_sayilar)) # 1
print(next(_iter_sayilar)) # 2 diye elemanları tek tek alabiliriz.

while True: # bu döngü sayesinde son elemana kadar yazar.
    try:
        sayi = next(_iter_sayilar)
        print(sayi)
    except StopIteration:
        break
