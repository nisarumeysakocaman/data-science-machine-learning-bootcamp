#-------------------------------------------
# SORU 1
#"notlar.txt" adında bir dosya olusturun ve içine 5 öğrencinin notunu yazın.
# Her not ayrı satırda olsun.
#-------------------------------------------

print("-----1.Sorunun Çözümü-----")
with open("notlar.txt","w") as dosya:
    dosya.write("78\n")
    dosya.write("45\n")
    dosya.write("79\n")
    dosya.write("99\n")
    dosya.write("65\n")

print("-"*50)
#-------------------------------------------
#SORU 2
# Bu dosyayı okuyun ve:
# Notların ortalamasını hesaplayın
# En yüksek notu bulun
# En düşük notu bulun
#-------------------------------------------

print("-----2.Sorunun Çözümü-----")
with open("notlar.txt","r") as dosya:
    icerik=dosya.readlines()
    satir=float(len(icerik))
    toplam=0
    for i in icerik:
        sayi=int(i)
        toplam+=sayi
    ortalama=toplam/satir
    print(f"notlarin ortalamasi: {ortalama}")
    print(f"En yuksek not: {max(icerik)}")
    print(f"En dusuk not: {min(icerik)}")

#     notlar = []
# with open("notlar.txt", "r", encoding="utf-8") as dosya:
# for satir in dosya:
# notlar.append(int(satir.strip()))
# ortalama sum(notlar) / len(notlar)
# en_yuksek max(notlar)
# en_dusuk = min(notlar)
# print("Notlar:", notlar)
# print("Ortalama:", ortalama)
# print("En yüksek not:", en_yuksek)
# print("En düşük not:", en_dusuk)


print("-"*50)


#-------------------------------------------
# SORU 3
# Eğer ortalama 50'den büyükse "Sınıf geçti"
# değilse "Sınıf kaldı" sonucunu
# "sonuc.txt" dosyasına kaydedin.
#-------------------------------------------

print("-----3.Sorunun Çözümü-----")
with open("sonuc.txt","w",encoding="utf-8") as dosya:
    if ortalama > 50:
        dosya.write(f"Ortalama: {ortalama}\n---Sınıf geçti---")
    else:
        dosya.write(f"Ortalama: {ortalama}\n---Sınıf kaldı---")


print("-"*50)