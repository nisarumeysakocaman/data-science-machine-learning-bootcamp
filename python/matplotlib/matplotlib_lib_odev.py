# ÖRNEK VERİ SETİ
# Aşağıdaki veri seti tüm sorular için kullanılacaktır.
aylar = ["Ocak", "Şubat", "Mart", "Nisan", "Mays", "Haziran"]
satislar = [120, 150, 170, 160, 200, 220]
karlar = [20, 35, 40, 30, 50, 60]
reklam = [5, 8, 10, 7, 12, 15]
import matplotlib.pyplot as plt

#---------------------------------------
# SORU 1
# Aylar ve satışlar verisini kullanarak basit bir çizgi grafiği oluşturun.
#---------------------------------------
print("-----1.Sorunun Çözümü-----")
plt.plot(aylar,satislar,color="green")
plt.title("aylık satış")
plt.xlabel("aylar")
plt.ylabel("satışlar")
plt.show()

print("-"*50)

#---------------------------------------
# SORU 2
# Aylar ve kârlar verisini kullanarak çizgi grafiği oluşturun.
# Çizgi rengi kırmızı olsun.
#---------------------------------------
print("-----2.Sorunun Çözümü-----")
plt.plot(aylar,karlar,color="red")
plt.title("aylık karlar")
plt.xlabel("aylar")
plt.ylabel("karlar")
plt.show()

print("-"*50)

#---------------------------------------
# SORU 3
# Aylar ve satışlar verisini kullanarak marker'lı bir çizgi grafiği oluşturun.
#---------------------------------------
print("-----3.Sorunun Çözümü-----")
plt.plot(aylar,satislar,marker="o")
plt.title("aylik satislar")
plt.xlabel("karlar")
plt.ylabel("satışlar")
plt.show()

print("-"*50)


#---------------------------------------
# SORU 4
# Aylar ve satışlar verisini kullanarak sütun grafiği oluşturun.
#---------------------------------------
print("-----4.Sorunun Çözümü-----")
plt.bar(aylar,satislar)
plt.title("aylık satışlar -> bar chart")
plt.xlabel("aylar")
plt.ylabel("satışlar")
plt.show()

print("-"*50)


#---------------------------------------
# SORU 5
# Aylar ve reklam verisini kullanarak yeşil renkli bir sütun grafiği oluşturun.
#---------------------------------------
print("-----5.Sorunun Çözümü-----")
plt.bar(aylar,reklam,color="green")
plt.title("aylık reklam")
plt.xlabel("aylar")
plt.ylabel("reklam")
plt.show()

print("-"*50)


#---------------------------------------
# SORU 6
# Satışlar verisini kullanarak pasta grafiği oluşturun.
# Ay isimlerini etiket olarak gösterin ve yüzdeleri ekrana yazdırın.
#---------------------------------------
print("-----6.Sorunun Çözümü-----")
plt.pie(satislar,labels=aylar,autopct="%1.1f%%")
plt.title("Aylara göre satış dağılımı")
plt.axis("equal")
plt.show()


print("-"*50)


#---------------------------------------
# SORU 7
# Reklam ve satışlar verisini kullanarak scatter plot oluşturun.
#---------------------------------------
print("-----7.Sorunun Çözümü-----")
plt.scatter(reklam,satislar)
plt.title("reklam-satış grafiği")
plt.xlabel("reklamlar")
plt.ylabel("satışlar")
plt.show()

print("-"*50)



#---------------------------------------
# SORU 8
#Reklam ve kar verisini kullanarak kırmızı renkli ve büyük noktalı scatter plot oluşturun.
#---------------------------------------
print("-----8.Sorunun Çözümü-----")
plt.scatter(reklam,karlar,s=100,color="red")
plt.title("reklam-kar grafiği")
plt.xlabel("reklamlar")
plt.ylabel("karlar")
plt.show()


print("-"*50)

#---------------------------------------
# SORU 9
# Aynı figür içinde 1 satır 2 sütun olacak şekilde iki grafik oluşturun.
# Solda satışlar için line plot, sağda kârlar için bar chart gösterin.
#---------------------------------------
print("-----9.Sorunun Çözümü-----")
plt.subplot(1,2,1)
plt.plot(aylar,satislar)
plt.title("ay-satış grafiği")
plt.xlabel("aylar")
plt.ylabel("satışlar")
plt.subplot(1,2,2)
plt.bar(aylar,karlar)
plt.title("ay-kar grafiği")
plt.xlabel("aylar")
plt.ylabel("karlar")
plt.show()


print("-"*50)


#---------------------------------------
# SORU 10
# 2 satır 2 sütun olacak şekilde 4 farklı grafik oluşturun.
# 1. grafik: satışlar line plot
# 2. grafik: kârlar bar chart
# 3. grafik: reklam-satış scatter plot
# 4. grafik: satışlar pie chart
#---------------------------------------
print("-----10.Sorunun Çözümü-----")

plt.subplot(2,2,1)
plt.plot(aylar,satislar)
plt.title("ay-satış line plot")
plt.xlabel("aylar")
plt.ylabel("satışlar")

plt.subplot(2,2,2)
plt.bar(aylar,karlar)
plt.title("ay-kar bar chart")
plt.xlabel("aylar")
plt.ylabel("karlar")

plt.subplot(2,2,3)
plt.scatter(reklam,satislar)
plt.title("reklam-satışlar scatter plot")
plt.xlabel("reklam")
plt.ylabel("satışlar")

plt.subplot(2,2,4)
plt.pie(satislar,labels=aylar,autopct="%1.1f%%")
plt.title("ay-satış pie chart")

plt.tight_layout() #grafikteki ögelerin birbiri üzerine binmesini veya çerçevenin dışına taşmasını engeller

plt.show()

print("-"*50)