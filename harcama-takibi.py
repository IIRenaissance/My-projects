print("===Harcama Takip===")
toplam = 0
print(f"Toplam harcama: {toplam} Tl")

harcama=int(input("Harcama miktarı:"))
toplam= toplam + harcama
print(f"Toplam harcama : {toplam} TL")

devam = input("Başka harcama var mı? (e/h):")

while devam == "e":
    harcama=int(input("Harcama miktarı:"))
    toplam= toplam + harcama
    print(f"Toplam harcama : {toplam} TL")

    devam = input("Başka harcama var mı? (e/h):")

print("------------------------")
print(f"Toplam harcama: {toplam} Tl")