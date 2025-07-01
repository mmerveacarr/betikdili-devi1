# hafta5extra.py

isimler = ['merve acar', 'yaren parlak', 'efe akar']

def harf_sayisi(isimler):
    for isim in isimler:
        parcala = isim.split(' ')
        for parca in parcala:
            print(f"{parca}: {len(parca)} harf")

harf_sayisi(isimler)
