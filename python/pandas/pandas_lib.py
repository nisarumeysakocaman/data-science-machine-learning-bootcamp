"""
Pandas: veri bilimi kütüphanesi
    tablo şeklinde veri oluşturmak
    verileri düzenlemek, filtrelemek
    sütun ve satır işlemleri yapmak
    dosyalardan veri okumak

Pandas Numpy ilişkisi:
    numpy: say sal dizi sağlar
    pandas: tablo veri yapıları

Pandas Nerelerde Kullanılır?
    veri analizi
    veri düzenleme
    veri temizleme
    veri işleme
    veri dosyalarını okuma

Pandas ile ilgili neler öğreneceğiz?
    Series
    dataframe
    veri okuma ve yazma
    veri seçmce ve filtreleme
    satır ve sütun işlemleri
    veri sıralama ve gruplama
    temel pandas fonksiyonları
 """

import pandas as pd

#series oluşturma
veri=pd.Series([10,20,30,40])
print(veri)
"""
0    10
1    20
2    30
3    40
dtype: int64
"""
#series içindeki verilere erişme
veri=pd.Series([1,2,3,4,5,6,7])
print(veri[0]) #1
print(veri[5]) #6

#series için özel index belirleme
veri=pd.Series([10,20,30,40], index=["a","b","c","d"])
print(veri)
"""
a    10
b    20
c    30
d    40
dtype: int64
"""

print(veri["b"]) #20


#dictionary ile series oluşturma

veri={
    "ali": 45,
    "nisa": 75,
    "melek": 90
}

s=pd.Series(veri)
print(s)
"""
ali      45
nisa     75
melek    90
dtype: int64
"""

#series özellikleri
print(s.index)   #Index(['ali', 'nisa', 'melek'], dtype='str')
print(s.values)  #[45 75 90]
print(s.dtype)   #int64

#series ile matematiksel işlemler
veri=pd.Series([10,20,30])
sonuc=veri*2
print(sonuc)
"""
0    20
1    40
2    60
dtype: int64
"""

#series filtreleme
yas=pd.Series([10,20,39,40,50])
filtre=yas > 25 #boolean filtreleme
print(filtre)
"""
0    False
1    False
2     True
3     True
4     True
dtype: bool
"""

sonuc=yas[filtre]
print(sonuc)
"""
2    39
3    40
4    50
dtype: int64
"""

#dataframe oluşturma
veri={
    "isim": ["nisa","zeynep","mehmet"],
    "yas": [20,26,29],
    "sehir": ["Bursa","Bolu","Karaman"]

}

df=pd.DataFrame(veri)
print(df)
"""
     isim  yas    sehir
0    nisa   20    Bursa
1  zeynep   26     Bolu
2  mehmet   29  Karaman
"""

#sütun isimleri
print(df.columns) #Index(['isim', 'yas', 'sehir'], dtype='str')

#satır sayısını öğrenme
print(df.shape)  #(3, 3)

#sütunlara erişim
print(df["isim"])
"""
0      nisa
1    zeynep
2    mehmet
Name: isim, dtype: str
"""

#birden fazla sütuna erişim
print(df[["isim","yas"]])
"""
     isim  yas
0    nisa   20
1  zeynep   26
2  mehmet   29
"""

#yeni sütun ekleme
df["maas"]= [5000,4500,7800]
print(df)
"""
isim  yas    sehir  maas
0    nisa   20    Bursa  5000
1  zeynep   26     Bolu  4500
2  mehmet   29  Karaman  7800
"""

#sütun silme 
df=df.drop("sehir",axis=1)
print(df)
"""
 isim  yas  maas
0    nisa   20  5000
1  zeynep   26  4500
2  mehmet   29  7800
"""

#ilk satırları görüntülemek
print(df.head()) #ilk 5 satırı görüntüler
"""
 isim  yas  maas
0    nisa   20  5000
1  zeynep   26  4500
2  mehmet   29  7800
"""

#son satırları görüntülemek
print(df.tail()) #son 5 satırı görüntüler
"""
  isim  yas  maas
0    nisa   20  5000
1  zeynep   26  4500
2  mehmet   29  7800
"""

#dataframe hakkında bilgi alma
print(df.info())
"""
<class 'pandas.DataFrame'>
RangeIndex: 3 entries, 0 to 2
Data columns (total 4 columns):
 #   Column  Non-Null Count  Dtype
---  ------  --------------  -----
 0   isim    3 non-null      str  
 1   yas     3 non-null      int64
 2   sehir   3 non-null      str  
 3   maas    3 non-null      int64
dtypes: int64(2), str(2)
memory usage: 228.0 bytes
"""

"""Dosya okuma ve yazma"""
# csv (comma seperated values) dosyası okuma
df=pd.read_csv("veri.csv")
print(df)
"""
     isim   yas     sehir
0    nisa    22    Mersin
1     ali    56     Konya
2  zeynep    34   Trabzon
"""

#excel okuma
df=pd.read_excel("veri_excel.xlsx")
print(df)
"""
     isim  yas    sehir
0    nisa   22   Edirne
1  mehmet   56    Bursa
2  meryem   23  Karaman
"""

#csv dosyası yazma
veri={
    "isim":["nisa","hasan","kader"],
    "yas":[22,99,23],
    "sehir":["erzincan","hakkari","kilis"]
}

df=pd.DataFrame(veri)

df.to_csv("new_data.csv",index=False)

df.to_excel("new_data.xlsx",index=False)


"""veri seçme ve filtreleme"""
#örnek dataframe oluştur
veri={
    "isim":["nisa","ali","gamze","mehmet"],
    "yas":[22,34,56,33],
    "sehir":["Ankara","Ankara","Edirne","Siirt"],
    "maas":[3000,5600,7790,1200]
}

df=pd.DataFrame(veri)
print(df)
"""
isim  yas   sehir  maas
0    nisa   22  Ankara  3000
1     ali   34  Ankara  5600
2   gamze   56  Edirne  7790
3  mehmet   33   Siirt  1200
"""

#sütun seçme
print(df["isim"])
"""
0      nisa
1       ali
2     gamze
3    mehmet
"""

#birden fazla sütun seçme
print(df[["isim","yas"]])
"""
 isim  yas
0    nisa   22
1     ali   34
2   gamze   56
3  mehmet   33
"""

#satır seçme -> iloc
print(df.iloc[0]) #0.satırı yazdırır ,satır ve sıra numrasına göre seçim için iloc kullanılır
"""
isim       nisa
yas          22
sehir    Ankara
maas       3000
Name: 0, dtype: object
"""

#birden fazla satır seçme
print(df.iloc[0:3]) #burada 3 dahil değil
"""
 isim  yas   sehir  maas
0   nisa   22  Ankara  3000
1    ali   34  Ankara  5600
2  gamze   56  Edirne  7790
"""

#satır seçme -> loc
print(df.loc[2]) #indexi 2 olan satırı yazdırır ,etiketlerine göre seçim için loc kullanılır
"""
isim      gamze
yas          56
sehir    Edirne
maas       7790
Name: 2, dtype: object
"""

#belirli bir satır ve belirli bir sütun seçerek yazdırma
print(df.loc[:, ["isim","maas"]]) #tüm satırlar ve adı isim ve maas olan tüm sütunları yazdırır
"""
     isim  maas
0    nisa  3000
1     ali  5600
2   gamze  7790
3  mehmet  1200
"""

print(df.loc[:2, ["isim","maas"]]) #loc'ta 'e kadar kısmı da dahildir yani burada 2 de dahil edilir
"""
 isim  maas
0   nisa  3000
1    ali  5600
2  gamze  7790
"""

#koşullu filtreleme
filtre=df["yas"] > 40
print(filtre)
"""
0    False
1    False
2     True
3    False
"""

print(df[df["yas"] > 40])
"""
 isim  yas   sehir  maas
2  gamze   56  Edirne  7790
"""

#birden fazla koşul varsa
#şehir Ankara ve maaşı 5000'den fazla olan insanları getir
sonuc=df[ (df["sehir"]=="Ankara") & (df["maas"] > 5000) ]
print(sonuc)
"""
  isim  yas   sehir  maas
1  ali   34  Ankara  5600
"""

#belirli bir değeri içeren satırlar
print(df[ df["sehir"]=="Ankara"])
"""
  isim  yas   sehir  maas
0  nisa   22  Ankara  3000
1   ali   34  Ankara  5600
"""

#sadece belirli sütunları gösterme
#yaşı 25'ten büyük olanların sadece isim ve maaşını yazdırma
print(df[ df["yas"] > 25][["isim","maas"]])
"""
     isim  maas
1     ali  5600
2   gamze  7790
3  mehmet  1200
"""


"""sütun ve satır işlemleri"""
#dataframe oluşturma
veri={
    "isim":["melih","ezgi","ceren","alper"],
    "yas":[12,43,70,32],
    "sehir":["Adana","Antalya","Edirne","Denizli"]
}

df=pd.DataFrame(veri)
print(df)
"""
    isim  yas    sehir
0  melih   12    Adana
1   ezgi   43  Antalya
2  ceren   70   Edirne
3  alper   32  Denizli
"""

#yeni bir sütun ekleme
df["maas"]=[3400,5600,3800,9000]
print(df)
"""
    isim  yas    sehir  maas
0  melih   12    Adana  3400
1   ezgi   43  Antalya  5600
2  ceren   70   Edirne  3800
3  alper   32  Denizli  9000
"""

#hesaplama ile yeni bir sütun oluşturma
df["yillik_maas"]=df["maas"]*12
print(df)
"""
    isim  yas    sehir  maas  yillik_maas
0  melih   12    Adana  3400        40800
1   ezgi   43  Antalya  5600        67200
2  ceren   70   Edirne  3800        45600
3  alper   32  Denizli  9000       108000
"""

#sütun silme
df=df.drop("maas", axis=1 )
print(df)
"""
    isim  yas    sehir  yillik_maas
0  melih   12    Adana        40800
1   ezgi   43  Antalya        67200
2  ceren   70   Edirne        45600
3  alper   32  Denizli       108000
"""

#sütun ismi değiştirme
df=df.rename(columns={"yillik_maas": "Yillik_maas"})
print(df)
"""
    isim  yas    sehir  Yillik_maas
0  melih   12    Adana        40800
1   ezgi   43  Antalya        67200
2  ceren   70   Edirne        45600
3  alper   32  Denizli       108000
"""

#yeni satır ekleme
df.loc[3]=["Hamit",34,"Kocaeli",7900] # buradaki 3 index numarasıdır
print(df)
"""
    isim  yas    sehir  Yillik_maas
0  melih   12    Adana        40800
1   ezgi   43  Antalya        67200
2  ceren   70   Edirne        45600
3  Hamit   34  Kocaeli         7900
"""
#satır silme
df=df.drop(0) #satır numarası 0 olan satır silinir, index numaraları güncellenmez 
print(df)
"""
  isim  yas    sehir  Yillik_maas
1   ezgi   43  Antalya        67200
2  ceren   70   Edirne        45600
3  Hamit   34  Kocaeli         7900
"""

#index değerlerini yeniden düzenleme
df=df.reset_index(drop=True)
print(df)
"""
    isim  yas    sehir  Yillik_maas
0   ezgi   43  Antalya        67200
1  ceren   70   Edirne        45600
2  Hamit   34  Kocaeli         7900
"""


"""veri sıralama ve gruplama"""
#dataframe oluşturma
veri={
    "isim":["nisa","ali","ekin","beyza","mehmet"],
    "sehir":["Ankara","Adana","Ankara","Afyon","Afyon"],
    "maas":[4500,6700,8200,7600,5900]
}

df=pd.DataFrame(veri)
print(df)
"""
     isim   sehir  maas
0    nisa  Ankara  4500
1     ali   Adana  6700
2    ekin  Ankara  8200
3   beyza   Afyon  7600
4  mehmet   Afyon  5900
"""

#veri sıralama
df_sirali=df.sort_values("maas")
print(df_sirali)
"""
     isim   sehir  maas
0    nisa  Ankara  4500
4  mehmet   Afyon  5900
1     ali   Adana  6700
3   beyza   Afyon  7600
2    ekin  Ankara  8200
"""

#azalan sıralama
df_sirali=df.sort_values("maas", ascending=False)
print(df_sirali)
"""
     isim   sehir  maas
2    ekin  Ankara  8200
3   beyza   Afyon  7600
1     ali   Adana  6700
4  mehmet   Afyon  5900
0    nisa  Ankara  4500
"""

#birden fazla sütuna göre sıralama
df_sirali=df.sort_values(["sehir","maas"]) #önce şehir sonra maaş sıralaması yapar
print(df_sirali)
"""
     isim   sehir  maas
1     ali   Adana  6700
4  mehmet   Afyon  5900
3   beyza   Afyon  7600
0    nisa  Ankara  4500
2    ekin  Ankara  8200
"""
#veri gruplama -> groupby
#şehir bazında gruplama
gruplar=df.groupby("sehir")
print(gruplar) #<pandas.api.typing.DataFrameGroupBy object at 0x00000187E2C5FB60>


#grupların ortalama maaşı
sonuc=df.groupby("sehir")["maas"].mean() #şehir bazında ortlama maaş hesaplama
print(sonuc) 
"""
sehir
Adana     6700.0
Afyon     6750.0
Ankara    6350.0
Name: maas, dtype: float64
"""

#grupların toplam maaşı
sonuc=df.groupby("sehir")["maas"].sum() #şehir bazında toplam maaş hesaplama
print(sonuc)
"""
sehir
Adana      6700
Afyon     13500
Ankara    12700
Name: maas, dtype: int64
"""

#grupların kaç kişi olduğunu bulma
sonuc=df.groupby("sehir")["isim"].count() 
print(sonuc)
"""
sehir
Adana     1
Afyon     2
Ankara    2
Name: isim, dtype: int64
"""

#birden fazla işlem yapma
sonuc=df.groupby("sehir")["maas"].agg(["mean","max","min"])
print(sonuc)
"""
          mean   max   min
sehir                     
Adana   6700.0  6700  6700
Afyon   6750.0  7600  5900
Ankara  6350.0  8200  4500
"""

"""temel pandas fonksiyonları"""
#dataframe oluşturma
veri={
    "isim":["nisa","ali","ekin","beyza","mehmet"],
    "yas":[24,65,78,23,11],
    "sehir":["Ankara","Adana","Ankara","Afyon","Afyon"],
    "maas":[4500,6700,8200,7600,5900]
}

df=pd.DataFrame(veri)
print(df)
"""
     isim  yas   sehir  maas
0    nisa   24  Ankara  4500
1     ali   65   Adana  6700
2    ekin   78  Ankara  8200
3   beyza   23   Afyon  7600
4  mehmet   11   Afyon  5900
"""

#ilk satırları görüntüleme -> head
print(df.head(3)) #3 yazdığım için ilk 3 satırı gösterecek eğer hiçbir şey yazmazsak ,head(), ilk 5 satırı gösterir
"""
   isim  yas   sehir  maas
0  nisa   24  Ankara  4500
1   ali   65   Adana  6700
2  ekin   78  Ankara  8200
"""

#son satırları görüntüleme -> tail
print(df.tail(4)) #son 4 satırı gösterecek hiçbir şey yazmazsak son 5 satırı gösterir
"""
     isim  yas   sehir  maas
1     ali   65   Adana  6700
2    ekin   78  Ankara  8200
3   beyza   23   Afyon  7600
4  mehmet   11   Afyon  5900
"""

#info
print(df.info())
"""
<class 'pandas.DataFrame'>
RangeIndex: 5 entries, 0 to 4
Data columns (total 4 columns):
 #   Column  Non-Null Count  Dtype
---  ------  --------------  -----
 0   isim    5 non-null      str  
 1   yas     5 non-null      int64
 2   sehir   5 non-null      str  
 3   maas    5 non-null      int64
dtypes: int64(2), str(2)
memory usage: 292.0 bytes
"""

#sayısal sütunların temel istatistiklerini görmek için -> describe()
print(df.describe())
"""
             yas         maas
count   5.000000     5.000000
mean   40.200000  6580.000000
std    29.388773  1454.991409
min    11.000000  4500.000000
25%    23.000000  5900.000000
50%    24.000000  6700.000000
75%    65.000000  7600.000000
max    78.000000  8200.000000
"""

#bir sütundaki değerlerin kaç kez tekrar ettiğini yazdırma -> value_counts()
print(df["sehir"].value_counts())
"""
sehir
Ankara    2
Afyon     2
Adana     1
Name: count, dtype: int64
"""
#bir sütundaki benzersiz değerleri görmek -> unique()
print(df["sehir"].unique()) 
"""
['Ankara', 'Adana', 'Afyon']
Length: 3, dtype: str
"""

#bir sütunda kaç farklı değer olduğunu görmek -> nuunique()
print(df["sehir"].nunique()) #3

