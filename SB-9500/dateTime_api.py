import datetime
from tts_api import speak

def now_time():

    # Şu anki saat ve tarihi al
    simdi = datetime.datetime.now()
    saat = simdi.hour
    dakika = simdi.minute

    # Saati ifade etmek için kullanılan isimleri tanımlayalım
    saatler = ["Geceyarısı", "Gece Bir", "Gece İki", "Gece Üç", "Sabah Dört", "Sabah Beş", "Akşam Altı", "Akşam Yedi", "Akşam Sekiz", "Akşam Dokuz", "Akşam On", "Akşam On Bir", "Öğlen On İki", "Öğlen Bir", "Öğlen İki", "Öğlen Üç", "Öğlen Dört", "Öğlen Beş", "Akşam Altı", "Akşam Yedi", "Akşam Sekiz", "Akşam Dokuz", "Akşam On", "Geceyarısı"]

    # Saati ekrana yazdır
    if 0 <= saat < 6:
        if saat == 0:
            saat = 24
        print(saatler[saat], f"{dakika:02d}")
        ek = ""
        if saatler[saat] == "Geceyarısı":
            ek = "nı"
        if saatler[saat] == "Gece Bir":
            ek = "i"
        if saatler[saat] == "Gece İki":
            ek = "yi"
        if saatler[saat] == "Gece Üç":
            ek = "ü"
        if saatler[saat] == "Sabah Dört":
            ek = "ü"
        if saatler[saat] == "Sabah Beş":
            ek = "i"
        if saatler[saat] == "Akşam Altı":
            ek = "yı"
        if saatler[saat] == "Akşam Yedi":
            ek = "yi"
        if saatler[saat] == "Akşam Sekiz":
            ek = "i"
        if saatler[saat] == "Akşam Dokuz":
            ek = "u"
        if saatler[saat] == "Akşam On":
            ek = "u"
        if saatler[saat] == "Akşam On Bir":
            ek = "i"
        if saatler[saat] == "Öğlen On İki":
            ek = "yi"
        if saatler[saat] == "Öğlen Bir":
            ek = "i"
        if saatler[saat] == "Öğlen İki":
            ek = "yi"
        if saatler[saat] == "Öğlen Üç":
            ek = "ü"
        if saatler[saat] == "Öğlen Dört":
            ek = "ü"
        if saatler[saat] == "Öğlen Beş":
            ek = "i"
        
        timetm = f"{saatler[saat]}{ek} {dakika:02d} geçiyor."
        speak("Şuanda saat, {}".format(timetm))
    else:
        print(saatler[saat], f"{dakika:02d}")
        ek = ""
        if saatler[saat] == "Geceyarısı":
            ek = "nı"
        if saatler[saat] == "Gece Bir":
            ek = "i"
        if saatler[saat] == "Gece İki":
            ek = "yi"
        if saatler[saat] == "Gece Üç":
            ek = "ü"
        if saatler[saat] == "Sabah Dört":
            ek = "ü"
        if saatler[saat] == "Sabah Beş":
            ek = "i"
        if saatler[saat] == "Akşam Altı":
            ek = "yı"
        if saatler[saat] == "Akşam Yedi":
            ek = "yi"
        if saatler[saat] == "Akşam Sekiz":
            ek = "i"
        if saatler[saat] == "Akşam Dokuz":
            ek = "u"
        if saatler[saat] == "Akşam On":
            ek = "u"
        if saatler[saat] == "Akşam On Bir":
            ek = "i"
        if saatler[saat] == "Öğlen On İki":
            ek = "yi"
        if saatler[saat] == "Öğlen Bir":
            ek = "i"
        if saatler[saat] == "Öğlen İki":
            ek = "yi"
        if saatler[saat] == "Öğlen Üç":
            ek = "ü"
        if saatler[saat] == "Öğlen Dört":
            ek = "ü"
        if saatler[saat] == "Öğlen Beş":
            ek = "i"
        
        timetm = f"{saatler[saat]}{ek} {dakika:02d} geçiyor."
        speak("Şuanda saat, {}".format(timetm))