import re

text = "ABC 123 XYZ 456 $#£ 300"

pattern = r"\d\d\d" # \d sayı içeriyorsa demek. 3 tane yan yana kullandım. 3 sayı yan yana olmalı. 

match = re.findall(pattern, text)

sonuc = match

print(sonuc)