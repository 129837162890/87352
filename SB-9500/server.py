import speech_recognition as sr
from colorama import Fore,init
init(autoreset=True)
import openai
import simplejson as json
import system
from tts_api import speak
import time

def listen_for_trigger():
    
    with open("Json/User.json", "r", encoding="utf-8") as userInfoTueAc:
        userInfoTue = json.load(userInfoTueAc)

    r = sr.Recognizer() 
    openai.api_key = "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"

    def record(ask=False):
        with sr.Microphone() as source:
            if ask:
                speak(ask)
            audio = r.listen(source)
            voice = ""
            try:
                voice = r.recognize_google(audio, language='tr-TR')
            except sr.UnknownValueError:
                print(Fore.RED + "SB-9500: " + Fore.WHITE + "Dinlemeye devam ediyorum.")
            except sr.Recognizer():
                speak("Sistem çalışmıyor.")
                print(Fore.RED + "- SERVER CALISMIYOR - (server.py)")
            return voice

    def response(voice):
        if "Hey Yapay Zeka" in voice or "Hey Yapay zeka" in voice or "Hey yapay zeka" in voice or "hey yapay zeka" in voice:
            print(Fore.YELLOW + "{}: ".format(userInfoTue["username"]) + Fore.WHITE + "Hey Yapay Zeka")
            system.detect()
        if "kapan" in voice or "sistemi kapat" in voice or "Kapan" in voice or "Sistemi kapat" in voice:
            speak("Sistemi kapatıyorum.")
            exit()
        if "uyku modu" in voice or "Uyku modu" in voice or "Uyku Modu" in voice:
            speak("Kaç dakika boyunca uyumamı istiyorsunuz?")
            uyku = record()
            if "1" in uyku or "Bir" in uyku or "bir" in uyku:
                 speak("Tamam, bir dakika boyunca uyuyacağım.")
                 time.sleep(60)
                 speak("Bir dakika oldu, uyku modunu kapatıyorum.")
            if "2" in uyku or "İki" in uyku or "iki" in uyku:
                 speak("Tamam, iki dakika boyunca uyuyacağım.")
                 time.sleep(120)
                 speak("İki dakika oldu, uyku modunu kapatıyorum.")
            if "3" in uyku or "Üç" in uyku or "üç" in uyku:
                 speak("Tamam, üç dakika boyunca uyuyacağım.")
                 time.sleep(180)
                 speak("Üç dakika oldu, uyku modunu kapatıyorum.")
            if "4" in uyku or "Dört" in uyku or "dört" in uyku:
                 speak("Tamam, dört dakika boyunca uyuyacağım.")
                 time.sleep(240)
                 speak("Dört dakika oldu, uyku modunu kapatıyorum.")
            if "5" in uyku or "Beş" in uyku or "beş" in uyku:
                 speak("Tamam, bir dakika boyunca uyuyacağım.")
                 time.sleep(300)
                 speak("Bir dakika oldu, uyku modunu kapatıyorum.")
            if "6" in uyku or "Altı" in uyku or "altı" in uyku:
                 speak("Tamam, altı dakika boyunca uyuyacağım.")
                 time.sleep(360)
                 speak("Altı dakika oldu, uyku modunu kapatıyorum.")
            if "7" in uyku or "Yedi" in uyku or "yedi" in uyku:
                 speak("Tamam, yedi dakika boyunca uyuyacağım.")
                 time.sleep(420)
                 speak("Yedi dakika oldu, uyku modunu kapatıyorum.")
            if "8" in uyku or "Sekiz" in uyku or "sekiz" in uyku:
                 speak("Tamam, sekiz dakika boyunca uyuyacağım.")
                 time.sleep(480)
                 speak("Sekiz dakika oldu, uyku modunu kapatıyorum.")
            if "9" in uyku or "Dokuz" in uyku or "dokuz" in uyku:
                 speak("Tamam, dokuz dakika boyunca uyuyacağım.")
                 time.sleep(540)
                 speak("Dokuz dakika oldu, uyku modunu kapatıyorum.")
            if "10" in uyku or "On" in uyku or "on" in uyku:
                 speak("Tamam, on dakika boyunca uyuyacağım.")
                 time.sleep(600)
                 speak("on dakika oldu, uyku modunu kapatıyorum.")
            else:
                speak("Ben en fazla 10 dakika kadar uyuyabilirim, ve benim bir robot olup uykuya ihtiyacım olmadığını unutmayın.")
        
        else:
            pass

    print(Fore.CYAN + "Başlamak için 'Hey Yapay Zeka' diyebilirsiniz.")

    while True:
        voice = record()
        response(voice)
