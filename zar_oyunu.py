import random

print("🎲 === ZAR OYUNU === 🎲")
print("Kural: 7 gelirse +10, 2 veya 12 gelirse -5 puan!\n")

puan = 0

for i in range(5):
    input(f"\n Tur {i+1} - Enter'a bas ve zarları at!")

    zar1=random.randint(1,6)
    zar2=random.randint(1,6)
    toplam= zar1+zar2

    print(f"🎲 Zar 1: {zar1}")
    print(f"🎲 Zar 2: {zar2}")
    print(f"📊 Toplam: {toplam}")

    if toplam==7:
        puan+=10
        print("🎉Süper! 7 geldi! +10 puan")
    elif toplam==2 or toplam==12:
        puan-=5
        print("😢 Kaybettin! -5 puan!")
    else:
        print("➡️ Devam...")

    print(f"💰 Güncel puan: {puan}")

print("\n" + "="*40)

if puan > 0 :
    print(f"🏆 Oyun bitti! Toplam puanın: {puan} - Kazandın!")
elif puan < 0:
    print(f"💔 Oyun bitti! Toplam puanın: {puan} - Kaybettin!")
else:
    print(f"🤝 Oyun bitti! Toplam puanın: {puan} - Berabere!")
print("="*40)

