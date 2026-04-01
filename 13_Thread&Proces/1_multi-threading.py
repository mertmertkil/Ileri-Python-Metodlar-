# thread, işlemleri ardışık ele almak yerine eş zamanlı çalıştırmaya yarayan kavram.

import time


def calculate_square(numbers):
    print("kare hesaplanıyor...")

    for i in numbers:
        time.sleep(0.3)  # siteme bekletiyorum.
        print(f" {i}'nin karesi: {i * i} ")


def calculate_cube(numbers):
    print("küp hesaplanıyor...")

    for i in numbers:
        time.sleep(0.3)  # siteme bekletiyorum.
        print(f"{i}'nin kübü: {i*i*i}")


sayilar = [3, 5, 6, 8, 9]

t = time.time()

# calculate_square(sayilar)
# calculate_cube(sayilar) # thread için yoruma aldık.


# buraya kadar normal şekilde işlemi gerçekleştirdik. şimdi ise thread kullanarak işlemi gerçekleştirelim.

import threading

t1 = threading.Thread(target=calculate_square, args=(sayilar,))
t2 = threading.Thread(target=calculate_cube, args=(sayilar,))
t1.start()
t2.start()

t1.join()  # t1 işlemi bitene kadar bekle.
t2.join()  # t2 işlemi bitene kadar bekle.

print(f"işlem tamamlandı. {time.time()- t}")
