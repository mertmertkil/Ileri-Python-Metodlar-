# Tanımlanacak olan sınıfların temelde nasıl davranması gerketiğini meta classlar içinde tanımlayabiliriz.

class Meta(type):
    def __new__(self, class_name, bases, attrs):
        print(attrs)
    
        a = {}

        for name, val in attrs.items():
            if name.startswith("_"):
                a[name] = val
            else:
                a[name.upper()] = val

        return type(class_name, bases, a)
    


class Person(metaclass=Meta):
    x=5
    y=10
    _age = 50

    def hello():
        print("merthaba")

        
p = Person()

#sonuc = p.x # hata verir. çünkü person clasının metasında dedim ki, bu clasa değişken tanımlanırken değişken isimlerini büyük yap.
sonuc = p.X
sonuc = p.Y
print(sonuc)