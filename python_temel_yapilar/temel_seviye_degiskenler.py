"""
Değişken Kavramı: Veriyi saklamak için kullandığımız alan

--Değişken Adlandırma Kuralları---

    rakamla başlamaz : 1_var 
    boşluk içermez: nisa rümeysa
    özel karakter kullanılmaz : önemli_değişken 
    büyük küçük harf duyarlılığı vardır : degisken ile Degisken aynı değildir


    ---Derste Bahsedilecek Olan Konular---

        -integer,float,string
        -type fonksiyonu, veri tipi kontrolü ve tip dönüşümleri
        -listeler
            -indeksleme ve slicing
            -list metotları
        -tuple : Birden fazla veriyi saklayan bir veri yapısıdır, tuple değiştirilemez.Tuple tanımlarken ' () ' normal parantez kullanılır,index
        belirtirken ise ' [ ] ' köşeli parantez kullanılır
        
        -dictionary: verileri anahtar-değer  yani key-value mantığıyla saklar
        -set: unique elemanlardan oluşan bir veri yapısıdır. Aynı eleman birden fazla kez olamaz.
        -veri yapıları arasındaki farklar

        NOT: CTRL + Ö ile seçtiğimiz satırları yorum satırına çevirebiliriz ya da yorum satırıysa onu kaldırabiliriz.
        
        Listeler: Numpy array'in temelini oluşturur
        Tuple: Sabit veriler ve güvenli yapı içindir
        Dictionary: Pandas dataframe temelini oluşturur,anlamlı veri saklamak ve etkiketli veri tutmak için kullanılır
        Set: Tekrar eden değerleri temizlemek için ve küme işlemleri yapmak için kullanılır.


"""


"""integer: tam sayı"""

yas=35
sicaklik=-20
print(yas)
print(sicaklik)

#dört işlem
a=10
b=45
toplam=a+b
print(toplam)
carpma=a*b
print(carpma)
cikarma=a-b
print(cikarma)
bolme=a/b
print(bolme)


#örnek1: birim fiyat ile adet sayısı verilen ürünün toplam değerini hesaplama
birim_fiyat=60
adet=25
toplam_fiyat=birim_fiyat * adet
print(toplam_fiyat)

#örnek2: bir ürüne girilen değer yüzdesi kadar zam yapma
# urun_fiyat=70
# yuzde=int(input("Zam yüzdesini yazın: "))
# yeni_fiyat=urun_fiyat + urun_fiyat * yuzde/100
# print(yeni_fiyat)

""" float: ondalıklı sayılar not: nokta kullanarak yazmalıyız 3.14 gibi"""

pi=3.14
number=5.67

#dört işlem
print(pi+number)
print(pi-number)
print(pi*number)
print(pi/number)

#ondalık hassasiyeti sorunu için round fonksiyounu kullanırız
print(0.3-0.1) #sonuç 0.2 olmalı ama çıkan sonuç 0.19999999999999998
sonuc=0.3-0.1
yeni_sonuc=round(sonuc,2) # 2 virgülden sonra kaç basamak yazılacağını temsil eder
print(yeni_sonuc) #sonuç bu sefer 0.2 oldu

#örnek3: gelen fiyat üzerinden kdv (%20) hesaplama
# fiyat=float(input("Ürünün fiyatını giriniz: "))
# print(fiyat)
# kdvli_fiyat=fiyat + fiyat*(20/100)
# print(kdvli_fiyat)

"""string : karakter dizisi"""
#stringlerde hem tek tırnak ' hem de çift tırnak " kullanabiliriz.

isim="nisa"
isim2='rümeysa' 
bilgi= "nisa'nın diğer adı rümeysa"
#concatenation (string birleştirme)
print(bilgi)
bilgi2= isim +"'nın diğer adı" + " " + isim2
print(bilgi2)

#string ve sayı birleştirme
yil=1879
yil_to_str=str(yil) #1879 -> "1879"
ay="Mart"
gun=14
gun_to_str=str(gun) #14-> "14"
isim3="Albert Einstein"
bilgi3=isim3 + " " +  gun_to_str +  " " + ay + " " + yil_to_str + " tarihinde doğmuştur."
print(bilgi3)

kurulum_tarihi=2007
print("Karabük Üniversitesi " + str(kurulum_tarihi) + " yılında kurulmuştur.")
print(f"Karabük Üniversitesi {kurulum_tarihi} yılında kurulmuştur.") #f string

sayi3=100

print(f"Suyun kaynama sıcaklığı {sayi3} derecedir.")

#string indexleme
isim4="python"
print(isim4[0]) #p
print(isim4[3]) #h

#string metotları
metin="PythoN"
metin_lower_case=metin.lower() #metindeki harfleri küçük harfe çevirir
print(metin_lower_case)

#uzunluk bulma
metin2="klavye"
metin2_uzunluk=len(metin2)
print(metin2_uzunluk)

#yer değiştirme
metin3="bilgisayar"
print(metin3.replace('b','B')) #b harfi, B ile değiştirilecek


"""Veri Tipi ile İlgili İşlemler"""
#veri tipi kontorlü
x=10
print(type(x))  # <class 'int'>

x="10"
print(type(x))  # <class 'str'>

#print("25" + 10)   #can only concatenate str (not "int") to str

#casting (tip dönüşümleri)
# x="25"
# print(type(int(x))) #<class 'int'>
# print(type(float(x))) #<class 'float'>

# x=40
# print(type(str(x)))  #<class 'str'>

# sayi4=input("Bir sayi giriniz: ")
#print(type(sayi4)) #<class 'str'> NOT:input fonksiyonun çıktısı string olur.

#print(int("abc")) #invalid literal for int() with base 10: 'abc'

"""Listeler : birden fazla veriyi tek bir değişken içinde saklamamızı sağlar"""
sayilar=[0,1,2,3,4,5] #integer listesi
isimler=["nisa", "rümeysa" , "furkan" , "kader"] #string listesi
karisik=[1,"hello","world",3,"şeftali"] # farklı veri tiplerini aynı listede tutabiliriz.
print(karisik) #[1, 'hello', 'world', 3, 'şeftali']

#liste indeksleme
meyveler=["muz","ananas","limon"]
print(meyveler[0]) #muz
print(meyveler[2]) #limon 
print(meyveler[-1]) # -1 sondan 1. elemanı yazdırır yani limon

#liste uzunluğu
print(len(meyveler)) # 3 -> listenin toplam eleman sayısı

#listelerde slicing
sayilar=[10,20,30,40,50,60]
print(sayilar[1:4]) #[20, 30, 40]   [a,b] -> a dahil, b dahil değil -> bu aralıktaki tüm değerleri yazdırır.
print(sayilar[2:5]) #[30, 40, 50]
print(sayilar[:3]) # [10, 20, 30]  [:3] -> ilk elemandan 3 elemana kadar yazdırır
print(sayilar[1:]) # [20, 30, 40, 50, 60]  [1:] -> 1.indexteki elemandan son elemana kadar yazdırır. NOT:burada son elemanı da dahil ederiz.

#listeye eleman ekleme işlemleri
sayilar=[1,2,3,4]
sayilar.append(5) #elemanı listenin sonuna ekler
print(sayilar) #[1, 2, 3, 4, 5]

sayilar.insert(0,7) # 0. indexe 7 değerini ekler
print(sayilar) #[7, 1, 2, 3, 4, 5]

#listeden eleman silme işlemleri
sayilar.remove(4) #listedeki 4 değerini siler
print(sayilar) #[7, 1, 2, 3, 5]

sayilar.pop() #listedeki son elemanı siler
print(sayilar) #[7, 1, 2, 3]

sayilar.pop(3) # 3.indexteki elemanı siler
print(sayilar) #[7, 1, 2]

#bir indexteki değeri değiştirme
sayilar[2]=678
print(sayilar) #[7, 1, 678]


"""Tuple"""

koordinat=(15,76)
renkler=("kırmızı","yeşil","mavi")

#liste vs tuple
liste=[1,2,3,4]
liste[0]=99 # bu elemanı değiştirebilirim
print(liste)

t=(10,20,30)
#t[0]=45 #'tuple' object does not support item assignment 
print(t)

#indexleme
tup=(10,20,30)
print(tup[0]) #10
print(tup[-1]) #30

#slicing
tup=(1,2,3,4)
print(tup[1:3]) #(2, 3)

#tek elemanlı tuple 
tup=(5)
print(type(tup)) #<class 'int'>

tup=(5,)
print(type(tup)) #<class 'int'>

#tuple unpacking
koordinat=(10,40)
x,y=koordinat
print(x) #x=10
print(y) #y=40

#tuple metotları

t=(20,20,30,40)
print(t.count(20)) # 2 yani tuple'da kaç tane 20 değeri olduğunu döndürür.
print(t.index(30)) # 2 yani 30'un kaçıncı indexte olduğunu gösterir.



"""Dictionary"""

ogrenci= {   #key="isim" ,value="nisa"  {key:value}
    "isim":"nisa",
    "yas": 22,
    "bolum": "bilgisayar"

}
    
print(ogrenci) #{'isim': 'nisa', 'yas': 22, 'bolum': 'bilgisayar'}

#dictionary'e erişim
print(ogrenci["isim"]) #nisa
print(ogrenci["yas"]) #22

#dictionary'e yeni değer ekleme
ogrenci["not"]=99
print(ogrenci) #{'isim': 'nisa', 'yas': 22, 'bolum': 'bilgisayar', 'not': 99}

#dictionary değer güncelleme
ogrenci["isim"]="rümeysa"
print(ogrenci)  #{'isim': 'rümeysa', 'yas': 22, 'bolum': 'bilgisayar', 'not': 99}

#dictionary eleman silme
del ogrenci["bolum"]
print(ogrenci) #{'isim': 'rümeysa', 'yas': 22, 'not': 99}

#anahtarları ve değerleri alma
print(ogrenci.keys()) #dict_values(['rümeysa', 22, 99])
print(ogrenci.values()) #dict_values(['rümeysa', 22, 99])
print(ogrenci.items()) #dict_items([('isim', 'rümeysa'), ('yas', 22), ('not', 99)])


"""Set"""

sayilar={1,2,3,4}
print(sayilar) #{1, 2, 3, 4}

#tekrar eden elemanlar
sayilar={1,2,2,3,3,4,5}
print(sayilar) #{1, 2, 3, 4, 5}

#NOT: setler sırasızdır yani indexi yoktur.
# print(sayilar[2]) #'set' object is not subscriptable

#listeyi set'e çevirme
liste=[1,2,3,5,6,7,7]
sayilar=set(liste)
print(sayilar)  #{1, 2, 3, 5, 6, 7}

#set'e eleman ekleme
sayilar.add(8)
print(sayilar) #{1, 2, 3, 5, 6, 7, 8}

#setten eleman silme
sayilar.remove(3)
print(sayilar) #{1, 2, 5, 6, 7, 8}

#set işlemleri
a={1,2,3}
b={3,4,5}

print(a.union(b)) # a birleşim b -> {1, 2, 3, 4, 5}

print(a.intersection(b)) # a kesişim b -> {3}

print(a.difference(b)) # a fark b -> {1, 2}







