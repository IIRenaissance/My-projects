dogru_sifre = "1234"
giris_hakki = 3

while giris_hakki >0:
    sifre=input("Şifrenizi girin:")

    if sifre == dogru_sifre:
        print("✓ Giriş başarılı!\n")
        break
    else:
        giris_hakki -=1
        if giris_hakki >0:
            print(f" Yanlış şifre! Kalan hak {giris_hakki}")
        else:
            print("❌ Giriş hakkınız bitti! Program sonlandırılıyor.")
            exit()


print("╔═══════════════════════╗")
print("║   ATM SİMÜLATÖRÜ      ║")
print("╚═══════════════════════╝")

try:
    dosya=open("bakiye.txt", "r")
    bakiye= int(dosya.read())
    dosya.close()
    print(f"Hesap yüklendi. Bakiye: {bakiye} TL")
except:
    bakiye= 1000
    print(f" Yeni hesap oluşturuldı. Toplam bakiye: {bakiye} TL" )

while True:
    print("=====MENÜ=====")
    print("1-Bakiye görüntüle")
    print("2-Para yatır")
    print("3-Para Çek")
    print("4-Çıkış")

    
    secim = input("Hangi işlemi yapmak istersiniz? (1/2/3/4): ")

    if secim == "1":
        print(f"Toplam bakiye: {bakiye} TL")
    
    elif secim == "2":
        yeni_para = int(input("Para miktarı giriniz: "))
        bakiye = bakiye + yeni_para

        dosya=open("bakiye.txt", "w")
        dosya.write(str(bakiye))
        dosya.close()

        print(f"✓ {yeni_para} TL yatırıldı!")
        print(f"Yeni bakiye: {bakiye} TL")
    
    elif secim == "3":
        cekilecek_para = int(input("Çekmek istediğiniz para miktarını giriniz: "))
        
        if cekilecek_para > bakiye:
            print("❌ Yetersiz bakiye!")
            print(f"Mevcut bakiye: {bakiye} TL")
        else:
            bakiye = bakiye - cekilecek_para
           

            dosya=open("bakiye.txt", "w")
            dosya.write(str(bakiye))
            dosya.close()
            
            print(f"✓ {cekilecek_para} TL çekildi!")
            print(f"Kalan bakiye: {bakiye} TL")
    
    elif secim == "4":
        print("Çıkış yapılıyor... Görüşürüz!")
        break
    
    else:
        print("❌ Geçersiz seçim! Lütfen 1, 2, 3 veya 4 girin.")