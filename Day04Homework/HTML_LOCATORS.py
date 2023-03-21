# HTML,Hypertext Markup Language(Hiper Metin İşaretleme Dili) kelimelerinin kısaltmasıdır.
# Web sitelerini oluşturmak için kullandığımız kodlama dilidir.
# Diğer web teknolojileriyle birlikte kullanılır css,javascript gibi.



from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome("C:\chromedriver.exe")
driver.get("https://www.google.com/")


# 1- ID Locator
# Bir HTML öğesinin benzersiz kimliği olan "id" niteliğini kullanarak öğeyi bulur.
element = driver.find_element_by_id("my_id")

# 2- Class Locator 
# Bir HTML öğesinin "class" niteliğini kullanarak bir öğeyi bulur.
element = driver.find_element_by_class_name("my_class")

# 3- Name Locator
# Bir HTML öğesinin "name" niteliğini kullanarak bir öğeyi bulur.
element = driver.find_element_by_name("my_name")

# 4-Xpath Locator 
# Bir HTML öğesinin yolunu kullanarak bir öğeyi bulur.
element = driver.find_element_by_xpath("//div[@class='my_class']")

# 5-CSS Selector Locator 
# Bir HTML öğesinin stil özelliklerini kullanarak bir öğeyi bulur.
# 1.ID,2.Class,3.Attribute Values
element = driver.find_element_by_css_selector(".my_class")

