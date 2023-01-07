#KÜTÜPHANELER
import datetime # uygulamanın açıldığı tarihi görmek için
import win32gui # uygulama adlarını görmek için
import time # sayaç tutmak için

dosya = open("Geçmiş.txt", "a", encoding='utf-8')
dosya.write ("\t========GEÇMİŞ========\n\n")
dosya.close()

def aktifPencereBaslik(): # 'aktifPencereBaslik' adında fonksiyon oluşturuldu 
    return win32gui.GetWindowText(win32gui.GetForegroundWindow()) # açılan pencerenin adını döndürür

enSonBaslik = "" # bu değişkeni aşağıda açıklayacağım

while True: # program döngüde
        
  time.sleep(0.01) # program işlemcinin içinden geçmemesi için 0.01 zaman bekliyor
  Baslik = aktifPencereBaslik() # 'aktifPencereBaslik' fonksiyonu 'Baslik' değişkenine aktarıldı
  Tarih = datetime.datetime.now() # tarih zaman değişkeni
  
  if Baslik != enSonBaslik: # eğer başlık sonbaslık değilse : 
        print(Baslik) # değişken ekrana yazdırılır
        enSonBaslik = Baslik # ensonbaşlık başlık değişkenine eklendi
  
        dosya = open("Geçmiş.txt", "a", encoding='utf-8') # 'Geçmiş.txt' dosyası oluşturdu
        dosya.write (f"[{Tarih.strftime('%x %X')}] {Baslik}\n") # uygulamaları adlarını ve açıldığı tarihler yazıldı
        dosya.close # işi bitince kapattı 
