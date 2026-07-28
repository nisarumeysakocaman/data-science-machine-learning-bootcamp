"""Environment (Ortam)
Bir projenin callsmasa icin gerekli olan python sürümü, kütüphaneler, paketler gibi 
bileşenlerin bulunduğu çalisma alaridir.
bir proje için gerekli python araçlarının bulunduğu izloe bir çalışma alanadir

Neden kullanilir:
    farkla projelerde farklı paket sürümleri
        -Proje A: numpy 1.20
        -Proje B: numpy 1.26

Virtual Environment (Sanal ortam)
    kurulum: python -m venv venv

aktif hale getirmek:
    windows: .\venv\Scripts\activate
    mac, linux: source venv/bin/activate

Paket Yöneticisi (pip)
-kütüphane = paket
    numpy: sayısal işlemler
    pandas: veri analizi
    matploblit: görselleştirme

python paketleri yönetmek için kullanılan arac: pip
    -paket kurabilir
    -silebilir
    -listeleyebilir

Paket kurma:
numpy: pip install numpy
pandas, matplotlib: pip install pandas matplotlib  

NOT: pip list ,kurduğumuz kütüphaneleri listeler 

requirements.txt
    bir projenin ihtiyaç duyduğu tüm paketlerin listelendiği dosya
    bu dosya sayesinde başka bir projeyi kolayca çalıstırabiliriz.
    pip freeze > requirements.txt
Kurulum:
pip install -r.\requirements.txt    """