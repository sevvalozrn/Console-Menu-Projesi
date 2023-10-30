import tkinter as tk
from tkinter import simpledialog
from functools import reduce

def k_kucuk():
    k = simpledialog.askinteger("K Değeri", "K değerini giriniz:")
    if k is not None:
        liste = simpledialog.askstring("Liste", "Liste değerlerini aralarında birer boşluk olacak şekilde giriniz:")
        if liste is not None:
            liste = list(map(int, liste.split()))
            liste.sort()
            k_kucuk_sonuc = liste[k - 1]
            sonuc_pencere("K. Küçük Sonuç", f"K. küçük değer: {k_kucuk_sonuc}")

def en_yakin_sayi_cifti():
    sayi = simpledialog.askinteger("Sayı", "Sayıyı giriniz:")
    if sayi is not None:
        liste = simpledialog.askstring("Liste", "Liste değerlerini aralarında birer boşluk olacak şekilde giriniz:")
        if liste is not None:
            liste = list(map(int, liste.split()))
            liste.sort()
            min_fark = float('inf')
            for i in range(len(liste)):
                m = i + 1
                for m in range(len(liste) - i):
                    fark = abs(sayi - (liste[i] + liste[m]))
                    if fark < min_fark:
                        min_fark = fark
                        cift1 = liste[i]
                        cift2 = liste[m]
            sonuc_pencere("En Yakın Sayı Çifti Sonuç", f"{cift1} ve {cift2}")

def tekrar_eden_elemanlar():
    liste = simpledialog.askstring("Liste", "Liste değerlerini aralarında birer boşluk olacak şekilde giriniz:")
    if liste is not None:
        liste = list(map(int, liste.split()))
        tekrar = list({eleman for eleman in liste if liste.count(eleman) > 1})
        sonuc_pencere("Tekrar Eden Elemanlar Sonuç", tekrar)

def matrix_carpimi():
    def mat_al(matris):
        satir_s = simpledialog.askinteger("Matris Satır Sayısı", "Kaç satırlı bir matris oluşturacaksınız:")
        if satir_s is not None:
            for i in range(1, satir_s + 1):
                satir = simpledialog.askstring("Matris Satırı", f"{i}. Matris satırının elemanlarını birer boşluk bırakarak giriniz:")
                if satir is not None:
                    satir = list(map(int, satir.split()))
                    matris.append(satir)

    mat1 = []
    mat2 = []

    mat_al(mat1)
    mat_al(mat2)
    mat_2 = list(zip(*mat2))

    def mat_carp(mat1, mat_2):
        carpim = []
        for satir in mat1:
            carpim_satiri = []
            for sutun in mat_2:
                mat_carp_sonucu = sum(a * b for a, b in zip(satir, sutun))
                carpim_satiri.append(mat_carp_sonucu)
            carpim.append(carpim_satiri)
        return carpim

    sonuc = mat_carp(mat1, mat_2)
    sonuc_pencere("Matrix Çarpımı Sonuç", sonuc)

def kelime_frekansi():
    dosya_adi = simpledialog.askstring("Dosya İsmi", "Dosya ismini sonunda '.txt' ile giriniz (örn: dosya.txt):")
    if dosya_adi is not None:
        with open(dosya_adi, 'r') as dosya:
            metin = dosya.read().split()

        def hesap(kelime_frek, kelime):
            kelime_frek[kelime] = kelime_frek.get(kelime, 0) + 1
            return kelime_frek

        kelime_frek = reduce(hesap, metin, {})

        sonuc = "\n".join([f"{kelime}: {frekans}" for kelime, frekans in kelime_frek.items()])
        sonuc_pencere("Kelime Frekansı Sonuç", sonuc)

def en_kucuk_deger():
    liste = simpledialog.askstring("Liste", "Liste değerlerini aralarında birer boşluk olacak şekilde giriniz:")
    if liste is not None:
        liste = list(map(int, liste.split()))
        def ekd_islem(liste, kucuk=float('inf'), sayac=0):
            if sayac == len(liste):
                sonuc_pencere("En Küçük Değer Sonuç", kucuk)
            else:
                if liste[sayac] < kucuk:
                    kucuk = liste[sayac]
                ekd_islem(liste, kucuk, sayac + 1)

        ekd_islem(liste)

def karekok():
    n = simpledialog.askfloat("Karekök Hesaplama", "Karekök değeri bulunacak sayıyı giriniz:")
    x0 = simpledialog.askfloat("Karekök Hesaplama", "Tahmini sonuç giriniz:")

    def kk_islem(n, x0, tol=10 ** (-10), maxiter=10, iterasyon=1):
        x0 = 0.5 * (x0 + n / x0)
        hata = abs(x0 ** 2 - n)
        if hata < tol:
            sonuc_pencere("Karekök Hesaplama Sonuç", x0)
        elif iterasyon > maxiter:
            sonuc_pencere("Karekök Hesaplama Sonuç", "10 iterasyonda sonuca ulaşılamadı. 'hata' veya 'maxiter' değerlerini değiştirin.")
        else:
            kk_islem(n, x0, tol, maxiter, iterasyon + 1)

    kk_islem(n, x0)

def ebob_bul():
    sayi1 = simpledialog.askinteger("EBOB Hesaplama", "Büyük sayıyı giriniz:")
    sayi2 = simpledialog.askinteger("EBOB Hesaplama", "Küçük sayıyı giriniz:")

    def eb_islem(sayi1, sayi2):
        if sayi2 == 0:
            sonuc_pencere("EBOB Hesaplama Sonuç", sayi1)
        else:
            bolum = sayi1 % sayi2
            eb_islem(sayi2, bolum)

    eb_islem(sayi1, sayi2)

def asal_veya_degil():
    n = simpledialog.askinteger("Asal Sayı Sorgulama", "Sorgulamak istenilen pozitif tam sayıyı giriniz:")

    def avd_islem(n, sayac=0, tekrar=1):
        if n == 1:
            sonuc_pencere("Asal Sayı Sorgulama Sonuç", False)
        if sayac > 2:
            sonuc_pencere("Asal Sayı Sorgulama Sonuç", False)
        elif tekrar > n:
            sonuc_pencere("Asal Sayı Sorgulama Sonuç", True)
        else:
            bolum = n % tekrar
            if bolum == 0:
                sayac += 1
            tekrar += 1
            avd_islem(n, sayac, tekrar)

    avd_islem(n)

def fibonacci():
    n = simpledialog.askinteger("Fibonacci Hesaplama", "Kaçıncı Fibonacci değerini istiyorsunuz:")
    k = 1
    fibk = 1
    fibk1 = 0

    def hizlandirici(n, k, fibk, fibk1):
        if n == k:
            sonuc_pencere("Fibonacci Hesaplama Sonuç", fibk)
        else:
            k += 1
            fib_k = fibk + fibk1
            fib_k1 = fibk
            hizlandirici(n, k, fib_k, fib_k1)

    hizlandirici(n, k, fibk, fibk1)

def sonuc_pencere(baslik, sonuc):
    sonuc_pencere = tk.Toplevel(pencere)
    sonuc_pencere.title(baslik)
    sonuc_label = tk.Label(sonuc_pencere, text=sonuc)
    sonuc_label.pack()

pencere = tk.Tk()
pencere.title("Console Menü")

menubar = tk.Menu(pencere)
pencere.config(menu=menubar)

menubar.add_command(label="K. Küçük Hesapla", command=k_kucuk)
menubar.add_command(label="En Yakın Sayı Çifti", command=en_yakin_sayi_cifti)
menubar.add_command(label="Tekrar Eden Elemanlar", command=tekrar_eden_elemanlar)
menubar.add_command(label="Matrix Çarpımı", command=matrix_carpimi)
menubar.add_command(label="Kelime Frekansı", command=kelime_frekansi)
menubar.add_command(label="En Küçük Değer", command=en_kucuk_deger)
menubar.add_command(label="Karekök Hesapla", command=karekok)
menubar.add_command(label="En Büyük Ortak Bölen", command=ebob_bul)
menubar.add_command(label="Asal Mı Değil Mi?", command=asal_veya_degil)
menubar.add_command(label="Fibonacci Sayısı", command=fibonacci)
menubar.add_command(label="Çıkış", command=pencere.quit)
pencere.mainloop()
