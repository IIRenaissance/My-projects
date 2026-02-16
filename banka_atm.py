import sqlite3

print("╔═══════════════════════╗")
print("║   ATM SİMÜLATÖRÜ      ║")
print("║      (SQL VERSİYON)   ║")
print("╚═══════════════════════╝")

conn=sqlite3.connect("atm.db")
cursor=conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS hesap(
    id INTEGER PRIMARY KEY,
    bakiye INTEGER
)              
""")

cursor.execute("SELECT COUNT(*) FROM hesap")

if cursor.fetchone()[0]==0:
    cursor.execute("INSERT INTO hesap (id,bakiye) VALUES (1,1000)")
    conn.commit()
    print("✓ Yeni hesap oluşturuldu. Bakiye: 1000 TL")

else:
    cursor.execute("SELECT bakiye FROM hesap WHERE id=1")
    bakiye= cursor.fetchone()[0]
    print(f"✓ Hesap yüklendi. Bakiye: {bakiye} TL")

dogru_sifre = "1234"
giris_hakki = 3

while giris_hakki > 0:
    sifre=input("\nŞifrenizi girin:")

    if sifre== dogru_sifre:
        print("✓ Giriş başarılı!\n")
        break

    else:
        giris_hakki-=1
        if giris_hakki > 0 :
            print(f"❌ Yanlış şifre! Kalan hak: {giris_hakki}")
        else:
            print("❌ Giriş hakkınız bitti!")
            conn.close()
            exit()

while True:
    cursor.execute("SELECT bakiye FROM hesap WHERE id =1")
    bakiye=cursor.fetchone()[0]

    print("\n=====MENÜ=====") 
    print("1-Bakiye görüntüle")
    print("2-Para yatır")
    print("3-Para çek")
    print("4-Çıkış")

    secim = input("Seçiminiz (1/2/3/4): ")
    
    if secim == "1":
        print(f"\nToplam bakiye: {bakiye} TL")
        
    elif secim == "2":
        miktar = int(input("Yatırılacak miktar: "))
        yeni_bakiye = bakiye + miktar
        
        cursor.execute("UPDATE hesap SET bakiye = ? WHERE id = 1", (yeni_bakiye,))
        conn.commit()
        
        print(f"✓ {miktar} TL yatırıldı!")
        print(f"Yeni bakiye: {yeni_bakiye} TL")
    
    elif secim == "3":
        miktar = int(input("Çekilecek miktar: "))
        
        if miktar > bakiye:
            print("❌ Yetersiz bakiye!")
            print(f"Mevcut bakiye: {bakiye} TL")
        else:
            yeni_bakiye = bakiye - miktar
            
            cursor.execute("UPDATE hesap SET bakiye = ? WHERE id = 1", (yeni_bakiye,))
            conn.commit()
            
            print(f"✓ {miktar} TL çekildi!")
            print(f"Kalan bakiye: {yeni_bakiye} TL")
            
    elif secim == "4":
        print("\nGörüşürüz!")
        break  
        
    else:
        print("❌ Geçersiz seçim!")

conn.close()


