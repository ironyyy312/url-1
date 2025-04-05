import time
import requests

# Sürekli açık kalması istenen URL
url = "https://streamelements.com/overlay/67f040c9051cb72361332329/nnF0dF3sMVnCWHAHCoC9IXVinvzNrL0rfGFRXwIdth8FKkny"

# İstek gönderme aralığı (saniye cinsinden), örneğin her 5 dakikada bir (300 saniye)
ping_interval = 300

while True:
    try:
        response = requests.get(url)
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] URL'ye istek gönderildi. Durum kodu: {response.status_code}")
    except Exception as e:
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Hata oluştu: {e}")
    time.sleep(ping_interval)
