class Matematik:
    def __init__(self, sayi1, sayi2):
        self.sayi1 = sayi1
        self.sayi2 = sayi2
        print("Matematik başladı (referansı oluştu)")

    def topla(self):
        return self.sayi1 + self.sayi2

    def cikar(self):
        return self.sayi1 - self.sayi2

    def bol(self):
        return self.sayi1 / self.sayi2

    def carp(self):
        return self.sayi1 * self.sayi2


matematik = Matematik(14, 7)
sonuc = matematik.topla()
print("Sonuç : " + str(sonuc))


class Istatistik(Matematik):
    def __init__(self, sayi1, sayi2):
        super().__init__(sayi1, sayi2) # =>super üst sınıfı temsil ediyor
    def varyansHesapla (self):
        return self.sayi1 * self.sayi2

# inheritance
istatistik = Istatistik(5,8)

    