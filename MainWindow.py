#!/usr/bin/env python
#-*-coding:utf-8-*-

from curses.textpad import Textbox
from tkinter import *
from turtle import width

pencere = Tk()      # Ana Pencere - MainWindow
pencere.geometry("360x430+500+300")
pencere.resizable(FALSE, FALSE)
pencere.title("Nüfus ve Debi Hesabı")


def pencere_hakkinda():     # "Hakkında" Penceresinin Özellikleri ve Metni                      
    hakkinda = Toplevel()
    hakkinda.title("Hakkında")
    hakkinda.geometry("300x125")
    hakkinda.resizable(FALSE, FALSE)
    yazar_adres = Label(hakkinda, text="\nNüfus ve Debi Hesabı\n\nMustafa Halil\nhttps://github.com/mhalil\n")
    yazar_adres.pack()


### Menüler
menu_cubugu = Menu(pencere)
pencere.config(menu=menu_cubugu) #menümüzü oluşturduk

dosya_menusu = Menu(menu_cubugu, tearoff=0)
menu_cubugu.add_cascade(label="Dosya", menu=dosya_menusu)
dosya_menusu.add_command(label="Aç")                # Fonksiyon Eklenecek. Aç Diyalog Kutusu
dosya_menusu.add_command(label="Kaydet")            # Fonksiyon Eklenecek. Kaydet Diyalog Kutusu
dosya_menusu.add_command(label="Farklı Kaydet...")  # Fonksiyon Eklenecek. Kaydet Diyalog Kutusu
dosya_menusu.add_command(label="Kapat", command=pencere.quit)

hakkinda_menusu = Menu(menu_cubugu, tearoff=0)
menu_cubugu.add_cascade(label="Hakkında", menu=hakkinda_menusu)
hakkinda_menusu.add_command(label="Hakkında", command=pencere_hakkinda)       

yazi_rengi = "black"
yazi_tipi = "Tahoma 10"
yazi_tipi_kalin = "Tahoma 11 bold"

### Arayüz ogeleri;
# 1. Satır
ilk_nufus_yili_etk = Label(pencere, text="İlk Nüfus Yılı:", fg = yazi_rengi, font = yazi_tipi )
ilk_nufus_yili_etk.place(x=10, y=20)

ilk_nufus_yili = Entry(pencere)     # tE
ilk_nufus_yili.place(x=150, y=15, width=150, height=30)

# 2. Satır
ilk_nufus_degeri_etk = Label(pencere, text="İlk Nüfus Değeri:", fg = yazi_rengi, font = yazi_tipi )
ilk_nufus_degeri_etk.place(x=10, y=60)

ilk_nufus_degeri = Entry(pencere, width=20)   # NE
ilk_nufus_degeri.place(x=150, y=55, width=150, height=30)

ilk_nufus_degeri_brm = Label(pencere, text="kişi", fg = yazi_rengi, font = yazi_tipi )
ilk_nufus_degeri_brm.place(x=310, y=60)

# 3. Satır
son_nufus_yili_etk = Label(pencere, text="Son Nüfus Yılı:", fg = yazi_rengi, font = yazi_tipi )
son_nufus_yili_etk.place(x=10, y=100)

son_nufus_yili = Entry(pencere, width=20)   #tS
son_nufus_yili.place(x=150, y=95, width=150, height=30)

# 4. Satır
son_nufus_degeri_etk = Label(pencere, text="Son Nüfus Değeri:", fg = yazi_rengi, font = yazi_tipi )
son_nufus_degeri_etk.place(x=10, y=140)

son_nufus_degeri = Entry(pencere, width=20)   # NS
son_nufus_degeri.place(x=150, y=135, width=150, height=30)

son_nufus_degeri_brm = Label(pencere, text="kişi", fg = yazi_rengi, font = yazi_tipi )
son_nufus_degeri_brm.place(x=310, y=140)

# 5. Satır
gelecek_nufus_yili_etk = Label(pencere, text="Gelecek Nüfus Yılı:", fg = yazi_rengi, font = yazi_tipi )
gelecek_nufus_yili_etk.place(x=10, y=180)

gelecek_nufus_yili_degeri = Entry(pencere, width=20)    # NG
gelecek_nufus_yili_degeri.place(x=150, y=175, width=150, height=30)

# 6. Satır
cogalma_katsayisi_etk = Label(pencere, text="Çoğalma Katsayısı:", fg = yazi_rengi, font = yazi_tipi )
cogalma_katsayisi_etk.place(x=10, y=220)

cogalma_katsayisi_degeri = Label(pencere, text="", fg="blue", font = yazi_tipi_kalin )         # Hesaplanacak olan Çoğalma Katsayısı Değeri bu Etikete yazılacak
cogalma_katsayisi_degeri.place(x=170, y=220)

# 7. Satır
tahmini_nufus_degeri_etk = Label(pencere, text="Tahmini Nüfus Değeri:", fg = yazi_rengi, font = yazi_tipi )
tahmini_nufus_degeri_etk.place(x=10, y=260)

tahmini_nufus_degeri = Label(pencere, text="", fg="blue", font = yazi_tipi_kalin )         # Hesaplanacak olan Tahmini Nüfus Değeri bu Etikete yazılacak
tahmini_nufus_degeri.place(x=180, y=260)

tahmini_nufus_degeri_brm = Label(pencere, text="kişi", fg = yazi_rengi, font = yazi_tipi )
tahmini_nufus_degeri_brm.place(x=310, y=260)



def hesapla():  # Çoğalma Katsayısı ve Nüfus Hesabı Fonksiyonu

    # Çoğalma Katsayısı ve Nüfus Hesabı için Entry değerlerini, fonksiyon değerlerine atama işlemi
    tE = int(ilk_nufus_yili.get())
    NE = int(ilk_nufus_degeri.get())
    tS = int(son_nufus_yili.get())
    NS = int(son_nufus_degeri.get())
    n = tS - tE

    C =  (( ((NS/NE)**(1/(tS-tE))) - 1 ) * 100) # Çoğalma Katsayısı
    NG = NS * ( 1 + (C/100) )**(30+5+n)  # Tahmini (olası) nüfus (projeksiyon) değeri 
    cogalma_katsayisi_degeri["text"] = round(C,2)
    tahmini_nufus_degeri["text"] = int(NG)
    # sonuc = list(NS, C)
    # return sonuc    # Sonucu liste olarak elde ediyoruz. Listenin ilk değeri Çoğalma Katsayısı ikinci değeri ise Tahmini Nüfus Değeri

# 8. Satır
buton_hesapla = Button(pencere, text="Hesapla", height=2, width=40, command=hesapla)     # komut eklenecek. Komut çalıştırıldığında  Gelecek Nüfus değeri ve çoğalma katsayıları hesplanıp, ekranda görünür olacak. Gerekli veriler girilmeden Buton aktif olmayacak
buton_hesapla.place(x=7, y=300)

# 9. Satır
buton_debi_hesabi = Button(pencere, text="Debi Hesabı", height=2, width=40)     # komut eklenecek. Komut çalıştırıldığında  Debi ayarları için yeni pencere açılacak. TopLevel()
buton_debi_hesabi.place(x=7, y=360)





pencere.mainloop() # tk.mainloop() ibaresi daha mı doğru? sorgula !