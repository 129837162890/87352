import speech_recognition as sr
import random
from colorama import Fore, init
init(autoreset=True)
import openai
import simplejson as json
from tts_api import speak
import server
import Weather
import dateTime_api
import time
import trafficdata_api
import yazitura_api
import datetime

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
                print(Fore.RED + "SB-9500: " + Fore.WHITE + "Anlamadım, dinlemeye devam ediyorum. (system.py)")
            except sr.RequestError:
                speak("Sistem çalışmıyor.")
                print(Fore.RED + "- SISTEM CALISMIYOR - ")
            return voice
        
    def creditCardSave():
            cardType = ""
            if "kredi kartı" in voice:
                cardType = "Kredi Kartı"
                print(Fore.CYAN + "Kart tipi: " + Fore.WHITE + "Kredi Kartı")
            if "banka kartı" in voice:
                cardType = "Banka Kartı"
                print(Fore.CYAN + "Kart tipi: " + Fore.WHITE + "Banka Kartı")
            cardNumber = ""
            cardName = ""
            cardCvv = ""
            cardDate = ""
            Note = ""
            speak(f"Eklemek istediğiniz {cardType}'nın adı ne olsun?")
            cardNameUser = record("")
            cardNameUser = cardNameUser.lower()
            print("-"*75)
            print(Fore.YELLOW + "Kart adı: " + cardNameUser)
            speak(f"Kartınızın adı {cardNameUser} olarak ayarlanacak, onaylıyor musunuz?")
            onay1 = record("")
            onay1 = onay1.lower()
            print(Fore.CYAN + "Onay durumu [1] >> " + onay1)
            if "evet" in onay1 or "onaylıyorum" in onay1 or "yes" in onay1 or "kabul ediyorum" in onay1 or "onay veriyorum" in onay1:
                cardName = cardNameUser
                speak(f"Tamam, kartının adını {cardName} olarak kaydettim. Şimdi ise kartının üzerinde yazan numara nedir?")
                cardNumberUser = record("")
                print(Fore.CYAN + "Kart numarası: " + cardNumberUser)
                prompt = f"Bu {cardNumberUser} sayının türkçe okunuşu nedir? (NOT: sadece türkçe okunuşu düz yaz başka bir şeyler yazma ve açıklama yapma.)"
                response = openai.Completion.create(
                    engine="text-davinci-003",
                    prompt=prompt,
                    max_tokens=3000
                )
                cardResp = response.choices[0].text.strip()
                if "?" in cardResp:
                    cardResp = cardResp.replace("?", "")
                speak(f"Kartınızın numarasını okuyorum sizde lütfen doğruluğunu kontrol edin. Kart numaranız, {cardResp} bu kart numarası için onay veriyor musunuz?")
                onay2 = record("")
                onay2 = onay2.lower()
                print(Fore.CYAN + "Onay durumu [2] >> {}".format(onay2))
                if "evet" in onay2 or "onaylıyorum" in onay2 or "yes" in onay2 or "kabul ediyorum" in onay2 or "onay veriyorum" in onay2:
                    cardNumber = cardNumberUser
                    speak("Tamam, kartının numarasını kaydettim. Şimdi ise bana kartının Arka yüzünde yer alan 3 haneli güvenlik kodunu vermeni istiyorum.")
                    cardCvvUser = record("")
                    cardCvvUser = cardCvvUser.lower()
                    print(Fore.CYAN + "Kart CVV: " + cardCvvUser)
                    speak(f"Kartın güvenlik kodunu {cardCvvUser} olarak kaydettim, onaylıyor musunuz?")
                    onay3 = record("")
                    onay3 = onay3.lower()
                    print(Fore.CYAN + "Onay durumu [3] >> " + onay3)
                    if "evet" in onay3 or "onaylıyorum" in onay3 or "yes" in onay3 or "kabul ediyorum" in onay3 or "onay veriyorum" in onay3:
                        cardCvv = cardCvvUser
                        speak("Tamam, kartının güvenlik kodunuda kaydettiğimize göre şimdi sıra kart son kullanma tarihinde. Lütfen bana kartınızın üzerinde yazan son kullanma tarihininin sadece ayını verir misiniz?")
                        cardDateUser = record("")
                        print(Fore.CYAN + "Kart son kullanma tarihi [ay]: " + cardDateUser)
                        speak(f"Kartınızın son kullanma tarihininin ay'ı, {cardDateUser} olarak kayıt ettim, onaylıyor musunuz?")
                        onay4 = record("")
                        onay4 = onay4.lower()
                        if "evet" in onay4 or "onaylıyorum" in onay4 or "yes" in onay4 or "kabul ediyorum" in onay4 or "onay veriyorum" in onay4:
                            speak("Peki şimdi son kullanma tarihinin yılı nedir?")
                            cardDateUser2 = record("")
                            cardDate1 = cardDateUser # ay
                            cardDate2 = cardDateUser2 # yıl
                            cardDateUser3 = cardDate1 + "/" + cardDate2
                            cardDate = cardDateUser3
                            speak(f"Tamam, kartınızın son kullanma tarihini {cardDate} olarak kayıt ettim.")
                            time.sleep(1)
                            speak("Artık tüm kart bilgilerinizi ayarladık, şimdi bu karta bir not eklemek ister misiniz?")
                            onay5 = record("")
                            onay5 = onay5.lower()
                            print(Fore.CYAN + "Not eklemek istiyor musunuz: " + onay5)
                            if "evet" in onay5 or "elbette" in onay5 or "ekle" in onay5 or "ekleyelim" in onay5 or "tabii ki" in onay5 or "tabi ki" in onay5 or "olur" in onay5:
                                speak("Tamam o zaman, şimdi istediğiniz notu söyleyin?")
                                noteUser = record("")
                                print(Fore.CYAN + "Kart notu >> " + noteUser)
                                speak(f"Notunuzu, {noteUser} olarak kayıt ediyorum onaylıyor musunuz?")
                                onay6 = record("")
                                onay6 = onay6.lower()
                                print(Fore.CYAN + "Onay durumu [6] >> " + onay6)
                                if "evet" in onay6 or "onaylıyorum" in onay6 or "yes" in onay6 or "kabul ediyorum" in onay6 or "onay veriyorum" in onay6: 
                                     Note = noteUser
                                     cardData = {
                                         "cardType":cardType,
                                         "cardName":cardName,
                                         "cardNumber":cardNumber,
                                         "cardDate":cardDate,
                                         "cardCvv":cardCvv,
                                         "Note":Note,
                                         "status":"true"
                                     }
                                     with open("Json/creditcard.json", "w") as fff:
                                         json.dump(cardData, fff)
                                     speak("Tebrikler, artık tüm kart bilgileriniz ve notunuz kaydedildi.")
                                     server.listen_for_trigger()
                                else:
                                    Note = noteUser
                                    cardData = {
                                         "cardType":cardType,
                                         "cardName":cardName,
                                         "cardNumber":cardNumber,
                                         "cardDate":cardDate,
                                         "cardCvv":cardCvv,
                                         "Note":Note,
                                         "status":"true"
                                     }
                                    with open("Json/creditcard.json", "w") as fff:
                                         json.dump(cardData, fff)
                                    speak("Notunuz kaydedilmedi fakat artık tüm kart bilgileriniz kaydedildi.")
                                    server.listen_for_trigger() 
                            else:
                                cardData = {
                                         "cardType":cardType,
                                         "cardName":cardName,
                                         "cardNumber":cardNumber,
                                         "cardDate":cardDate,
                                         "cardCvv":cardCvv,
                                         "Note":Note,
                                         "status":"true"
                                     }
                                with open("Json/creditcard.json", "w") as fff:
                                    json.dump(cardData, fff)
                                speak("Tebrikler, artık tüm kart bilgileriniz sisteme kayıt edildi.")
                                server.listen_for_trigger()
                        else:
                            speak("Tamam, işlemleri iptal ediyorum.")
                            server.listen_for_trigger()
                    else:
                        speak("Tamam, işlemleri iptal ediyorum.")
                        server.listen_for_trigger()
                else:
                    speak("Tamam, işlemleri iptal ediyorum.")
                    server.listen_for_trigger()    
            else:
                speak("Kart kaydetme işlemi onay verilmediği için iptal edildi.")
                server.listen_for_trigger()

    def response(voice):
        if "Hava durumu" in voice or "hava durumu" in voice:
            Weather.StartHava()
            server.listen_for_trigger()
            
        if "bugün ayın kaçı" in voice or "bugün ayın hangi günü" in voice or "bugün ayın kaçıncı günü" in voice:
            todayy = datetime.date.today()
            month_day = todayy.day
            print(Fore.CYAN + "Bugün ayın {}. günü".format(month_day))
            speak(f"Bugün ayın {month_day}. günü.")
            server.listen_for_trigger()
            
        if "şuan hangi aydayız" in voice or "şuan hangi ay içerisindeyiz" in voice or "hangi aydayız" in voice:
            today2 = datetime.date.today()
            month_day2 = today2.month
            print(Fore.CYAN + "Şuanda {} ayındayız.".format(month_day2))
            month = ""
            if month_day2 == 1:
                month = "Ocak"
            if month_day2 == 2:
                month = "Şubat"
            if month_day2 == 3:
                month = "Mart"
            if month_day2 == 4:
                month = "Nisan"
            if month_day2 == 5:
                month = "Mayıs"
            if month_day2 == 6:
                month = "Haziran"
            if month_day2 == 7:
                month = "Temmuz"
            if month_day2 == 8:
                month = "Ağustos"
            if month_day2 == 9:
                month = "Eylül"
            if month_day2 == 10:
                month = "Ekim"
            if month_day2 == 11:
                month = "Kasım"
            if month_day2 == 12:
                month = "Aralık"
            
            speak(f"Şuanda {month} ayındayız.")
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
            
        if voice == "adın ne" or voice == "Adın ne" or voice == "ismin ne" or voice == "ismin ne" or voice == "adın nedir" or voice == "Adın nedir" or voice == "İsmin nedir" or voice == "ismin nedir" or "adın ne" in voice or "Adın ne" in voice or "ismin ne" in voice or "İsmin ne" in voice or "adın nedir" in voice or "Adın nedir" in voice:
            speak("Benim adım klasik olarak sadece Yapay Zeka fakat ben Salih Baştanın üretimi olan SB 9500 numaralı yapay zeka teknolojisine sahip robotuyum.")
            server.listen_for_trigger()
            
        if "yazı tura at" in voice or "Yazı tura at" in voice or "Yazı Tura at" in voice or "yazı mı tura mı" in voice or "Yazı mı tura mı" in voice or "Yazı mı Tura mı" in voice:
            yazitura_api.yaziandtura()
            # Server'a kendi içerisinde gidiyor.
            
        if voice == "müzik aç" or voice == "Müzik aç" or voice == "şarkı aç" or voice == "Şarkı aç":
            speak("Hangi müziği açmamı istiyorsunuz?")
            musicUser = record("")
            print(Fore.CYAN + "Seçilen müzik: " + Fore.WHITE + musicUser)
            speak("{} adı altındaki müziği şuanda oynatamıyorum.".format(musicUser))
            server.listen_for_trigger()
            
        if "kredi kartı kaydet" in voice or "banka kartı kaydet" in voice or "kredi kartı kayıt et" in voice or "banka kartı kayıt et" in voice or "kredi kartı ekle" in voice or "banka kartı ekle" in voice or "kredi kartı bilgilerimi kaydet" in voice or "banka kartı bilgilerimi kaydet" in voice or "kredi kartı bilgilerimi kayıt et" in voice or "banka kartı bilgilerimi kayıt et" in voice or "banka kartımı kaydet" in voice or "kredi kartımı kaydet" in voice:
            creditCardSave()
            server.listen_for_trigger()
                
        if "kayıtlı kartları sorgula" in voice or "kayıtlı kartlarımı sorgula" in voice or "kayıtlı banka kartımı sorgula" in voice or "kayıtlı kredi kartımı sorgula" in voice or "kayıtlı kartlarımı sorgula" in voice or "kayıtlı kartımı sorgula" in voice:
            speak(f"Senin için şuan kayıtlı kartının bilgisini araştırıyorum.")
            with open("Json/creditcard.json", "r", encoding="utf-8") as ff:
                cardData = json.load(ff)
            time.sleep(1)
            
            if cardData["status"] == "true":
                print(Fore.GREEN + "- Kart Bulundu -")
                print("-"*75)
                print(Fore.GREEN + "Kart tipi: " + cardData["cardType"])
                print(Fore.GREEN + "Kart adı: " + cardData["cardName"])
                print(Fore.GREEN + "Kart numarası: " + cardData["cardNumber"])
                print(Fore.GREEN + "Kart skt: " + cardData["cardDate"])
                print(Fore.GREEN + "Kart CVV: " + cardData["cardCvv"])
                print(Fore.GREEN + "Kart notu: " + cardData["Note"])
                print(Fore.GREEN + "Durum: " + cardData["status"])
                print("-"*75)
                speak(f"Kayıtlı kartının bilgileri şunlardır. Kart tipi {cardData['cardType']} , Kart adı {cardData['cardName']} , Kart numarası {cardData['cardNumber']} , Kartın son kullanma tarihi {cardData['cardDate']} , Kartın güvenlik kodu {cardData['cardCvv']} , Kartın kullanıcı notu {cardData['Note']}")
                server.listen_for_trigger()
                
            else:
                print(Fore.RED + "- Kart Bulunamadı -")
                speak("Şuan hiç kayıtlı kartın bulunmuyor, Yeni bir tane kayıt etmek ister misin?")  
                onay01 = record("")
                onay01 = onay01.lower()
                if "evet" in onay01 or "elbette" in onay01 or "tabi" in onay01 or "tabii" in onay01 or "kayıt edelim" in onay01 or "kaydedelim" in onay01 or "olur" in onay01:
                    creditCardSave()
                    server.listen_for_trigger()
                else:
                    speak("Tamam, yeni bir kart kaydetmeyeceğim. Bana tekrar ulaşmak istediğinizde lütfen Hey Yapay Zeka diyin.")
                    server.listen_for_trigger()

        if voice == "kapan" or "sistemi kapat" in voice or "Sistemi kapat" in voice or "Robotu kapat" in voice or "robotu kapat" in voice:
            exit_log = [
                "Tamam sistemi kapatıyorum, şimdilik hoşçakalın.",
                "Tamam, sistemi kapatıyorum.",
                "Tekrar görüşmek üzere, sistemi kapatıyorum.",
                "Sistemi kapatıyorum, iyi günler."
            ]
            exit_log2 = random.choice(exit_log)
            speak(exit_log2)
            exit()

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
        voice = voice.lower()
        print(Fore.YELLOW + "{}: ".format(userInfoTue["username"]) + Fore.WHITE + "{}".format(voice))
        response(voice)
