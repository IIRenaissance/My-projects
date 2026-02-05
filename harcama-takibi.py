print("===Harcama Takip===")

#eski veriler
try:
    dosya=open("harcamalar.txt", "r")
    satirlar = dosya.readlines()
    dosya.close()
    
    toplam = 0
    for satir in satirlar:
        toplam = toplam + int(satir)
    
    print(f"Önceki toplam harcama: {toplam} TL")

except:
    toplam = 0
    print(f"Toplam harcama: {toplam} Tl")

harcama=int(input("Harcama miktarı:"))
toplam= toplam + harcama
print(f"Toplam harcama : {toplam} TL")

#dosyaya kaydetme
dosya= open("harcamalar.txt","a")
dosya.write(f"{harcama} \n")
dosya.close()

devam = input("Başka harcama var mı? (e/h):")

while devam == "e":
    harcama=int(input("Harcama miktarı:"))
    toplam= toplam + harcama
    print(f"Toplam harcama : {toplam} TL")

    #dosya ekleme
    dosya = open("harcamalar.txt", "a")
    dosya.write(f"{harcama}\n")
    dosya.close()

    devam = input("Başka harcama var mı? (e/h):")

print("------------------------")
print(f"Toplam harcama: {toplam} Tl")