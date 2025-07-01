import random

print("⚽ Maç Simülasyonu: Fenerbahçe vs Galatasaray\n")

fenerbahce = random.randint(0, 10)
galatasaray = random.randint(0, 10)

print(f"Fenerbahçe: {fenerbahce}")
print(f"Galatasaray: {galatasaray}")

if fenerbahce > galatasaray:
    print("🏆 Fenerbahçe kazandı!")
elif fenerbahce == galatasaray:
    print("🤝 Maç berabere.")
else:
    print("🏆 Galatasaray kazandı!")
