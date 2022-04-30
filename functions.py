"""
NÜFUS PROJEKSİYONU YÖNTEMLERİ 
İller Bankası Yöntemi :
Bu  metot,  geometrik  artış  metodu  esasına  göre  artışın  sınırlandırıldığı  bir  yöntemdir.  
Artış hızı çoğalma katsayısı ile ifade edilir.  
"""

# C = ( ((Ns/Ne)**(1/(tS-tE))) - 1 ) * 100    # Çoğalma Katsayısı

# NG = NS * ( 1+(C/100) )**n   # Gelecekteki Nüfus

# ### MainWindow içerisindeki TexBpxlardan alınan değerler aşağıdaki değerlere atanacak.
# NS      # Son nüfus sayım değeri 
# NE      # İlk nüfus sayım değeri  
# tS      # NS (Son) nüfusunun belirlendiği yıl 
# tE      # NE (İlk) nüfusunun belirlendiği yıl 
# tG      # NG (Gelecek) nüfusun belirleneceği yıl 
# n  = tG - tS     # Son nüfus sayımından projenin başlatılmasına kadar geçen süre (tG -tS )  

def cog_kts():      # Çoğalma Katsayısı Fonksiyonu
    return (( ((Ns/Ne)**(1/(tS-tE))) - 1 ) * 100)
    
"""
Proje inşaatı bittikten sonra proje ömrünün 30 yıl kabul edildiği ve tesisin projelendirmeden 
işletmeye  alınmasına  kadar  geçen  sürenin  5  yıl  kabul  edildiği  varsayımı  ile  gelecek  nüfus 
hesabında; 
"""

NG = NS * ( 1 + (C/100) )**(30+5+n)  # Hesaplanacak olan olası nüfus (projeksiyon) değeri 
