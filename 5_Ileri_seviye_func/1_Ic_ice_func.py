def faktoriyel(sayi):
    def inner_faktoriyel(sayi):
        if sayi <=1:
                return 1
        
        return sayi * inner_faktoriyel(sayi - 1)
    
    return inner_faktoriyel(sayi)

print(faktoriyel(5))