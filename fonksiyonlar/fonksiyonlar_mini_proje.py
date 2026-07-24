#---Fonksiyonlar Mini Proje---
#Kullanıcıdan vize notu ve final notu alalım
#Ortalama hesaplama
#harf notu belirleme
#sonucu ekrana yazdırma

#not hesaplama 
def ortalama_hesapla(vize: float,final: float) -> float:
    """Vize %40,final %60 etkileyecek."""
    sonuc=0.4*vize+0.6*final
    return sonuc


def harf_notu_belirle(ortalama: float) -> str:
    """ortalamaya göre harf notu döndürür"""
    if ortalama>= 85:
        return "AA"
    elif ortalama>=75:
        return "BB"
    elif ortalama>=50:
        return "CC"
    else:
        return "FF"

def sonucu_yazdir(isim: str,ort:float,harf:str):
    """bütün sonuçları ekrana yazdırır"""
    print("------SONUC-------")
    print(f"isim: {isim} \nortalama: {ort} \nharf notu: {harf}")
    


#program akışı
isim=input("Enter a name: ")
vize=float(input("enter a midterm grade: "))
final=float(input("enter a final grade: "))

ortalama=ortalama_hesapla(vize=vize,final=final)
harf=harf_notu_belirle(ortalama=ortalama)
sonucu_yazdir(isim=isim,ort=ortalama,harf=harf)