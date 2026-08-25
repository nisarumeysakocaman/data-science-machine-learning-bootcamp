"""
numpy:  yüksek performanslı sayısal hesap kütüphanesi
        numpy C dili ile yazılmıştır 

Numpy Neden Gerekli?
    daha hızlı hesaplama
    çok boyutlu veri yapıları
    matrisler, N boyutlu dizi ile, veri tabloları
    matematiksel işlem kolaylığı
Numpy ve Yapay Zeka
    scikit-learn (ml)
    tensorflow ve pytorch (dl)
    pandas (data science)
Numpy bölümünde ne öğrenicez?
    Diziler
    matematiksel işlemler
    indeksleme ve dilimleme
    dizi birleştirme ve bölme
    çok boyutlu diziler
    matris işlemleri
    rastgele say üretimi """

import numpy as np

sayilar=[1,2,3,4,5]
print(sayilar)

#np.array python dizisini numpy array'ine dönüştürür
dizi=np.array(sayilar) #numpy dizisi
print(dizi)

#numpy dizisi tipini inceleme
print(type(dizi)) #<class 'numpy.ndarray'>

#numpy dizisinin boyutunu öğrenme
print(dizi.shape)  #(5,) -> tek boyutlu 5 elemanlı bir dizi

#numpy dizisi veri tipi
print(dizi.dtype) #int64 -> integer

#numpy ile dizi oluşturmanın farklı yolları
dizi=np.zeros(5)  #[0. 0. 0. 0. 0.]  , elemanları 0 olan 5 elemanlı bir dizi oluşturduk
print(dizi)

dizi=np.ones(5) #[1. 1. 1. 1. 1.] , elemanları 1 olan 5 elemanlı bir dizi oluşturduk
print(dizi)

#belirli bir aralıkta sayı dizisi oluşturma
dizi=np.arange(0,10) #[0 1 2 3 4 5 6 7 8 9] , 10 dahil değil
print(dizi)

#belirli aralıklarla sayı üretme
dizi=np.arange(0,10,2) # [0 2 4 6 8] , en sondaki 2 aralık değeridir.
print(dizi)

#belirli bir aralığa eşit bölünmüş diziler
dizi=np.linspace(0,10,5) # [ 0.   2.5  5.   7.5 10. ] , burada 0 ve 10 arasında eşit aralıklı toplam 5 eleman üretti
print(dizi)


"""matematiksel işlemler"""

#toplama : z= a0 + a1w1

a=np.array([1,2,3])
b=np.array([4,5,6])
sonuc=a+b
print(sonuc) #[5 7 9]

#çıkarma 
a=np.array([1,2,3])
b=np.array([4,5,6])
sonuc=a-b
print(sonuc) #[-3 -3 -3]

#çarpma
sonuc=a*b
print(sonuc) #[ 4 10 18]

#bölme
sonuc=a/b
print(sonuc) #[0.25 0.4  0.5 ]

#dizi ile sayı arasında işlem yapma
a=np.array([10,20,30])
sonuc=a*3
print(sonuc) #[30 60 90]

#dizinin karesini alma
a=np.array([6,7,8])
sonuc=a ** 2  # a ** 3 -> a üzeri 3 , a**4 -> a üzeri 4 ...
print(sonuc) #[36 49 64]

#karekökünü alma
a=np.array([36,49,100])
sonuc=np.sqrt(a)
print(sonuc)

#dizinin toplamını bulma
a=np.array([4,5,6,7])
print(np.sum(a))  #22

#ortalama
print(np.mean(a))  #5.5


#min ve max değerler
print(np.max(a)) #7
print(np.min(a)) #4

#standart sapma
print(np.std(a))  #1.118033988749895

"""indexing and slicing"""
#indexing
dizi=np.array([10,20,30,40,50])
print(dizi[0]) #10
print(dizi[-1]) #50

#slicing
dizi=np.array([50,60,70,80,90])
print(dizi[1:3]) #[60 70] 

print(dizi[:4]) #[50 60 70 80]

print(dizi[2:]) #[70 80 90]

#step kullanımı
print(dizi[::2]) #diziden ikişer adım ile eleman seçmek , [50 70 90]

#2 boyutlu dizilerde indeksleme
matris=np.array(
    [
    [1,2,3,4],
    [5,6,7,8],
    [6,8,3,7],
    [3,7,9,1]
    ]
)

print(matris)

print(matris[0,0]) #1

print(matris[3,2]) #9

#belirli bir satırı seçmek
print(matris[1, :]) #[5 6 7 8]

#belirli bir sütunu seçmek
print(matris[: ,3])  #[4 8 7 1]

#matris dilimleme
print(matris[1:3,1:3]) 
"""[[6 7]
    [8 3]]  çıktısını verir ,satır olarak 1 ve 2'yi ve sütun olarak da 1 ve 2'yi alır ve onların kesişimini yazdırır """

#dizi birleştirme
a=np.array([1,2,3])
b=np.array([4,5,6])
sonuc=np.concatenate((a,b)) # [1 2 3 4 5 6] 
print(sonuc)

#iki boyutlu dizi birleştirme
a=np.array([
    [1,2],
    [3,4]
])

b=np.array([
    [5,6],
    [7,8]
])

sonuc=np.concatenate((a,b))
print(sonuc)
"""[[1 2]
    [3 4]
    [5 6]
    [7 8]]   satır bazında birleştirme yapar       """


"""NOT: axis=0 ise satır bazında birleştirme, axis=1 ise sütun bazında birleştirme yapar"""

sonuc=np.concatenate((a,b), axis=1)
print(sonuc)
"""[[1 2 5 6]
    [3 4 7 8]] burada sütun bazında birleştirme yaptık"""

#vstack -> dikey birleştirme
sonuc=np.vstack((a,b))
print(sonuc)
"""[[1 2]
    [3 4]
    [5 6]
    [7 8]]
"""

#hstack -> yatay birleştirme
sonuc=np.hstack((a,b))
print(sonuc)
"""[[1 2 5 6]
    [3 4 7 8]]"""

#diziyi parçalara bölme
dizi=np.array([1,2,3,4,5,6])

sonuc=np.split(dizi,2) #diziyi 2 eşit  parçaya böler,2 yerine 4 yazsaydık eşit bölemeyeceği için hata verirdi
print(sonuc) #[array([1, 2, 3]), array([4, 5, 6])]

sonuc=np.split(dizi,3) #diziyi 3 eşit parçaya böler
print(sonuc) #[array([1, 2]),   array([3, 4]),   array([5, 6])]

#2 boyutlu dizilerde bölme
matris=np.array([
    [1,2],
    [3,4],
    [5,6],
    [7,8]
])

sonuc=np.split(matris,2) #satır bazında 2'ye bölme
print(sonuc)
"""[array([[1, 2],
           [3, 4]]), 

    array([[5, 6],
           [7, 8]])]"""


sonuc=np.split(matris,2,axis=1) #sütun bazında 2'ye bölme
print(sonuc)
"""[array([ [1],
            [3],
            [5],
            [7]]), 

     array([[2],
            [4],
            [6],
            [8]] )]   """

#2 boyutlu dizi oluşturma
matris=np.array([
    [1,2],
    [3,4],
    [5,6],
    [7,8]
])
print(matris)
"""[[1 2]
    [3 4]
    [5 6]
    [7 8]]
"""

print(matris.shape) #(4, 2)

print(matris.ndim) #2

print(matris.size) #8 -> eleman sayısı

#3 boyutlu dizi oluşturma 

"""görsel -> (height,width) -> (1920 ,1080),(1920,1080),(1920,1080)...(1920,1080) -> (N adet,1920,1080) """

dizi=np.array([
    [ [1,2],
      [3,4]

    ],
    [
        [5,6],
        [7,8]

    ]
])

print(dizi)
""" [[[1 2]
      [3 4]]

    [[5 6]
     [7 8]]] """

print(dizi.shape) #(2, 2, 2) -> (2 adet matris,her matriste 2 satır,her matriste 2 sütun)


#numpy ile çok boyutlu dizi oluşturma  reshape
dizi=np.arange(12)
print(dizi) #[ 0  1  2  3  4  5  6  7  8  9 10 11]

#matrise dönüştürme
matris=dizi.reshape(3,4) 
print(matris)
""" [[ 0  1  2  3]
    [ 4  5  6  7]
    [ 8  9 10 11]]  """


#matris işlemleri
a=np.array([
    [1,2],
    [3,4]
])

b=np.array([
    [5,6],
    [7,8]
])

sonuc=a+b
print(sonuc)
"""
[[ 6  8]
 [ 10 12]]

"""
sonuc=a-b
print(sonuc)
sonuc=a*b
print(sonuc)

#gercek matris carpimi
sonuc=np.dot(a,b)
print(sonuc)
"""
[[19 22]
 [43 50]]
"""

#matrisin transpose'u
print(a.T)
"""
[[1 3]
 [2 4]]
"""

#matris determinantı
det=np.linalg.det(a)
print(det) # -2.0000000000000004

#matrisin tersi
ters=np.linalg.inv(a)
print(ters)
"""
[[-2.   1. ]
 [ 1.5 -0.5]] 
"""

"""rastgele sayı üretme"""

#rastgele ondalıklı sayı üretme
rastgele=np.random.rand(5) # 5 tane rastgele odanlıklı sayı üretir
print(rastgele) #[0.83969961 0.74822063 0.33181003 0.77928359 0.03357956]

#rastgele matris oluşturma
rastgele=np.random.rand(3,3) #3'e 3'lük bir ondalıklı sayı matrisi üretir
print(rastgele)
"""
[[0.97762589 0.34017253 0.52461947]
 [0.77672133 0.25107575 0.80243266]
 [0.11392152 0.562569   0.25894579]]  
"""

#rastgele tam sayı üretme
rastgele=np.random.randint(1,20,5) #1 ile 20 arasındaki sayılardan rastgele 5 tane tam sayı üretir
print(rastgele) #[ 4 13 11 17 13]

#rastgele tam sayı matrisi oluşturma
rastgele=np.random.randint(1,30,(3,4)) #1 ile 30 arasındaki tam sayılarla (3,4)'lük bir matris oluşturur
print(rastgele)
"""
[[ 8  8  1 29]
 [ 5 12 15  6]
 [ 4 19 24 27]]
"""
#aynı rastgele sonucu üretmek için -> seed
np.random.seed(50) #seed(50) olduğu sürece hep aynı rastgele sayıları üretecek, 50'yi değiştirirsek sonuç da değişir
rastgele=np.random.rand(5) 
print(rastgele) #[0.49460165 0.2280831  0.25547392 0.39632991 0.3773151 ] 

#bir diziden rastgele eleman seçmek
dizi=np.array([1,2,3,4,5,6,7])
sonuc=np.random.choice(dizi)
print(sonuc) #7

#birden fazla eleman seçme
sonuc=np.random.choice(dizi,3)
print(sonuc) #[6 6 3]
