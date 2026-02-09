meyveler=[]
print("Başta:",meyveler)

meyveler.append("Elma")
print("Ekledikten sonra:", meyveler)

meyveler.append("Armut")
meyveler.append("Muz")
print("3 ekleme sonrası:",meyveler)
print("Kaç meyve var?", len(meyveler))


print("\n---Tüm meyveler---")
for meyve in meyveler:
    print("-"+ meyve)

print("\n ---Numaralı Liste---")
for i in range(len(meyveler)):
    print(f"{i+1}. {meyveler[i]}")

meyveler.remove("Armut")
print("Armut silindikten sonra:", meyveler)





"""
gorevler=[]

gorevler = ["Alısveriş yap","Ders çalış", "Spor yap"]

"""