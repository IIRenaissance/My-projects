import random 
sayi=random.randint(1,100)
tahmin_hakki=7

print("1-100 arası sayı tuttum, tahmin et")

while tahmin_hakki>0:
    tahmin= int(input("Tahminin: "))

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
    