# # (1-♾️) arasındaki her sayının karesini alan bir fonksiyon.

# def kareAl():
#     sayi = 0
#     while True:
#         yield sayi ** 2
#         sayi +=1

# generator = kareAl()
# print(next(generator))
# print(next(generator))
# print(next(generator))

# # for i in generator:
# #     print(i)


# fibonacci serisini hem normal fonk hem de generator kullanarak oluştur.

def fib_liste(max):
    sayilar = []

    a, b = 0, 1

    while len(sayilar) <= max:
        sayilar.append(b)
        a, b = b, a + b

    return sayilar

# print(fib_liste(9000)) # bu bellekte büyük bir yer kaplar. bunu generator ile yapalım.

def gen_list(max):
    a, b = 0 ,1
    count = 0
    while count <= max :
        a, b = b, a+b
        yield b
        count +=1
    
# for i in gen_list(9000):
#     print(i)

# performans 
import sys
list = [i for i in range(10000)]
print(sys.getsizeof(list)) # 85176

gene = (i for i in range(10000)) # yuvarlak parantez generator oluşturur.
print(sys.getsizeof(gene)) # 192