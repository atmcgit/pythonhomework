from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By  # daha basit arama için
# driver = webdriver.Chrome(ChromeDriverManager().install())   otomatik web driver tanıtma

driver = webdriver.Chrome("C:\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.google.com/")
sleep(5)
input = driver.find_element(By.NAME, "q")    # name'a göre arama
input.send_keys("Kodlama.io")
searchButton = driver.find_element(By.NAME, "btnK")
sleep(2)
searchButton.click()
sleep(2)
firstResult = driver.find_element(By.XPATH,"/html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div[1]/a")
firstResult.click()
listOfCourses= driver.find_elements(By.CLASS_NAME,"course-listing")
print(f"Kodlamaio sitesinde şu anda {len(listOfCourses)} adet kurs var.")
# sleep(10)
while True:
    continue

 # HTML LOCATORS
# full xpath
#  /html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div[1]/a
# xpath
#  //*[@id="rso"]/div[1]/div/div/div/div/div/div/div[1]/a

# data scraping 
# web scraping