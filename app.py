#KÜTÜPHANELER
import datetime # Tarih kütüphanesi
import win32gui # Başlık için kütüphane
import time # Zaman kütüphanesi

def aktifPencereBaslik(): # 'aktifPencereBaslik' adında fonksiyon oluşturuldu 
    return win32gui.GetWindowText(win32gui.GetForegroundWindow()) # Açılan pencerenin adını döndürür

enSonBaslik = "" # Bu değişken En son açılan pencereyi tutuyor

with open("log.txt", "a", encoding='utf-8') as dosya: # log.txt dosyası oluşturuldu
          dosya.write (f'Program {Tarih.strftime('%d/%m/%Y %H:%M:%S')} başladı.\n') # Program açıldığında 'Programı x/x/x/ y:y:y zamanında başladı' yazacak

while True: # Program döngüde
  time.sleep(0.01) # Program işlemciyi yormaması için 0.01 saniye bekliyor
  Baslik = aktifPencereBaslik() # 'aktifPencereBaslik' fonksiyonu 'Baslik' değişkenine aktarıldı
  Tarih = datetime.datetime.now() # Tarih değikeni zaman değişkenini tutuyor
  
  if Baslik != enSonBaslik: # eğer başlık sonbaslık değilse : 
        print(f"{Baslik} programı {Tarih.strftime('%d/%m/%Y %H:%M:%S')} zamanında başladı.\n") # Değişken ekrana yazdırılır
        enSonBaslik = Baslik # ensonbaşlık başlık değişkenine eklendi

        with open("log.txt", "a", encoding='utf-8') as dosya: # log.txt dosyası açıldı
          dosya.write (f"[{Tarih.strftime('%d.%m.%Y %H:%M:%S')}] {Baslik}\n") # [gün.hafta.yıl saat:dakika:saniye] program_adi 
