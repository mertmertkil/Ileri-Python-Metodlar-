# map ile aynı yapıda. koşula bağlı listeler.

sayilar = [1,2,3,4,5]

filt = list(filter(lambda x: x%2 == 0, sayilar))

print(filt)

# örnek 2 

isimler = ["ali","arda","mahmut","mustafa","selvi"]

filtA = list(filter(lambda x: x[0] == "a", isimler))

print(filtA)

# map içinde filter da kullanılabil.

users = [
    {"username": "mert mertkil", "posts": ["post1", "post2"]},
    {"username": "merve mertkil", "posts": ["post1"]},
    {"username": "güneş mertkil", "posts": ["post1", "post2","post3"]}
]

filteredResult = list(filter(lambda u: len(u["posts"])>1, users))
map_filters = list(map(lambda u: u["username"] ,filteredResult))
print(map_filters)