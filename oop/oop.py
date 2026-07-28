"""
Class Nedir?
    bir nesnenin (object) nasıl olacağını tanımlayan bir şablondur.
    - class bir taslak yada plan gibidir
    öğrenci:
    isim, yaş, bmlüm
    ders calışmak, sınava girmek
Class tanımlama:
    class Ogrenci:
    pass
    Ogrenci > class ismi
Class neden kullanırız?
    kodun daha düzenli olması için
    kod tekrarını azaltır
    büyük projelerde yönetimi kolaylastirir
    scikit learn -> en önemli machine learning kütüphanesi -> L CarRegression() class tanımlamış olur
Neler Öğreneceğiz?
    _init_ metodu (initializer) :nesne oluşturulduğunda otomatik olarak oluşan özel (kurucu) bir metottur
    attribute ve method
    object oluşturma
    Mini proje  """

""" Ogrenci class
    -isim
    -yaş
    """

class Ogrenci:
    def __init__(self,isim,yas): # self -> oluşturulan nesneyi temsil eder ,isim ve yaş ise parametrelerdir
        print(f"yeni bir öğrenci oluşturuluyor... isim: {isim} yaş: {yas}")


#object (nesne) oluşturma
Ogrenci1=Ogrenci("nisa",22)

"""Attribute bir class a veya nesneye ait özellikleri temsil eden değişkenlerdir. yani bir nesnenin verilerini tutan yapılardır
Öğrenci:
isim, yaş ve bölüm: bunlar öğrencinin attribute larıdır."""

class Ogrenci:
    def __init__(self,isim,yas):
        self.isim=isim #isim attribute
        self.yas=yas #yas attribute

#attribute kullanımı
ogrenci1=Ogrenci("nisa",22)

#ogrenci1'in attribute'larına erişim
print(ogrenci1.isim) #nisa
print(ogrenci1.yas)  #22


"""Metot (method): bir class içerisinde tanımlanan fonksiyonlardır
bir nesnenin yapabileceği işlemleri temsil ederler"""


class Ogrenci:
    def __init__(self,isim,yas):
        self.isim=isim
        self.yas=yas,

    def tanit(self):
        print(f"merhaba benim adım: {self.isim}")


ogrenci1=Ogrenci("nisa",22)
ogrenci2=Ogrenci("ahmet",56)

ogrenci1.tanit()

ogrenci2.tanit()


"""object oluşturma ve class kullanımı
        class: şablon->araba
        object:şablondan oluşturulan yapı->mercedes
"""
class Kitap:
    def __init__(self,ad,yazar,sayfa):
        self.ad=ad
        self.yazar=yazar
        self.sayfa=sayfa

    def bilgi_goster(self):
        print(f"Kitap Adı: {self.ad}")
        print(f"Yazar: {self.yazar}")
        print(f"Sayfa Sayısı: {self.sayfa}")

#object oluşturma
kitap1=Kitap("Zorba","Nikos Kazancakis",379)

#method
kitap1.bilgi_goster()
"""
Kitap Adı: Zorba
Yazar: Nikos Kazancakis
Sayfa Sayısı: 379
"""

#birden fazla obje oluşturma
kitap2=Kitap("Veronika Ölmek İstiyor","Paulo Coelho",215)
kitap3=Kitap("Kızıl Veba","Jack London",88)

print(kitap2.ad) #Veronika Ölmek İstiyor

kitap3.bilgi_goster()
"""
Kitap Adı: Kızıl Veba
Yazar: Jack London
Sayfa Sayısı: 88
"""