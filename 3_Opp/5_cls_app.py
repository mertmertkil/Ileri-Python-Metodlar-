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

class ShoppingCard:
    def __init__(self, list):
        self.list = list

    def add_item(self, item):
        self.list.append(item)

    def display_item(self):
        for i in self.list:
            print(f"{i.name} {i.price}")

    def calculate_total(self):
        return sum([item.price * item.quantity  for item in self.list])
    
sc = ShoppingCard([item1, item2])

sc.add_item(item3)

sc.display_item()

print(sc.calculate_total())

 

