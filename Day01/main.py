
print("Kodlamaio")
baslik = "Taşıt Kredisi"
print(baslik)
baslik = "İhtiyaç Kredisi"
print(baslik)
# int, integer => tamsayı
vade = 36
ekVade = 6
# Metinsel ifade
vade2 = "36"

# float, decimal, double
aylikOdeme = 200.50

# bool, boolean => True veya False
yukselisteMi = True
yukselisteMi = False

# matematiksel operatörler

# +
print(5 + 5)
print(vade + 12)
print(vade + ekVade)
print(36 + 6)


# -
print(5 - 5)
print(vade - 12)
print(vade - ekVade)

# *
print(5 * 5)
print(vade * 12)
print(vade * ekVade)
print(10 * 10)

# /
print(5 / 5)
print(vade / 12)
print(vade / ekVade)
print(10 / 2)

yeniVade = vade / 2
fiyat = 100
indirimliFiyat = fiyat - 20

print(yeniVade)
print(indirimliFiyat)

# % => mod operator
print(10 % 2)
print(vade % 12)
print(vade % ekVade)
print(10 % 2)

# ** mantıksal operatörler
print(1 == 1)
print(1 == 2)

print(1 > 2)
print(1 < 2)
print(1 >= 1)

print(1 < 2)
print(3 > 1)
print(1 < 1)
print(1 <= 1)


print(1 != 1)
print(1 != 2)

# or and => veya

print(1 > 2 or 5 > 2)
print(1 > 2 and 5 > 2)
print(1 > 2 or 5 > 2 and 3 > 2)

print(1 > 2 and 5 > 2 and 3 > 2)

print(2 > 1 or 1 > 2 and 3 > 2)

# karar yapıları
# if else


sayi1 = 15
sayi2 = 15
# sayi1 sayi2'den büyükse ekrana sayi1 daha büyüktür yazdır
# condition şart

# indent
if sayi1 <= sayi2:
    print("Sayı 1 Sayı 2'den büyüktür.")
elif sayi1 == sayi2:
    print("İki sayı eşittir.")
# eğer if ve else if bloklarından hiç birine girmez ise
else:
    print("Sayı 1 Sayı 2'den küçüktür.")
# eğer herhangi bir bloğa girdiyse diğerlerine girmez


if sayi1<= sayi2:
    print("Sayi 1 sayi 2'den küçüktür")

#yeni bir yapıya geçtik alttaki ve üstteki if birbirinden bağımsız çalışır.

if sayi1==sayi2:
    print("İki sayi eşittir")
else:
    print("Sayi 1 Sayi 2'den büyüktür.")


print("Burası if bloğunun dışıdır.")

