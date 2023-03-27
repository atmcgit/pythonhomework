# PYTEST DECORATOR
 ## @pytest.mark.xfail
* Testin fail olduğunu bildiğimiz yerlerde kullanırız onu fail olarak değil xfail olarak görürüz.

## @pytest.mark.skip
* Testi atlamamızı sağlar.
* Reason neden atlandığı belirtilir.

## @pytest.mark.skipif()
* Şarta göre testi atlamamızı sağlayan decorator.
* Condition boolean olmalı. 
* Reason belirtilir.
* Şarta uyarsa atlar yoksa atlamaz.

## @pytest.mark.smoke
* Sistemin tam anlamıyla çalıştığını göstermez fakat önemli fonksiyonların çalışıp çalışmadiğın anlamak amacıyla yapılır.

NOT: Custom mark'ta oluşturup testleri gruplarız.

## @pytest.fixture()
* Bir teste başlatmadan yapılacak fonksiyonu seçerken kullanırız testimize ortak olan şeyleri önceden tek fonsiyon altında toplayıp fonksiyonu bağlayarak zaman kazanırız.
* Örneğin driver oluşturmada kullanacağız.
