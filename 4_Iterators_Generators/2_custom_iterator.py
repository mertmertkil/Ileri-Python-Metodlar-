# kendi tanımladığımız bir class'a iterable özelliği tanımlayacağız.

class MyNumbers:
    def __init__(self ,start, stop):
        self.start = start
        self.stop = stop
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start <= self.stop:
            x = self.start
            self.start +=1
            return x
        else:
           raise StopIteration

for i in MyNumbers(20,3000):
    print(i) # class'lar iterable olmadığı için bu şekilde veri alamam. bu yüzden class içinde metot tanımlamalıyım.



    