def filter(fn, liste):
    result = []
    for item in liste:
        if fn(item):
            result.append(item)
    return result
    
def is_even(num):
    return num %2 == 0

def is_positive(num):
    return num>0

sayilar = [1,4,5,6,89,76,45,-54,-43,-12]
print(filter(is_even, sayilar))
print(filter(is_positive, sayilar))

