class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        print("Person sınıfı türetildi.")

    def intro(self):
        print(self.name, self.surname, self.age) # bu metodu yazdıktan sonra da student içinden erişebilirim.

class Student(Person): # Kalıtım parantez içi ile sağlanıyor. Artık person'ın bütün özellikleri student ve teacher için gerekli
    pass

class Teacher(Person):
    pass

p1 = Person("mert", "mertkil", 33)
print(p1.name, p1.surname, p1.age) # bu şekilde zaten erişebilirim. ancak artık student içinden de erişebilirim.

s1 = Student("güneş", "mertkil", 1)
print(s1.name, s1.surname, s1.age) # bu satır yerine direkt 8.satırdaki metodu da çağırabilirim.
s1.intro()