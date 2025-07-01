# hafta5.py

t1 = '17.1.2002'
tarih1 = list(map(int, t1.split('.')))
gun1, ay1, yıl1 = tarih1

t2 = '3/8/2005'
tarih2 = list(map(int, t2.split('/')))
gun2, ay2, yıl2 = tarih2

kategoriler = ['saglik', 'dunya', 'teknoloji']
gazeteler = ['sabah', 'hurriyet', 'milliyet']

for gazete in gazeteler:
    site = f"www.{gazete}.com.tr"
    for kategori in kategoriler:
        for yil in range(yıl1, yıl2 + 1):
            for ay in range(1, 13):
                for gun in range(1, 31):
                    print(f"{site}/{kategori}/{yil}-{ay:02}-{gun:02}")
