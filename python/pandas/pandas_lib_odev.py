# ÖRNEK VERİ SETİ
# Aşağıdaki veri seti tüm sorular için kullanılacaktır.
import pandas as pd

veri = {
"isim": ["Ali", "Ayşe", "Mehmet", "Zeynep", "Ahmet", "Elif"],
"yas": [25, 30, 28, 35, 22, 27],
"sehir": ["Ankara", "İstanbul", "Ankara", "İzmir", "Bursa", "İstanbul"],
"maas": [5000, 7000, 6000, 8000, 4500, 6500] }

df = pd.DataFrame (veri)
print("VERİ SETİ")
print(df)
print("-" * 50)


#-------------------------------------------
# SORU 1
# DataFrame'in ilk 3 satırını gösterin.
#-------------------------------------------
print("-----1.Sorunun Çözümü-----")
print(df.head(3))
"""
     isim  yas     sehir  maas
0     Ali   25    Ankara  5000
1    Ayşe   30  İstanbul  7000
2  Mehmet   28    Ankara  6000
"""
print("-" * 50)

#-------------------------------------------
# SORU 2
# DataFramedeki sütunların ismini ekrana yazdırın.
#-------------------------------------------
print("-----2.Sorunun Çözümü-----")
print(df.columns) #Index(['isim', 'yas', 'sehir', 'maas'], dtype='str')
print("-" * 50)

#-------------------------------------------
# SORU 3
# Sadece isim sütununu seçin.
#-------------------------------------------
print("-----3.Sorunun Çözümü-----")
print(df["isim"])
"""
0       Ali
1      Ayşe
2    Mehmet
3    Zeynep
4     Ahmet
5      Elif
Name: isim, dtype: str
"""
print("-" * 50)


#-------------------------------------------
# SORU 4
# Sadece isim ve maas sütunlarını birlikte gösterin.
#-------------------------------------------
print("-----4.Sorunun Çözümü-----")
print(df[["isim","maas"]])
"""
     isim  maas
0     Ali  5000
1    Ayşe  7000
2  Mehmet  6000
3  Zeynep  8000
4   Ahmet  4500
5    Elif  6500
"""
print("-" * 50)

#-------------------------------------------
# SORU 5
# Yaşı 28'den büyük olan kişileri filtreleyin.
#-------------------------------------------
print("-----5.Sorunun Çözümü-----")
filtre=df["yas"] > 28
print(df[filtre])
"""
     isim  yas     sehir  maas
1    Ayşe   30  İstanbul  7000
3  Zeynep   35     İzmir  8000
"""
print("-" * 50)

#-------------------------------------------
# SORU 6
# Maaşı 6000'den büyük olan kişilerin sadece isim ve maaş bilgilerini gösterin.
#-------------------------------------------
print("-----6.Sorunun Çözümü-----")
print(df[ df["maas"] > 6000 ][["isim","maas"]])
"""
     isim  maas
1    Ayşe  7000
3  Zeynep  8000
5    Elif  6500
"""

print("-" * 50)

#-------------------------------------------
# SORU 7
# Maaşa göre küçükten büyüğe sıralayın.
#-------------------------------------------
print("-----7.Sorunun Çözümü-----")
print(df.sort_values("maas"))
"""
     isim  yas     sehir  maas
4   Ahmet   22     Bursa  4500
0     Ali   25    Ankara  5000
2  Mehmet   28    Ankara  6000
5    Elif   27  İstanbul  6500
1    Ayşe   30  İstanbul  7000
3  Zeynep   35     İzmir  8000
"""
print("-" * 50)


#-------------------------------------------
# SORU 8
# Maaşa göre büyükten küçüğe sıralayın.
#-------------------------------------------
print("-----8.Sorunun Çözümü-----")
print(df.sort_values("maas", ascending=False))
"""
     isim  yas     sehir  maas
3  Zeynep   35     İzmir  8000
1    Ayşe   30  İstanbul  7000
5    Elif   27  İstanbul  6500
2  Mehmet   28    Ankara  6000
0     Ali   25    Ankara  5000
4   Ahmet   22     Bursa  4500
"""

print("-" * 50)

#-------------------------------------------
# SORU 9
# Şehirlere göre gruplama yapın ve her şehir için ortalama maaşı hesaplayın.
#-------------------------------------------
print("-----9.Sorunun Çözümü-----")
print(df.groupby("sehir")["maas"].mean())
"""
sehir
Ankara      5500.0
Bursa       4500.0
İstanbul    6750.0
İzmir       8000.0
Name: maas, dtype: float64
"""

print("-" * 50)

#-------------------------------------------
# SORU 10
# "yillik_maas" adında yeni bir sütun oluşturun
# bu sütun maaşın 12 ile çarpılmasıyla oluşturulacaktır.
#-------------------------------------------
print("-----10.Sorunun Çözümü-----")
df["yillik_maas"]=df["maas"] * 12
print(df)
"""
     isim  yas     sehir  maas  yillik_maas
0     Ali   25    Ankara  5000        60000
1    Ayşe   30  İstanbul  7000        84000
2  Mehmet   28    Ankara  6000        72000
3  Zeynep   35     İzmir  8000        96000
4   Ahmet   22     Bursa  4500        54000
5    Elif   27  İstanbul  6500        78000
"""

print("-" * 50)