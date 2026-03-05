# child class : kalıtım alan alt sınıf

class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        print("Person sınıfı türetildi.")

    def intro(self):
        print(self.name, self.surname, self.age) 

class Student(Person):
    # def __init__(self):
    #     print("Student sınıfı üretildi.") # burada hata alırım. çünkü student init'i çağırıldı ve veriler yok. 
    def __init__(self, name, surname, age, number): # ekstra özellik de bu şekilde ekleyebilirim.
        Person.__init__(self, name, surname, age) # temel sınıfın init'ini çağrımak gerek.
        # person sınıfını kullanmak yerine, üst sınıfı hatırlamayabiliriz. super metodu çağırabilirim. onu da teacher 'da gösteriyorum.
        self.number = number
        print("student sınıfı türetildi.")

    def study(self):
        print(f"{self.name} ders çalışıyor.")

    def intro(self):
        print(self.name, self.surname, self.age, self.number) # person'daki metodu bu şekilde ezebiliriz. 

class Teacher(Person):
    def __init__(self, name, surname, age, branch):
        super().__init__(name, surname, age, )
        self.branch = branch
        print("Teacher türetildi.")

    def teach(self):
        print(f"{self.name} {self.branch} ders anlatıyor.")

   

p1 = Person("mert", "mertkil", 33)
print(p1.name, p1.surname, p1.age)

s1 = Student("güneş", "mertkil", 1, 105)
print(s1.name, s1.surname, s1.age) 
s1.intro()
s1.study()

t1 = Teacher("Merve", "Mertkil", 32, "Rehber")
t1.intro()
print(t1.branch)
t1.teach()