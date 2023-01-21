#KÜTÜPHANELER
import datetime # Tarih kütüphanesi
import win32gui # Başlık için kütüphane
import time # Zaman kütüphanesi

def aktifPencereBaslik(): # 'aktifPencereBaslik' adında fonksiyon oluşturuldu 
    return win32gui.GetWindowText(win32gui.GetForegroundWindow()) # Açılan pencerenin adını döndürür

enSonBaslik = "" # Bu değişken En son açılan pencereyi tutuyor

while True: # Program döngüde
  time.sleep(0.01) # Program işlemciyi yormaması için 0.01 saniye bekliyor
  Baslik = aktifPencereBaslik() # 'aktifPencereBaslik' fonksiyonu 'Baslik' değişkenine aktarıldı
  Tarih = datetime.datetime.now() # Tarih değikeni zaman değişkenini tutuyor
  
  if Baslik != enSonBaslik: # eğer başlık sonbaslık değilse : 
        print(f"- {Baslik} programı {Tarih.strftime('%x %X')} zamanında başladı.\n") # değişken ekrana yazdırılır
        enSonBaslik = Baslik # ensonbaşlık başlık değişkenine eklendi
  
        dosya = open("log.txt", "a", encoding='utf-8') # 'log.txt' dosyası oluşturdu
        dosya.write (f"- {Baslik} programı {Tarih.strftime('%x %X')} zamanında başladı.\n") 
        dosya.close # işi bitince kapattı
