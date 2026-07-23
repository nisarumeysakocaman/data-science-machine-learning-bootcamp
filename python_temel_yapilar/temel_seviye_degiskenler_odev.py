
#----------------------------------------------------
# SORU 1 
# Bir değişken tanımlayalım: ad="Kaan" , yas=25 , ortalama=3.45 
# Bu değişkenlerin tiplerini type() ile yazdıralım.
#----------------------------------------------------

ad="Kaan"
yas=25
ortalama=3.45

print("-------1.Sorunun Çözümü-------")
print(type(ad)) #<class 'str'>
print(type(yas)) #<class 'int'>
print(type(ortalama)) #<class 'float'>
print("-"*50)

#----------------------------------------------------
# SORU 2
# Kullanıcıdan yaş bilgisini input() ile alalım.
# Bu yaşın tipini ekrana basalım ve 5 yıl ekleyip sonucu yazdıralım.
# Not: input() her zaman string döndürür, int'e çevirmeyi unutmayalım.
#----------------------------------------------------

print("-------2.Sorunun Çözümü-------")
yas=input("Lutfen yasinizi giriniz: ")
print("Veri tipi : " , type(yas)) #Veri tipi :  <class 'str'>
yas_int=int(yas)
print("5 yıl sonraki yasiniz: " , yas_int+5 ) #5 yıl sonraki yasiniz:  17
print("-"*50)

#----------------------------------------------------
# SORU 3
# Bir ürün fiyatı (float) alalım. %18 KDV hesaplayalım
# Toplam fiyatı 2 basamak olacak şekilde yazdıralım
#----------------------------------------------------

print("-------3.Sorunun Çözümü-------")
fiyat=float(input("Lutfen urun fiyati giriniz: "))
kdv=fiyat * 0.18
yeni_fiyat=fiyat +kdv
print("KDV: " , round(kdv,2))
print("KDV'li urun fiyati: ", round(yeni_fiyat,2))
print("-"*50)

#----------------------------------------------------
# SORU 4
# Bir liste oluşturalım: sayilar [10, 20, 30, 40, 50]
# ilk elemanı yazdıralım
# Son elemanı yazdıralım
# 2. indexten sona kadar olan parçayı yazdıralım
# Listeye 60 ekleyelim
# Listedeki 20 değerini silelim
#----------------------------------------------------

print("-------4.Sorunun Çözümü-------")
liste=[10,20,30,40,50]
print(" liste: " , liste)
print("İlk eleman: " ,liste[0])
print("Son eleman:  " , liste[-1])
print("2.index ve sonrası: " , liste[2:])
liste.append(60)
print("listeye 60 elemanı eklendi: ",liste)
liste.remove(20)
print("listeden 20 elemanı silindi: " , liste)
print("-"*50)


#----------------------------------------------------
#SORU 5
# Bir tuple oluşturalım: koordinat (12, 34)
# Tuple icindeki değerleri unpacking ile x ve y değişkenlerine alalım
# x ve y'yi yazdıralım
# Tuple'ın değiştirilemediğini göstermek için (yorum satırıyla) örnek verelim
#----------------------------------------------------

print("-------5.Sorunun Çözümü-------")
koordinat=(12,34)
x,y=koordinat
print("x: " ,x)
print("y: " ,y)
#koordinat[0]=45 #'tuple' object does not support item assignment
print("-"*50)


#----------------------------------------------------
# SORU 6
# Bir sözlük (dictionary) oluşturalım:
# ogrenci = {"isim": "Ayşe", "yas": 22, "bolum": "Yazılım"}
#  Öğrencinin ismini yazdıralım
# "not" anahtarı ile 90 ekleyelim
# "yas" değerini 23 yaparak güncelleyelim
# Tüm anahtarları ve tüm değerleri yazdıralım
#----------------------------------------------------

print("-------6.Sorunun Çözümü-------")
ogrenci={"isim":"Nisa","yas":22,"bolum":"yazilim"}
print("Ad: " , ogrenci["isim"])
ogrenci["not"]=90
ogrenci["yas"]=23
print("Ogrenci Keys: " ,ogrenci.keys())
print("Ogrenci Values: " , ogrenci.values())
print("Ogrenci Bilgileri: " ,ogrenci.items())
print("-"*50)


#----------------------------------------------------
# SORU 7
# Set oluşturalım ve tekrar edenleri temizleyelim:
# liste ["Ali", "Ayse", "Ali", "Mehmet", "Ayşe"]
# listeyi set'e çevirip benzersiz isimleri yazdıralım
# benzersiz isim sayısını yazdıralım
#----------------------------------------------------

print("-------7.Sorunun Çözümü-------")
liste=["Ali","Ayse","Ali","Mehmet","Ayse"]
isimler=set(liste)
print("Benzersiz isimler: " ,isimler)
print("Benzersiz isim sayisi: " , len(isimler))
print("-"*50)
