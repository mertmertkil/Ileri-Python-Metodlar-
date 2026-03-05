# class tanımı

class CartItem:
  
    # constructor method
    def __init__(self, name, price, quantity):
        # instance attribues
        self.name = name
        self.price = price
        self.quantity = quantity
        

    #instance methods
    def calculate_total(self):
        return self.quantity * self.price # self aracılığıyla class içindeki attribues'lere ulaşabilirim.

item1 = CartItem("Telefon", 50000, 2)
item2 = CartItem("Bilgisayar", 70000, 4)
item3 = CartItem("Kitap", 200, 3)


print(f"{item1.name} adlı üründen {item1.quantity} tane aldınız. Toplam fiyat {item1.calculate_total()}")
print(f"{item2.name} adlı üründen {item2.quantity} tane aldınız. Toplam fiyat {item2.calculate_total()}")
print(f"{item3.name} adlı üründen {item3.quantity} tane aldınız. Toplam fiyat {item3.calculate_total()}")

 

