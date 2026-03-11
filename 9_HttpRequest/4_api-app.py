import requests

url = "http://api.weatherapi.com/v1/current.json"
key = "3f5e75b5e0f34401901104000260903"

print("--- Hava Durumu Uygulamasına Hoş Geldiniz ---")
print("(Çıkış yapmak için '0' tuşuna basınız)\n")

while True:
    konum = input("Hangi şehrin hava durumunu öğrenmek istiyorsun?: ")

    # Çıkış kontrolü
    if konum == "0":
        print("Uygulamadan çıkılıyor. İyi günler!")
        break

    try:
        response = requests.get(url, params={
            "key" : key,
            "q" : konum,
            "lang": "tr"
        })
        
        # HTTP hatalarını kontrol et (Yanlış şehir girilirse vb.)
        response.raise_for_status()
        
        sonuc = response.json()
        
        sehir = sonuc["location"]["name"]
        havadurumu = sonuc["current"]["temp_c"] 
        text = sonuc["current"]["condition"]["text"]
        saat = sonuc["location"]["localtime"]

        print(f"\n=> '{sehir}' şehrinde sıcaklık {havadurumu}°C ve hava '{text}'.")
        print(f"Son güncelleme: {saat}\n" + "-"*30)

    except Exception:
        print("Üzgünüm, bu şehir bulunamadı veya bir hata oluştu. Lütfen tekrar deneyin.\n")