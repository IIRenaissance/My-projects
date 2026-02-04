import random
max_sayi=100
tahmin_hakki=7


print("=== Zorluk Seviyesi Seç ===")
print("1. Kolay (1-50, 10 hak)")
print("2. Orta (1-100, 7 hak)")
print("3. Zor (1-500, 5 hak)")

zorluk=(input("Seçim yap (1/2/3):"))

if zorluk=="1":
    max_sayi=50
    tahmin_hakki=10

elif zorluk =="2":
    max_sayi=100
    tahmin_hakki=7
elif zorluk=="3":
    max_sayi=500
    tahmin_hakki=5
else:
    print("Yanlış seçim orta seviye başlatılıyor")

sayi=random.randint(1, max_sayi)

print(f"1-{max_sayi} arası sayı tuttum, tahmin et!")

while tahmin_hakki>0:
    tahmin=int(input("Tahminin: "))
    if tahmin ==sayi:
        print("Tebrikler kazandın!")
        break
    elif tahmin < sayi:
        print("Daha büyük söyle")
    else:
        print("Daha küçük söyle")
    
    tahmin_hakki -=1
    print(f"kalan hak: {tahmin_hakki}")

if tahmin_hakki ==0:
    print(f"kaybettin hakkın bitti! Sayı {sayi} idi.")

