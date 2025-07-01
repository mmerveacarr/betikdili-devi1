# hafta4.py

cümle = (
    "There may be times when you want to specify a type on to a variable. "
    "This can be done with casting. Python is an object-orientated language, "
    "and such as it uses classes to define data types, including its primitive types."
)

kelimeler = cümle.split()

def hesapla(kelimeler):
    uzunluklar = []
    for kelime in kelimeler:
        uzunluk = len(kelime)
        uzunluklar.append(uzunluk)
        print(f"{kelime}: {uzunluk} harf")
    return uzunluklar

sonuc = hesapla(kelimeler)
print("\nTüm uzunluklar:", sonuc)
