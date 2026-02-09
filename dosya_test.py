dosya = open("veriler.txt","w") 
dosya.write ("Merhaba Dünya!\n")
dosya.write("İkinci satır \n")
dosya.close()

print("Dosyaya yazıldı!")



dosya = open("veriler.txt", "a")
dosya.write("Üçüncü satır\n")
dosya.close()

dosya=open("veriler.txt", "r")
icerik=dosya.read()
dosya.close()

print("Dosyadan okunan:")
print(icerik)
