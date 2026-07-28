

"""Bozuk veri temizleme
veri:
        70
        85
        abc
        90
        50
        hata
        60

Amaç:
dosyayı oku
sayıya çevrilemeyen satırları atla
geçerli notları topla
ortalama hesapla """

notlar= []
hata_sayisi=0

with open("notlar.txt","r", encoding="utf-8") as dosya:

    for satir in dosya:

        try:
            not_degeri=int(satir.strip())
            notlar.append(not_degeri)
        except ValueError:
            print(f"Hatali veri bulundu: {satir.strip()}")
            hata_sayisi+=1


print(f"notlar: {notlar}")
print(f"hata sayisi: {hata_sayisi}")

ortalama=sum(notlar) / len(notlar)

print(f"ortalama: {ortalama}")
