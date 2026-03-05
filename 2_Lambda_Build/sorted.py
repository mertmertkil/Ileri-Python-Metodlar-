# # sorted : sıralama yapar

# sayilar = [1,53,4,5,65,23]
# sonuc = sorted(sayilar)
# print(sonuc)
# print(sayilar) # orjinal liste değişmez.

# sonuc = sorted(sayilar, reverse=True) # ters çevirir.
# print(sonuc)


users = [
    {"username": "mertmertkil", "posts": ["post1", "post2", "post3"], "email": "mertmertkil@gmail.com"},
    {"username": "mervemertkil", "posts": ["post1", "post2"], "email": "mervemertkil@gmail.com"},
    {"username": "güneşmertkil", "posts": ["post1", "post2", "post3", "post4"], "email": "güneşmertkil@gmail.com"}
]

# sonuc = sorted(users, key=len) # key bilgilerinin sayısına göre listeler.
# print(sonuc)

# sonuc = sorted(users, key = lambda user: user["username"])
# print(sonuc)

sonuc = list(map(lambda user: user["username"] ,sorted(users, key= lambda user: len(user["posts"]))))
print(sonuc)