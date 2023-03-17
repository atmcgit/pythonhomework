faiz = 1.59
vade = "36"
krediAdı = "İhtiyaç Kredisi"

print(type(faiz))
print(type(vade))
print(type(krediAdı))


print(int(vade)+12)
# print(int(krediAdi)) hatalı
faiz = str(faiz)
print(type(faiz))

vade = 30  # int(input("Lütfen isdeğiniz vade sayısını giriniz : "))
# kullanıcıdan alınan input defaul olarak string
print(type(vade))
vade = vade+12


# string interpolation

# Seçtiğiniz vade sonucu ortaya çıkan vade :
# print("Seçtiğiniz vade sonucu ortaya çıkan vade :" + vade)  => Hatalı
print("Seçtiğiniz vade sonucu ortaya çıkan vade :" + str(vade))
print("Seçtiğiniz vade sonucu ortaya çıkan vade :{}".format(vade))
# f-string
print(f"Seçtiğiniz vade sonucu ortaya çıkan vade: {vade} ")
ad = "Mustafa"  # input("İsim giriniz : ")
soyAd = "Atmaca"  # input("Soyad giriniz : ")
yaş = 22
print(f"Merhaba benim adım {ad} soyadım {soyAd} yaşım {yaş}")
print("Merhaba benim adım {} soyadım {} yaşım {}".format(ad, soyAd, yaş))
metin = f"Hoşgeldiniz {2+2}"
print(metin)

# listeler
# append()  Adds an element at the end of the list
# clear()   Removes all the elements from the list
# copy()    Returns a copy of the list
# count()   Returns the number of elements with the specified value
# extend()  Add the elements of a list (or any iterable), to the end of the current list
# index()   Returns the index of the first element with the specified value
# insert()  Adds an element at the specified position
# pop()     Removes the element at the specified position
# remove()  Removes the first item with the specified value
# reverse() Reverses the order of the list
# sort()    Sorts the list
# Dizi içerisine farklı türde elemanlar girilebilir
dizi = ["İhtiyaç Kredisi", 10, 5.2, True]

krediler = ["İhtiyaç Kredisi", "Taşıt Kredisi", "Konut Kredisi"]
print(type(krediler))
print(krediler[1])

print(len(krediler))  # length
krediler.append("Özel Kredi")
# listenin sonuna eleman ekler

print(krediler)

krediler.append("X Kredisi")

# print(krediler)

# krediler.pop()
# # index vermez isen son elemanı siler
print(krediler)

krediler.pop(0)

print(krediler)

krediler.append("Taşıt Kredisi")  # verilen bir değeri ekler
print(krediler)

krediler.remove("Taşıt Kredisi")

print(krediler)

krediler.extend(["Y Kredisi", "Z Kredisi"])
print(krediler)
krediler.insert(3, "Tarım Kredisi")  # belirtilen yere eleman ekler
print(krediler)
print(krediler.index("Tarım Kredisi"))  # belirtilen elamnın indexini verir
krediler.insert(3, "Tarım Kredisi")
krediler.sort()
print(krediler)
print(krediler.count("Tarım Kredisi"))


# döngüler for
# x içine verileri input ile de atayabiliriz
for i in range(10):
    print(i)
print("------------------")
for i in range(5, 10):
    print(i)
print("------------------")
for i in range(0, 51, 10):
    print(i)
print("------------------")
krediler = ["İhtiyaç Kredisi", "Taşıt Kredisi", "Konut Kredisi"]
for kredi in krediler:
    print(kredi)
print("------------------")
for kredi in range(len(krediler)):
    print(krediler[kredi])
print("------------------")
i = 0
l = 10

while i < 10:
    print("x")
    i += 1
print("y")
print("------------------")
while True:
    print("X")
    break
print("------------------")
krediler = ["İhtiyaç Kredisi", "Taşıt Kredisi", "Konut Kredisi"]
i = 0
while i < len(krediler):
    i += 1
    print(krediler[i])
    if krediler[i] == "Konut Kredisi":
        break


# fonksiyonlar

fiyat = 100
indirim = 20

# definition define


def calculate():
    print(100-20)


def calculateWithParams(fiyat, indirim):
    print(fiyat-indirim)


def sayHello(name):
    print(f"Merhaba {name} ")


calculate()
calculateWithParams(50, 10)
calculateWithParams(100, 30)
sayHello("Mustafa")
sayHello("Oğuzhan")
sayHello("Emre")

def calculatePrice(price,discount):
    print(price-discount)

def calculatePriceAndReturn(price, discount):
    return price - discount



print("------------------")
fonk1 = calculatePrice(100,50)
fonk2 = calculatePriceAndReturn(300,100)
print(fonk1)
print(fonk2)
print("------------------")