#KÜTÜPHANELER
import datetime # uygulamanın açıldığı tarihi görmek için
import win32gui # uygulama adlarını görmek için
import time # sayaç tutmak için

def aktifPencereBaslik(): # 'aktifPencereBaslik' adında fonksiyon oluşturuldu 
    return win32gui.GetWindowText(win32gui.GetForegroundWindow()) # açılan pencerenin adını döndürür

enSonBaslik = "" # bu değişkeni aşağıda açıklayacağım

while True: # program döngüde
        
  time.sleep(0.01) # program işlemcinin içinden geçmemesi için 0.01 zaman bekliyor
  Baslik = aktifPencereBaslik() # 'aktifPencereBaslik' fonksiyonu 'Baslik' değişkenine aktarıldı
  Tarih = datetime.datetime.now() # tarih zaman değişkeni
  
  if Baslik != enSonBaslik: # eğer başlık sonbaslık değilse : 
        print(f"{Baslik} [{Tarih.strftime('%x %X')}]") # değişken ekrana yazdırılır
        enSonBaslik = Baslik # ensonbaşlık başlık değişkenine eklendi
  
        dosya = open("log.txt", "a", encoding='utf-8') # 'Geçmiş.txt' dosyası oluşturdu
        dosya.write (f"{Baslik} [{Tarih.strftime('%x %X')}] zamanında başladı.\n")
        dosya.close # işi bitince kapattı
