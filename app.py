#KÜTÜPHANELER
import os # terminali temizlemek için
import win32gui # uygulama adlarını görmek için
import time # sayaç tutmak için
import datetime # uygulamanın açıldığı tarihi görmek için

# eğer programımızı Windows ve Linux/Unix için yazsaydık ve terminali temizlemek isteseydik şu kodu yazmamız gerekirdi;
'''
degisken = os.name

if degisken == "nt": # NT: Windows'un kullandığı çekirdek
    degisken2 = 'cls' # 'cls' Windows'da terminali temizler 
    os.system(degisken2) # Terminaliniz artık pırılpırıl :)

elif degisken == "poxit": # Linux/Unix (BSD,macOS vs...) için
    degisken = 'clear' # Linux/Unix'de terminali temizler 
    os.system(degisken2) # Terminaliniz artık pırılpırıl :)

# NOT: Ekranınıza sakın bal dökmeyin :D
'''

dosya = open("Geçmiş.txt", "a", encoding='utf-8')
dosya.write ("\t========GEÇMİŞ========\n\n")
dosya.close()

def aktifPencereBaslik(): # 'aktifPencereBaslik' adında fonksiyon oluşturuldu 
    return win32gui.GetWindowText(win32gui.GetForegroundWindow()) # açılan pencerenin adını döndürür

while True: # program döngüde
    
  Baslik = aktifPencereBaslik() # 'Baslik' değişkeni 'aktifPencereBaslik' değişkenine aktarıldı
  Tarih = datetime.datetime.now()
  
  print(Baslik) # ekrana pencereyi yazdı
  time.sleep(1.5) # 1.5 saniye bekledi
  os.system('cls') # terminali temizledi  NOT!:Sadece Windows'da çalışır Linux veya Unix(macOS, BSD vs...) sistemler için 'clear' kullanılır.
  
  dosya = open("Geçmiş.txt", "a", encoding='utf-8') # 'Geçmiş.txt' dosyası oluşturdu
  dosya.write (f"{Baslik} = ({Tarih.strftime('%H.%M.%S')})\n") # uygulamaları adlarını ve açıldığı tarihler yazıldı
  dosya.close # işi bitince kapattı 
