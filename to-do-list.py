

print("===GÖREV LİSTESİ===")

gorevler=[]

print("Görev sayısı:", len(gorevler))

yeni_gorev= input("Görev gir:")
gorevler.append(yeni_gorev)

print("Görev eklendl!")
print("Toplam görev:", len(gorevler))


print("\n---Görevlerim---")
for gorev in gorevler:
    print("-" + gorev)
while True:
    print("\n===MENÜ===")
    print("1. Görev ekle")
    print("2. Görevleri listele")
    print("3. Çıkış")

    secim=input("Seçiminiz (1/2/3): ")


    if secim =="1":
        yeni_gorev=input("Görev giriniz:")
        gorevler.append(yeni_gorev)
        print("Görev eklendi!")

    elif secim=="2":
        print("\n ---Görevlerim---")
        if len(gorevler)==0:
            print("Henüz görev yok!")
        else:
            for i in range(len(gorevler)):
                print(f"{i+1}. {gorevler[i]}")

    elif secim =="3":
        print("Çıkış seçildi. Görüşürüz!")
        break

    else:
        print("Geçersiz seçim! 1,2 veya 3 girin.")



