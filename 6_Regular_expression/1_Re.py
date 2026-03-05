# regular expression: bir metin içerisinde istediğimiz şeyi bulmamıza yarar.
# bkz: metakarakterler

import re

text = "BTK akademi Python dersleri BTK"

pattern = "BTK"

sonuc = re.search(pattern, text) # search bulduğu ifadeyi döndürür.

sonuc = re.findall(pattern, text) # findall dizi şeklinde döndürür.

print(sonuc)