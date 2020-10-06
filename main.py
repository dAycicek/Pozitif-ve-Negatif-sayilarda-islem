print("Girdiğiniz negatif ve pozitif sayılar arasında işlemler yapılacak. Çıkış için 0 giriniz")
ptoplam = 0
ntoplam = 0
pi = 0
ni = 0
pmax = 0
pmin = 0
nmax= 0
nmin = 0
devam = True
pkontrol = False
nkontrol = False
while devam:
        sayi = input("Sayı: ")
        sayi = int(sayi)
        if sayi == 0:
            devam = False
        if sayi >= 1:
            if pkontrol == False:
                pmin = sayi
                pkontrol = True
            if sayi > pmax:
                pmax = sayi
            if sayi < pmin:
                pmin = sayi
            ptoplam = ptoplam + sayi
            pi = pi + 1
        if -1 >= sayi:
            if nkontrol == False:
                nmax = sayi
                nkontrol = True
            if sayi > nmax:
                nmax = sayi
            if sayi < nmin:
                nmin = sayi
            ntoplam = ntoplam + sayi
            ni = ni + 1
if pi == 0 and ni == 0:
    print("En büyük pozitif sayı: ", pmax)
    print("En büyük negatif sayı: ", nmax)
    print("En küçük pozitif sayı: ", pmin)
    print("En küçük negatif sayı: ", nmin)
else:
    if pi >= 1 and ni >= 1:
        print("Pozitif Sayıların Ortalaması: ", float(ptoplam / pi))
        print("En büyük pozitif sayı: ", pmax)
        print("En küçük pozitif sayı: ", pmin)
        print("Negatif Sayıların Ortalaması: ", float(ntoplam / ni))
        print("En büyük negatif sayı: ", nmax)
        print("En küçük negatif sayı: ", nmin)
    else:
        if pi == 0:
            print("Negatif Sayıların Ortalaması: ", float(ntoplam / ni))
            print("En büyük negatif sayı: ", nmax)
            print("En küçük negatif sayı: ", nmin)
        else:
            if ni == 0:
                print("Pozitif Sayıların Ortalaması: ", float(ptoplam / pi))
                print ("En büyük pozitif sayı: ", pmax)
                print ("En küçük pozitif sayı: ", pmin)