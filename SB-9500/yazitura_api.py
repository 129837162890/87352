import time
from colorama import Fore,init
init(autoreset=True)
import random
from tts_api import speak
import server

def yaziandtura():

    print("-"*75)
    print(Fore.GREEN + "> Yazı - Tura <")
    print(Fore.YELLOW + "Yazı-Tura sonuçlanıyor...")
    speak("Yazı tura sonuçlanıyor.")
    print(Fore.CYAN + "Kalan süre: 3sn")
    time.sleep(1)
    print(Fore.CYAN + "Kalan süre: 2sn")
    time.sleep(1)
    print(Fore.CYAN + "Kalan süre: 1sn")
    time.sleep(1)

    yazi = False
    tura = False

    if yazi == True:
        print(Fore.GREEN + "Sonuç: " + Fore.WHITE + "Yazı")
        speak("Sonuç yazı olarak belirlendi.")
        server.listen_for_trigger()
    elif tura == True:
        print(Fore.GREEN + "Sonuç: " + Fore.WHITE + "Tura")
        speak("Sonuç tura olarak belirlendi.")
        server.listen_for_trigger()
    else:
        pass

    yazitura = [
        "Yazı",
        "Tura",
        "Yazı",
        "Tura",
        "Yazı",
        "Tura",
        "Yazı",
        "Tura",
        "Yazı",
        "Tura",
        "Yazı",
        "Tura",
        "Yazı",
        "Tura",
        "Yazı",
        "Tura",
        "Yazı",
        "Tura",
        "Yazı",
        "Tura"
    ]
    yazituraResult = random.choice(yazitura)
    print(Fore.GREEN + "Sonuç: " + Fore.WHITE + yazituraResult)
    speak("Sonuç {} olarak belirlendi.".format(yazituraResult))
    server.listen_for_trigger()
