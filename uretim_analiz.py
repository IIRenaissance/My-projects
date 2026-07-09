import sqlite3

print("╔══════════════════════════════╗")
print("║  ÜRETİM ANALİZ SİSTEMİ       ║")
print("╚══════════════════════════════╝")

conn = sqlite3.connect("uretim.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS uretim (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    urun_adi TEXT NOT NULL,
    uretim_miktari INTEGER NOT NULL,
    hatali_urun INTEGER NOT NULL,
    tarih TEXT NOT NULL
)
""")
conn.commit()
print("✓ Veritabanı hazır!")

# Eski verileri temizle (temiz başlangıç için)
cursor.execute("DELETE FROM uretim")
conn.commit()


def uretim_ekle():
    urun = input("Ürün adı: ")
    miktar = int(input("Üretim Miktarı: "))
    hatali = int(input("Hatalı ürün sayısı: "))
    tarih = input("Tarih (YYYY-MM-DD): ")
    cursor.execute("""
        INSERT INTO uretim (urun_adi, uretim_miktari, hatali_urun, tarih)
        VALUES (?, ?, ?, ?)
    """, (urun, miktar, hatali, tarih))
    conn.commit()
    print(f"✓ '{urun}' üretimi kaydedildi.")


def uretim_listele():
    cursor.execute("SELECT * FROM uretim")
    kayitlar = cursor.fetchall()
    if len(kayitlar) == 0:
        print("Henüz kayıt yok.")
    else:
        print("\n=== ÜRETİM KAYITLARI ===")
        for kayit in kayitlar:
            print(f"ID: {kayit[0]} | Ürün:{kayit[1]} | Üretim:{kayit[2]} | Hatalı:{kayit[3]} | Tarih:{kayit[4]}")


def urune_gore_toplam():
    cursor.execute("""
        SELECT urun_adi, SUM(uretim_miktari) as toplam_uretim
        FROM uretim
        GROUP BY urun_adi
        ORDER BY toplam_uretim DESC
    """)
    sonuc = cursor.fetchall()
    print("\n=== ÜRÜNE GÖRE TOPLAM ÜRETİM ===")
    for satir in sonuc:
        print(f"{satir[0]}: {satir[1]} adet")


def yuksek_hatali_urunler():
    cursor.execute("""
        SELECT urun_adi, SUM(hatali_urun) as toplam_hata
        FROM uretim
        GROUP BY urun_adi
        HAVING toplam_hata > 20
        ORDER BY toplam_hata DESC
    """)
    sonuc = cursor.fetchall()
    print("\n=== HATA SAYISI 20'DEN FAZLA OLAN ÜRÜNLER ===")
    if len(sonuc) == 0:
        print("Böyle bir ürün yok.")
    else:
        for satir in sonuc:
            print(f"{satir[0]}: {satir[1]} hatalı ürün")


def ortalama_alti_uretim():
    cursor.execute("""
        SELECT urun_adi, uretim_miktari, tarih
        FROM uretim
        WHERE uretim_miktari < (SELECT AVG(uretim_miktari) FROM uretim)
        ORDER BY uretim_miktari ASC
    """)
    sonuc = cursor.fetchall()
    print("\n=== ORTALAMANIN ALTINDA ÜRETİM YAPILAN GÜNLER ===")
    for satir in sonuc:
        print(f"{satir[0]} - {satir[1]} adet ({satir[2]})")



while True:
    print("\n╔══════════════════════════════╗")
    print("║           MENÜ                ║")
    print("╚══════════════════════════════╝")
    print("1 - Üretim kaydı ekle")
    print("2 - Tüm kayıtları listele")
    print("3 - Ürüne göre toplam üretim")
    print("4 - Hata oranı yüksek ürünler")
    print("5 - Ortalamanın altındaki üretimler")
    print("6 - Çıkış")

    secim= input("\nSeçiminiz: ")

    if secim=="1":
        uretim_ekle()
    elif secim=="2":
        uretim_listele()
    elif secim=="3":
        urune_gore_toplam()
    elif secim == "4":
        yuksek_hatali_urunler()
    elif secim=="5":
        ortalama_alti_uretim()
    elif secim=="6":
        print("\nGörüşürüz!")
        conn.close()
        break
    else:
        print("Geçersiz seçim, tekrar dene.")




