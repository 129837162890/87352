from gtts import gTTS
import speech_recognition as sr
import random
from colorama import Fore, init
init(autoreset=True)
import openai
import json
from tts_api import speak
import server
import Weather
import dateTime_api
import time
import trafficdata_api
import os

def detect():
    openai.api_key = "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"
    r = sr.Recognizer()

    def record(ask=False):
        with sr.Microphone() as source:
            if ask:
                speak(ask)
            audio = r.listen(source)
            voice = ""
            try:
                voice = r.recognize_google(audio, language='tr-TR')
            except sr.UnknownValueError:
                print("Err. Status: 1")
            except sr.RequestError:
                speak("Sistem çalışmıyor.")
            return voice

    def response(voice):
        if "Hava durumu" in voice or "hava durumu" in voice:
            Weather.StartHava()
            server.listen_for_trigger()

        if "trafik yoğunluğu" in voice or "Trafik durumu" in voice or "Trafik yoğunluğu" in voice or "trafik durumu" in voice:
            trafficdata_api.trafficStatus()
            server.listen_for_trigger()

        if "saat kaç" in voice or "Saat kaç" in voice:
            dateTime_api.now_time()
            server.listen_for_trigger()

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

        if "müslüman mısın" in voice or "Müslüman mısın" in voice:
            speak("Elhamdülillah müslümanım. Allah tüm müslüman kardeşlerimizden razı olsun.")
            server.listen_for_trigger()

        if "salih baştan" in voice or "Salih baştan" in voice or "Salih Baştan" in voice:
            speak("Salih abim hakkında herhangi bir yorum yapmam.")
            server.listen_for_trigger()

        if "kapan" in voice or "sistemi kapat" in voice or "Sistemi kapat" in voice:
            speak("Sistemi kapatıyorum.")
            os._exit(0)

        else:
            prompt = voice
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt,
                max_tokens=3000
            )
            sb9500resp = response.choices[0].text.strip()
            if "?" in sb9500resp:
                sb9500resp = sb9500resp.replace("?", "")
            speak(sb9500resp)
            server.listen_for_trigger()

    log_rnd = [
        "Efendim abi.",
        "Efendim abisi.",
        "Seni dinliyorum.",
        "Nasıl yardımcı olabilirim?",
        "Sizi dinlemeye devam ediyorum, ne istediğinizi söyleyin.",
        "Buyurun efendim, size nasıl yardımcı olabilirim?",
        "Buyurun efendim, size nasıl yardımcı olabilirim?"
    ]
    log_rnd2 = random.choice(log_rnd)
    speak(log_rnd2)  # Açılış kelimesi.
    print(Fore.CYAN + "SB-9500: " + Fore.WHITE + "{}".format(log_rnd2))
    print(Fore.CYAN + "- Soru sormak için şimdi konuşun -")

    with open("Json/User.json", "r", encoding="utf-8") as userInfoTueAc:
        userInfoTue = json.load(userInfoTueAc)

    while True:
        voice = record()
        print(Fore.YELLOW + "{}: ".format(userInfoTue["username"]) + Fore.WHITE + "{}".format(voice))
        response(voice)