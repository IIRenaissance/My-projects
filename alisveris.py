print("╔════════════════════════╗")
print("║  ALIŞ VERİŞ LİSTESİ    ║")
print("╚════════════════════════╝")

liste = []

while True:
    print("\n--- MENÜ ---")
    print("1 - Ürün ekle")
    print("2 - Listeyi göster")
    print("3 - Ürün sil")
    print("4 - Çıkış")
    
    secim = input("\nSeçiminiz (1/2/3/4): ")
    
    if secim == "1":
        urun = input("Ürün adı: ")
        liste.append(urun)
        print(f"✓ '{urun}' eklendi!")
        
    elif secim == "2":
        if len(liste) == 0:
            print("Liste boş!")
        else:
            print("\n=== ALIŞVERİŞ LİSTESİ ===")
            for i, urun in enumerate(liste, 1):
                print(f"{i}. {urun}")
                
    elif secim == "3":  
        if len(liste) == 0:
            print("Liste zaten boş!")
        else:
            print("\n=== LİSTENİZ ===")
            for i, urun in enumerate(liste, 1):
                print(f"{i}. {urun}")
            
            sira = int(input("Hangi sırayı silmek istersin? "))
            silinen = liste.pop(sira - 1)
            print(f"✓ '{silinen}' silindi!")
            
    elif secim == "4":
        print("\nGörüşürüz!")
        break
        
    else:
        print("❌ Geçersiz seçim!")