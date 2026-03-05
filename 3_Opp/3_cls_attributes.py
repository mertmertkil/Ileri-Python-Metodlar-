# class tanımı

class CartItem:
    
    #  class attribues
        
    discount_rate = 0.8
    item_count = 0

    # constructor method
    def __init__(self, name, price, quantity):
        # instance attribues
        self.name = name
        self.price = price
        self.quantity = quantity
        CartItem.item_count += 1
        
    #instance methods
    def calculate_total(self):
        return self.quantity * self.price # self aracılığıyla class içindeki attribues'lere ulaşabilirim.

item1 = CartItem("Telefon", 50000, 2)
item2 = CartItem("Bilgisayar", 70000, 4)
item3 = CartItem("Kitap", 200, 3)
print(f"{CartItem.item_count} tane ürün sepetinizde")


 

