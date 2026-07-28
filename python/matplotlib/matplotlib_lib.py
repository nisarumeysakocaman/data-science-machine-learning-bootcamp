"""
Matplotlib Nedir?
    görselleştirme kütüphanesi
    veriyi anlamak için görselleştiriyoruz
Matplotlib ile neler yapabiliriz?
    line, sütun, pasta, dağılım
Matplotlib ve Numpy/Pandas
    Örnek veri işleme süreci
    veri okunur (pandas)
    veri düzenleme (pandas)
    veri üzerinde işlemler yapi lir (Numpy veya pandas)
    veri grafikler ile gösterilir (matplotlib)
Bu bölüm ne öğreneceğiz?
    line plot (çizgi):zaman içinde değişen verileri görselleştirmek için kullanırız
    bar chart (sütun):kategorik verileri karşılaştırmak için kullanılır
    pie chart (pasta): bir bütünün parçalarını görmek için kullanılır
    scatter plot (dağ 12m): iki değişken arasındaki ilişkiyi görmek için kullanılır
    subplots : birden fazla grafiği aynı anda gösterme
    """

import matplotlib.pyplot as plt

"""line plot"""

#çizgi grafiği oluşturma
gunler=[1,2,3,4,5]
sicaklik=[23,25,21,27,30]

#(x=gunler ,y=sicaklik)
#color -> grafik çizgisinin rengini değiştirir
#linestyle -> çizginin stilini değiştirir
#mark -> grafik çizgisini noktalı gösterir
plt.plot(gunler,sicaklik,color="green", linestyle="--",marker="o") #plt.plot çizgi grafiği oluşturur
plt.title("Günlere Göre Sıcaklık Grafiği") #Grafik başlığı
plt.xlabel("Günler") # x ekseni etiketi
plt.ylabel("Sıcaklık") # y ekseni etiketi
plt.grid(True) #grafiğin arkasını çizgili yapar
plt.show()

"""bar charts (sütun grafikleri)"""

isim=["nisa","mehmet","hasan","zeynep"]
yas=[22,34,24,30]

renkler=["orange","blue","yellow","green"]

#plt.bar sütun grafiği oluşturur
plt.bar(isim,yas,color=renkler) #burada renkler listesi ile her sütun farklı renk olacak
plt.title("Öğrenci Yaş Grafiği")
plt.xlabel("İsim")
plt.ylabel("Yaş")
plt.show()

#yatay sütun grafiği oluşturma 
plt.barh(isim,yas)
plt.title("Yatay Yaş Grafiği")
plt.show()

"""pie chart"""

etiketler=["python","C#","Java","C++"]
oranlar=[30,45,17,8]
ayrim=[0,0.08,0,0]
renkler=["pink","purple","orange","blue"]

#explode -> dilimi daha ayrık göstermek için kullanılır
#autopct -> dilimlerin yüzdesini gösterir ,1.1f olursa virgülden sonra 1 basamak gösterir
#colors -> dilimlerin rengini ayarlamak için kullanılır
plt.pie(oranlar,labels=etiketler,colors=renkler,explode=ayrim,autopct="%1.1f%%") #plt.pie pasta grafiği oluşturur
plt.title("Programlama Dillerinin Kullanım Oranları")
plt.show()

"""scatter plot (dağılım grafiği)"""

calisma_saatleri=[1,2,3,4,5]
notlar=[45,56,60,78,89]

#s -> noktanın boyutunu ayarlamak için kullanılır
plt.scatter(calisma_saatleri,notlar,color="green",s=75)
plt.xlabel("Çalışma Saatleri")
plt.ylabel("Alınan Notlar")
plt.title("Ders Çalışma Saatleri ve Alınan Notlar")
plt.show()

#birden fazla veri grubu çizdirme


calisma_saatleri=[1,2,3,4,5]
mat=[45,56,60,78,89]
plt.scatter(calisma_saatleri,mat,color="blue",label="matematik")

calisma_saatleri=[1,2,3,4,5]
fen=[32,44,50,67,90]
plt.scatter(calisma_saatleri,fen,color="red",label="fen")
plt.legend() #labelları ekranda göstermek için kullanıyoruz
plt.show()


"""subplots"""

x=[1,2,3,4]
y1=[10,56,30,40]
y2=[50,60,32,80]

plt.subplot(1,2,1) #1 satır 2 sütunluk bir grafik oluşturur, en sondaki 1 de ilk oluşacak grafiği temsil ediyor.
plt.plot(x,y1)
plt.title("Grafik 1")
plt.subplot(1,2,2) # 2.grafiği oluşturur
plt.plot(x,y2)
plt.title("Grafik 2")

plt.show()

#farklı grafik türleri kullanarak subplot oluşturma

gunler=[1,2,3,4,5]
sicaklik=[23,25,21,27,30]

plt.subplot(1,2,1)
plt.plot(gunler,sicaklik)
plt.title("Line Plot ")
plt.subplot(1,2,2)
plt.bar(gunler,sicaklik)
plt.title("Bar Chart")
plt.show()

#2x2 grafik oluşturma
gunler=[1,2,3,4,5]
sicaklik=[23,25,21,27,30]

plt.subplot(2,2,1) # 2 satır 2 sütunluk bir grafik oluşturur ,1 ise ilk grafiği temsil ediyor
plt.plot(gunler,sicaklik)
plt.title("line plot")

plt.subplot(2,2,2)
plt.bar(gunler,sicaklik)
plt.title("bar chart")

plt.subplot(2,2,3)
plt.scatter(gunler,sicaklik)
plt.title("scatter plot")

plt.subplot(2,2,4)
plt.pie(sicaklik)
plt.title("pie chart")

plt.show()
