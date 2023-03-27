# PYTEST DECORATOR
 ## @pytest.mark.xfail
* testin fail olduğunu bildiğimiz yerlerde kullanırız onu fail olarak değil xfail olarak görürüz
***
## @pytest.mark.skip
* testi atlamamızı sağlar
* reason neden atlandığı belirtilir
***
## @pytest.mark.skipif()
* şarta göre testi atlamamızı sağlayan decorator
* condition boolean olmalı 
* reason belirtilir
* şarta uyarsa atlar yoksa atlamaz
***
## @pytest.mark.smoke
* sistemin tam anlamıyla çalıştığını göstermez fakat önemli fonksiyonların çalışıp çalışmadiğın anlamak amacıyla yapılır

NOT: Custom mark'ta oluşturup testleri gruplarız.

## @pytest.fixture()
* bir teste başlatmadan yapılacak fonksiyonu seçerken kullanırız testimize ortak olan şeyleri önceden tek fonsiyon altında toplayıp fonksiyonu bağlayarak zaman kazanırız
* örneğin driver oluşturmada kullanacağız
