dosya=open("ornek.txt","r",encoding="utf-8")
icerik=dosya.read() #tüm dosyayı okur
print(icerik)
dosya.close()

#satır satır okuma
dosya=open("ornek.txt","r",encoding="utf-8")

for satir in dosya:
    print(satir.strip()) #strip() satır sonu boşluklarını temizler

dosya.close()

#dosya işlemleri

dosya=open("ornek.txt","r",encoding="utf-8")
icerik=dosya.read()
dosya.close()

print(icerik)
yeni_icerik=icerik.upper() #dosyadaki tüm harfleri büyük harfe çevirir
print(f"---Yeni icerik---\n{yeni_icerik}")

#satır sayısını bulma
dosya=open("ornek.txt","r",encoding="utf-8")
satirlar=dosya.readlines() #satır satır dosyayı okur,liste döndürür
dosya.close()

print(f"Dosyadaki toplam satir sayisi: {len(satirlar)}")

#dosyaya yazma
dosya=open("yeni_dosya.txt","w",encoding="utf-8")
dosya.write("Hello World")
dosya.write("\nBu dosyayı neden oluşturduğumu ben de bilmiyorum")
dosya.close()

#oku-işle-kaydet
dosya=open("yeni_dosya.txt","r",encoding="utf-8")
icerik=dosya.read()
dosya.close()

yeni_icerik=icerik.upper()

dosya=open("son_dosya.txt","w",encoding="utf-8") #txt dosyası yoksa oluşturur
dosya.write(yeni_icerik)
dosya.close()


#with yapısı

with open("ornek.txt","r",encoding="utf-8") as dosya: #with dosyası otomatik olarak kapatır,hata olsa bile kapanır
    icerik=dosya.read()
    print(icerik)

with open("with_dosya.txt","w",encoding="utf-8") as dosya:
    dosya.write("With deniyorum ve bu yüzden bu dosyaya bir şeyler yazıyorum.")
