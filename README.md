# Selenium ile Otomatik Giriş Testi

Bu proje, Python ve Selenium kullanılarak hazırlanan basit bir otomatik giriş testidir. `https://the-internet.herokuapp.com/login` adresine kullanıcı adı ve şifre ile giriş yapılır, başarılı veya başarısız olup olmadığı kontrol edilir.

## Not
Bu proje Yazılım Mimarisi dersi ödevi kapsamında hazırlanmıştır.

## Özellikler
- Doğru kimlik bilgileri ile başarılı giriş testi
- Hatalı kimlik bilgileri ile hata mesajı kontrolü
- Otomatik tarayıcı başlatma ve kapatma

## Kullanım
```python
print(Login("tomsmith", "SuperSecretPassword!"))  # True döner
print(Login("tomsmith", "wrongpass"))             # False döner
```

## Gereksinimler
- Python
- Selenium
- Chrome ve ChromeDriver

