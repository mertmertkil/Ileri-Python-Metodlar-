def selamlama(fn):
        def inner(*args, **kyargs):
             print("Hoş geldiniz.")
             fn()
             print("Güle güle")
        return inner

@selamlama # decarator
def gunaydın(ad = input("Ad gir")):
    print(f"Günaydın benim adım {ad}")

@selamlama
def iyigunler():
    print("İyi günler benim adım Mert")


gunaydın()
iyigunler()