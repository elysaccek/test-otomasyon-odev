from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

def Login(username, password):
    # Chrome driver ayarları
    service = Service()
    driver = webdriver.Chrome(service=service)
    
    try:
        # Giriş sayfasına git
        driver.get("https://the-internet.herokuapp.com/login")
        time.sleep(5) # sayfa yüklenmesi için beklemek

        # Kullanıcı adı ve şifreyi gir
        driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(username)
        driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)

        # Giriş butonuna tıkla
        driver.find_element(By.XPATH, '//*[@id="login"]/button').click()
        time.sleep(5) # sayfa yüklenmesi için beklemek

        # URL kontrolü (başarılı giriş)
        if driver.current_url == "https://the-internet.herokuapp.com/secure":
            print("Giris Basarili")
            return True

        # Hata mesajı kontrolü (başarısız giriş)
        try:
            flash_message = driver.find_element(By.XPATH, '//*[@id="flash"]').text
            if "Your password is invalid!" in flash_message:
                print("Kullanici Adi veya Parola Hatali")
                return False
        except:
            print("Beklenmedik Hata Olustu")
            return False
        print("Beklenmedik Hata Olustu")
        return False

    finally:
        # Tarayıcıyı kapat
        driver.quit()

print(Login("tomsmith", "SuperSecretPassword!"))  # True döner
print(Login("tomsmith", "wrongpass"))             # False döner
