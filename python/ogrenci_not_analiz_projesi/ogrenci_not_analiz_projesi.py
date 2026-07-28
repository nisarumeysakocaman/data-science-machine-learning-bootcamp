"""Öğrenci Not Analiz Projesi
Plan/Program:
    1. csv dosyasından öğrenci verileri oku
    2. temel istatistiksel hesaplamalar
    3. filtreleme
    4. öğrenci notu görselleştirme
    5. OOP ile yapay class üzerinde toplama
    6. hata yönetimi
Veri seti:
    isim, yas, bolum ve not
Kurulumlar:
    pip install numpy pandas matplotlib   """

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class OgrenciNotAnalizSistemi:

    def __init__(self,dosya_yolu):
        self.dosya_yolu=dosya_yolu
        self.df=None


    def veriyi_oku(self):
        """ csv dosyasını okur ve df içerisine yükler"""

        try:
            self.df=pd.read_csv(self.dosya_yolu)

            if self.df.empty:
                raise ValueError("csv dosyası boş")

            #gerekli sütunları tanımla
            gerekli_sutunlar= {"isim","yas","bolum","not"}

            #dosyada gerekli sütunlar var mı kontrol et
            if not gerekli_sutunlar.issubset(self.df.columns):
                raise ValueError(
                    f"csv doyasında gerekli sütunlar eksik"
                    f"Gerekli sütunlar: {gerekli_sutunlar}"
                )

            self.df["not"] =pd.to_numeric(self.df["not"],errors="raise")

            print("veri başarıyla okundu")
            print(self.df)

        except FileNotFoundError:
            print(f"hata: {self.dosya_yolu} bulunamadı")

        except pd.errors.EmptyDataError:
            print("csv dosyası boş")

        except ValueError as error:
            print(f"hata: {error}")

        except Exception as e:
            print(f"beklenmeyen hata : {e}")


    def numpy_ile_hesaplama(self):
        """hesaplanan değerler:
            ortalama,en yüksek not,en düşük not ve standart sapma
        """

        try:

            if self.df is None: #önce veri yüklenmiş olmalı
                raise ValueError("önce veri yüklenmeli")


            #not sütununu numpy dizisine çevirme
            notlar=self.df["not"].to_numpy()

            #numpy ile temel istatistikleri hesapla
            print(f"Ortalama: {np.mean(notlar)}")
            print(f"En yüksek not: {np.max(notlar)}")
            print(f"En düşük not: {np.min(notlar)}")
            print(f"Standart Sapma: {np.std(notlar)}")

        except ValueError as hata:
            print(f"hata: {hata}")

        except Exception as e:
            print(f"Beklenmeyen bir hata oluştu: {e}")

    def pandas_ile_filtreleme(self):
        """
        filtrelemeler:
            -notu 80'den büyük olan öğrenciler
            -yaşı 22'den büyük olanlar
            -bölümü yapay zeka olanlar
        """

        try:
            if self.df is None:
                raise ValueError("Önce veri okunmalıdır.")

            print("Pandas ile filtreleme sonuçları")

            #notu 80'den yüksek olan öğrenciler
            yuksek_notlular=self.df[self.df["not"] >80]
            print(f"Notu 80'den yüksek olan öğrenciler:\n{yuksek_notlular}")

            #bölümü yapay zeka olan öğrenciler
            yapay_zeka_ogrencileri=self.df[self.df["bolum"]=="Yapay Zeka"]
            print(f"Yapay Zeka bölümünde okuyan öğrenciler:\n{yapay_zeka_ogrencileri}")

            #22 yaşından büyük olan öğrenciler
            buyuk_ogrenciler=self.df[self.df["yas"] > 22]
            print(f"Yaşı 22'den büyük olan öğrenciler :\n{buyuk_ogrenciler}")


        except ValueError as hata:
            print(f"hata: {hata}")

        except Exception as e :
            print(f"beklenmeyen hata : {e}")


    def grafik_ciz(self):
        """
            öğrenci notlarını sütun grafiği ile görselleştirme
        """    

        try:

            if self.df is None:
                raise ValueError("Önce veri okunmalı")

            #grafik boyutu ayarla
            plt.figure(figsize=(10,5))

            #isimleri x eksenine,notları y eksenine ekleme
            plt.bar(self.df["isim"],self.df["not"])
            plt.title("Öğrenci Not Grafiği")
            plt.xlabel("Öğrenci İsimleri")
            plt.ylabel("Öğrenci Notları")

            plt.tight_layout() #grafiği daha iyi göstermek için
            plt.show()

        except Exception as e:
            print(f"hata: {e}")


    def tum_analizi_calistir(self):

        #1. veriyi okuma
        self.veriyi_oku()

        #eğer veri yüklenmezse
        if self.df is None:
            print("Analiz durduruldu")
            return

        #2. numpy hesaplamaları
        self.numpy_ile_hesaplama()

        #3. pandas ile filtreleme
        self.pandas_ile_filtreleme()

        #4. görselleştirme
        self.grafik_ciz()

#programın başlangıç noktası

if __name__ =="__main__":

    dosya_yolu="ogrenci_notlari.csv"
    sistem=OgrenciNotAnalizSistemi(dosya_yolu)

    sistem.tum_analizi_calistir()

