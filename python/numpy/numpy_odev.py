#--------------------------------------------
# SORU 1
# 1) NumPy kullanarak 1'den 20'ye kadar sayılardan oluşan bir dizi oluşturun.
# 2) Dizinin kaç eleman içerdiğini ekrana yazdırın.
#--------------------------------------------
import numpy as np

print("-------1.Sorunun Cozumu------")
dizi=np.arange(1,21)
print("dizi1: ", dizi)
print("eleman sayisi: " ,dizi.size)

print("-"*50)

#--------------------------------------------
# SORU 2
# 1) [5, 10, 15, 20, 25] değerlerinden oluşan bir NumPy dizisi oluşturun.
# 2) Dizideki tüm elemanları 3 ile çarpın.
# 3) Sonucu ekrana yazdırın.
#--------------------------------------------
print("-------2.Sorunun Cozumu------")
dizi=np.arange(5,30,5)
print(dizi)
print("dizi 3 ile carpildi: ",dizi*3)

print("-"*50)

#--------------------------------------------
# SORU 3
# 1) 0'dan 30'a kadar sayılar içeren bir dizi oluşturun.
# 2) Bu diziden sadece 10 ile 20 arasındaki elemanları slicing kullanarak seçin.
#--------------------------------------------
print("-------3.Sorunun Cozumu------")

dizi=np.arange(0,31)
print(dizi[10:21]) #[10 11 12 13 14 15 16 17 18 19 20]

print("-"*50)

#--------------------------------------------
# SORU 4
# 1) [1,2,3] ve [4,5,6] dizilerini oluşturun.
# 2) Bu iki diziyi NumPy kullanarak birleştirin.
#--------------------------------------------
print("-------4.Sorunun Cozumu------")
a=np.array([1,2,3])
b=np.array([4,5,6])
sonuc=np.concatenate((a,b))
print("diziler birlestirildi: ", sonuc)

print("-"*50)

#--------------------------------------------
# SORU 5
# 1) 1'den 12'ye kadar sayılar içeren bir dizi oluşturun.
# 2) Bu diziyi reshape kullanarak 3x4 boyutunda bir matrise dönüştürün.
# 3) Matrisin shape değerini yazdırın.
#--------------------------------------------
print("-------5.Sorunun Cozumu------")

dizi=np.arange(1,13)
print(dizi)
sonuc=dizi.reshape(3,4)
print(f"dizi matrise donusturuldu: {sonuc}") #dizi matrise donusturuldu: [[ 1  2  3  4]
print(sonuc.shape) #(3, 4)

print("-"*50)



#--------------------------------------------
# SORU 6
# 1) Aşağıdaki matrisi oluşturun
#[[1,2,3],
#[4,5,6],
# [7,8,9]]
# 2) İkinci satırı ekrana yazdırın.
#3) İkinci sütunu ekrana yazdırın.
#--------------------------------------------
print("-------6.Sorunun Cozumu------")
matris=np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
print(f"2.satir: {matris[1,:]}") #2.satir: [4 5 6]
print(f"2.sutun: {matris[:,1]}") #2.sutun: [2 5 8]
 
print("-"*50)

#--------------------------------------------
# SORU 7
# 1) 3x3 boyutunda rastgele sayılardan oluşan bir matris oluşturun.
# 2) Matrisin ortalamasını hesaplayın.
# 3) Matrisin maksimum değerini yazdırın.
#--------------------------------------------
print("-------7.Sorunun Cozumu------")
matris=np.random.rand(3,3)
print(f"matris: {matris}")
ortalama=np.mean(matris)
print(f"ortalama: {ortalama}")
print(f"maksimum deger: {np.max(matris)}")

print("-"*50)



#--------------------------------------------
# SORU 8
# 1) [2,4,6,8] ve [1,3,5,7] dizilerini oluşturun.
# 2) Dizileri eleman bazlı çarpın.
#3) Sonucu ekrana yazdırın.
#--------------------------------------------
print("-------8.Sorunun Cozumu------")
a=np.array([2,4,6,8])
b=np.array([1,3,5,7,])
sonuc=a*b
print(f"a*b= {sonuc}")

print("-"*50)

#--------------------------------------------
# SORU 9
# 1) 1'den 9'a kadar sayılar içeren bir dizi oluşturun.
# 2) Bu diziyi 3x3 matrise dönüştürün.
# 3) Matrisin transpose'unu hesaplayın.
#--------------------------------------------
print("-------9.Sorunun Cozumu------")
dizi=np.arange(1,10)
matris=dizi.reshape(3,3)
print(f"matris: {matris}")
print(f"transpose: {matris.T}")
"""
transpose: [[1 4 7]
            [2 5 8]
            [3 6 9]]
"""


print("-"*50)


#--------------------------------------------
# SORU 10
# 1) 1 ile 50 arasında rastgele 10 tam sayı üretin.
#2) Bu sayılardan oluşan dizinin toplamını hesaplayın.
#3) Dizinin ortalamasını yazdırın.
#--------------------------------------------
print("-------9.Sorunun Cozumu------")
dizi=np.random.randint(1,50,10)
print(f"dizi: {dizi}")
toplam=np.sum(dizi)
print(f"toplam= {toplam}")
print(f"ortalama= {np.mean(dizi)}")


print("-"*50)