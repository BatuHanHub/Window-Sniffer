#KÜTÜPHANELER
import os # terminali temizlemek için
import win32gui # uygulama adlarını görmek için
import time # sayaç tutmak için

def aktifPencereBaslik(): # 'aktifPencereBaslik' adında fonksiyon oluşturuldu 
    return win32gui.GetWindowText(win32gui.GetForegroundWindow()) # açılan pencerenin adını döndürür

while True: # program döngüde
    
  Baslik = aktifPencereBaslik() # 'Baslik' değişkeni 'aktifPencereBaslik' değişkenine aktarıldı
  
  print(Baslik) # ekrana pencereyi yazdı
  time.sleep(1.5) # 1.5 saniye bekledi
  os.system('cls') # terminali temizledi
  
  dosya = open("Geçmiş.txt", "a", encoding='utf-8') # 'Geçmiş.txt' dosyası oluşturdu
  dosya.write (f"{Baslik}\n") # uygulamaları yazdı
  dosya.close # işi bitince kapattı 
