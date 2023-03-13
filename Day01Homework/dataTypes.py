# Numerik veri tipleri => int,float,complex

# int : tam sayı veri tipi
a=1
print(type(a))
# float : ondalıklı sayı veri tipi
b=5.2
print(type(b))
# complex : karmaşık sayı (j) veri tipi ileri düzey matematiksel işlemlerde kullanılır

#----------------------------------------------------------------------------------#

# Text-metin veri tipi => String
# string : karakter ,string tanımlamak için "" veya '' işaretleri arasına yazılır.
name="Mustafa"
print(type(name))

#----------------------------------------------------------------------------------#

# boolean True veya False değer veren tip

isStudent = True
print(type(isStudent))

#----------------------------------------------------------------------------------#

# List : verilerin liste şeklinde siralandığı tip
# Liste elemanlarından her biri farklı veri tipinde olabilir.
# Soldan itibaren 0' dan başlayarak indeks numarası ile ulaşabiliriz
list1 = ["abc", 34, True, 40, "male"]
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#----------------------------------------------------------------------------------#

# Tuple : List'e benzer ancak farkı tuple içindeki elamanlar değiştirilemez,ekleme,güncelleme ve silineme yapılamaz.
# Tuple liste elemanları değiştirilemez ancak başka bir liste türüne çevrilerek güncelleme yapılabilir.
# Tuple liste elemanları parantez kullanılarak oluşturulur.

# ikiside tupledır fakat okunabilirlik açısından parantez kullanmakta fayda var
names = ('mustafa', 'muhammet', 'elif')
names = 'mustafa', 'muhammet', 'elif'
tuple1 = (1, "abc", True, 50)
print(type(tuple1))

thistuple = ("apple",)
print(type(thistuple))

# NOT a tuple
thistuple = ("apple")
print(type(thistuple))

#----------------------------------------------------------------------------------#

# Set : Pythonda set list'e benzer ancak set'de elemanlar sıralanamaz index alamazlar.Güncelleyemeyiz ancak yeni eleman ekleyebiliriz ve silebiliriz
# Pythonda set oluşturmak için süslü parantezler kullanırız.
fruits = {"banana", "grape", "cherry"}
thisset = {"apple", "banana", "cherry", True, 1, 2}

# Frozen Set : Kısıtlanmış Küme
frozen = frozenset({"apple", "banana", "cherry"})
print(type(frozen))
# içerisindeki elemanlarda ekleme,sileme,güncelleme gibi değişikler yapılmaz.

#----------------------------------------------------------------------------------#

# Dictionary : Python collection veri tiplerinden olan dictinory veri tipi key = value şeklinde sakladığımız veri tipidir.

thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(thisdict)
ogrenci = {"numara": "120", "ad": "Mustafa", "soyad": "Atmaca"}
print(ogrenci)
user = {"username": "mustafaatmaca", "password": "123456",
        "email": "info@mustafaatmaca.com", "phone": "05320000000"}
#key erişim
for i in user:
    print(i)
# value erişim
print("***************")
for i in user:
    print(user[i])
print("***************")
for i in user.values():
   print(i)
print("***************")
# her ikisi
for a,b in user.items():
    print(a,b)