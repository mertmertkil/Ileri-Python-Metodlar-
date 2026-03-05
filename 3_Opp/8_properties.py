# properties: bir sınıfın niteliklerine kontrollü erişim için kullanılır.

class Product:
    def __init__(self, name, price):
        self.name = name
        if price>0:
            self._price = price
        else:
            raise ValueError("ürün fiyatı negatif olamaz.")
        
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if value>0:
            self._price = value
        else:
            raise ValueError("ürün fiyatı negatif olamaz.")
        
    # def set_price(self, value):
    #     if value>0:
    #         self.price = value
    #     else:
    #         raise ValueError("ürün fiyatı negatif olamaz.")
        
    # def get_price(self):
    #     return self._price

p = Product("Iphone 16", 80000)

print(p.price)

p.price = -90000
print(p.price)
# print(p.get_price())
# # print(p.name, p.price)