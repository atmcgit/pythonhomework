ogrenciListe = []
while True:
    print("---------------------------------")
    print("        1.Öğrenci Ekleme")
    print("        2.Öğrenci Silme")
    print("        3.Birden Fazla Öğrenci Ekleme")
    print("        4.Birden Fazla Öğrenci Silme")
    print("        5.Öğrenci Listesini Görüntüle")
    print("        6.Öğrenci Numarası Öğren")
    print("        7.Çıkıs Yap")
    print("---------------------------------")
    islemKodu = input("Yapılacak işlem kodunu giriniz :")


    def ogrenciEkle():
        ogrenciAdi = input("Eklemek istediğiniz kişinin adını giriniz :")
        ogrenciSoyadi = input("Eklemek istediğiniz kişinin soyadını giriniz :")
        ogrenciListe.append(ogrenciAdi + " " + ogrenciSoyadi)


    def ogrenciSil():
        ogrenciListe.remove(input("Silinecek öğrenci adını giriniz :"))


    def ogrencilerEkle():
        yeniListe = []
        kacOgrenci = input("Kaç öğrenci eklenecek :")
        kacOgrenci = int(kacOgrenci)
        for i in range(0, kacOgrenci):
            yeniListe.append((input(f"Girilecek {i + 1}. öğrencinin adı ve soyadı :")))
        print(yeniListe)
        ogrenciListe.extend(yeniListe)


    def ogrencilerSil():
        kacOgrenci = input("Kaç öğrenci silinecek :")
        kacOgrenci = int(kacOgrenci)
        for i in range(0, kacOgrenci):
            ogrenciListe.remove(input(f"Silinecek {i+1}. öğrenci adı ve soyadı :"))
            print(f"{i+1}. öğrenci silindi")
        print(ogrenciListe)

    def ogrenciListeGoruntule():
        a = 0
        for i in ogrenciListe:
            a += 1
            print(f" {a} - " + i)


    def ogrenciNoOgren():
        ogrenciAdi = input("Numarasını öğrenmek istediğiniz öğrencinin adını ve soyadını girin :")
        index = ogrenciListe.index(ogrenciAdi)
        print(f"Öğrenci Numarası : {index + 1}")


    if islemKodu == "1":
        ogrenciEkle()
        print("Öğrenci Eklendi")
        print(ogrenciListe)

    elif islemKodu == "2":
        ogrenciSil()
        print("Öğrenci Silindi")
    elif islemKodu == "3":
        ogrencilerEkle()
        print("Öğrenciler Eklendi")
    elif islemKodu == "4":
        ogrencilerSil()
        print("Öğrenciler Silindi")
    elif islemKodu == "5":
        ogrenciListeGoruntule()
        print("Öğrenci Listesi Görüntülendi")
    elif islemKodu == "6":
        ogrenciNoOgren()

    elif islemKodu == "7":
        print("Çıkış Yapıldı")
        break
    else:
        print("Geçerli İşlem Sayısı Giriniz!")
