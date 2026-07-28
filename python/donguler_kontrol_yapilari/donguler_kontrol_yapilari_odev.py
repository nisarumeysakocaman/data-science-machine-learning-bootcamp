
#---------------------------------------------
#SORU 1 (IF)
#Kullanıcıdan bir sayı alın.
#Sayı pozitifse "Pozitif", negatifse "Negatif", sıfırsa "Sıfır" yazdırın.
#---------------------------------------------

print("-----1.Sorunun Çözümü-----")
sayi=int(input("Lutfen bir sayi giriniz: "))
if sayi > 0:
    print(f"girdiginiz sayi pozitif: {sayi}")
elif sayi < 0:
    print(f"girdiginiz sayi negatif: {sayi}")
else:
    print(f"girdiginiz sayi sifir: {sayi}")    

print("-"*50)


#---------------------------------------------
#SORU 2 (FOR)
#1'den 10'a kadar (10 dahil) sayıları yazdırın.
#Ayrıca bu sayıların toplamını hesaplayıp ekrana yazdırın.
#---------------------------------------------

print("-----2.Sorunun Çözümü-----")
toplam=0
for sayi in range(1,11):
    print(sayi)
    toplam+=sayi
print(f"Sayilarin toplami: {toplam}")   

print("-"*50)

#---------------------------------------------
# SORU 3 (WHILE)
# Kullanıcıdan "q" yazana kadar sürekli giriş alın.
# Kullanıcı her giriş yaptığında "Girdiniz: ..." şeklinde ekrana yazdırın.
# Kullanıcı "q" yazarsa döngü bitsin ve "Çıkış yapıldı" yazsın.
#---------------------------------------------

print("-----3.Sorunun Çözümü-----")
yazi=""
while yazi != "q":
    yazi=input("Bir sey yazin(cikmak icin q'ya basin): ")
    if yazi!="q":
        print(f"Girdiniz: {yazi} ")
print("Cikis Yapildi")

print("-"*50)

#---------------------------------------------
# SORU 4 (NESTED)
# 1'den 20'ye kadar sayıları dolaşın.
# Eğer sayı çiftse "Çift", tekse "Tek" yazdırın.
# Ayrıca sayı 10'dan büyükse yanına "Büyük", değilse "Küçük/Eşit" yazdırın.
# Örnek çıktı: 12 -> Çift Büyük
#---------------------------------------------

print("-----4.Sorunun Çözümü-----")
for i in range(1,21):
    if i%2==1:
        if i>10:
            print(f"{i} -> Tek Buyuk")
        else:
            print(f"{i} -> Tek Kuçuk")
        
    else:
        if i>10:
            print(f"{i} -> Cift Buyuk")
        else:
            print(f"{i} -> Cift Kucuk")


print("-"*50)

