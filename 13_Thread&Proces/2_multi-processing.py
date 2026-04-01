import time
import multiprocessing


def calculate_square(numbers, list):
    print("kare hesaplanıyor...")

    for index, value in enumerate(numbers):
        time.sleep(0.3)  # siteme bekletiyorum.
        # print(f" {i}'nin karesi: { i* i} ")
        list[index] = value * value


def calculate_cube(numbers, list):
    print("küp hesaplanıyor...")

    for index, value in enumerate(numbers):
        time.sleep(0.3)  # siteme bekletiyorum.
        # print(f"{i}'nin kübü: {i*i*i}")
        list[index] = value * value * value


if __name__ == "__main__":
    arr = [2, 4, 6, 8, 12, 56, 126, 256, 512, 1024]

    t = time.time()

    list_square = multiprocessing.Array("i", len(arr))
    list_cube = multiprocessing.Array("i", len(arr))

    p1 = multiprocessing.Process(target=calculate_square, args=(arr, list_square))
    p2 = multiprocessing.Process(target=calculate_cube, args=(arr, list_cube))
    p1.start()
    p2.start()

    p1.join()  # p1 işlemi bitene kadar bekle.
    p2.join()  # p2 işlemi bitene kadar bekle.

    t = time.time()

    print(f"list_square: {list(list_square)}")
    print(f"list_cube: {list(list_cube)}")
    print(f"işlem tamamlandı. {time.time()- t}")
