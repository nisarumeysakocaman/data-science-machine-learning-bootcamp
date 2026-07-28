"""Veri analizi aracı
        sayı listesi tutma
        bu sayıların toplamın hesapla
        ortalamasını bul
        en büyük ve en küçük değerleri göster  """

class VeriAnaliz:
    def __init__(self,veriler):
        self.veriler=veriler

    def veri_goster(self):
        print(f"Veriler: {self.veriler}")

    def toplam_hesapla(self):
        toplam=sum(self.veriler)
        print(f"Verilerin Toplamı: {toplam}")

    def ortalama_bul(self):
        ortalama=sum(self.veriler)/len(self.veriler)
        print(f"Verilerin Ortalaması: {ortalama}")

    def min_bul(self):
        minimum=min(self.veriler)
        print(f"Minimum Değer: {minimum}")

    def max_bul(self):
        maximum=max(self.veriler)
        print(f"Maximum Değer: {maximum}")


analiz1=VeriAnaliz([10,20,30,40,50,60])

analiz1.veri_goster()
analiz1.toplam_hesapla()
analiz1.ortalama_bul()
analiz1.min_bul()
analiz1.max_bul()
"""
Veriler: [10, 20, 30, 40, 50, 60]
Verilerin Toplamı: 210
Verilerin Ortalaması: 35.0
Minimum Değer: 10
Maximum Değer: 60
"""
