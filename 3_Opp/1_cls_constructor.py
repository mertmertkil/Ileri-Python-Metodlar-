# class tanımı

class CartItem:
    
    # constructor method : yapıcı metod. her yeni üyede çalıştırılacak komutlar. self parametresi ile erişiriz
    
    def __init__(self, name, price, quantity):
        # instance attribues
        self.name = name
        self.price = price
        self.quantity = quantity
        
item1 = CartItem("Telefon", 50000, 2)
item2 = CartItem("Bilgisayar", 70000, 4)
item3 = CartItem("Kitap", 200, 3)

print(item1.name)


 

