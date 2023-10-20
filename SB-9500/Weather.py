import re
import urllib.request
from tts_api import speak
import json

with open("Library_9500.json", "r", encoding="utf-8") as f:
    il = json.load(f)
    
ing_sehir = il["ing_il"]
tr_sehir = il["tr_il"]

def StartHava():
    url = "https://www.havadurumu15gunluk.net/havadurumu/{}-hava-durumu-15-gunluk.html".format(ing_sehir)
    site = urllib.request.urlopen(url).read().decode('utf-8')

    r_gunduz = '<td width="45">&nbsp;&nbsp;(-?\d+)°C</td>'
    r_gece = '<td width="45">&nbsp;(-?\d+)°C</td>'
    r_gun = '<td width="70" nowrap="nowrap">(.*)</td>'
    r_tarih = '<td width="75" nowrap="nowrap">(.*)</td>'
    r_aciklama = '<img src="/havadurumu/images/trans.gif" alt="{} Hava durumu 15 günlük" width="1" height="1" />(.*)</div>'.format(tr_sehir)

    comp_gunduz = re.compile(r_gunduz)
    comp_gece = re.compile(r_gece)
    comp_gun = re.compile(r_gun)
    comp_tarih = re.compile(r_tarih)
    comp_aciklama = re.compile(r_aciklama)

    gunduz = []
    gece = []
    gun = []
    tarih = []
    aciklama = []

    for i in re.findall(r_gunduz, site):
        gunduz.append(i)

    for i in re.findall(r_gece, site):
        gece.append(i)

    for i in re.findall(r_gun, site):
        gun.append(i)

    for i in re.findall(r_tarih, site):
        tarih.append(i)

    for i in re.findall(r_aciklama, site):
        aciklama.append(i)

    print("-" * 75)
    print("{} Hava Durumu".format(tr_sehir))
    print("-" * 75)
    for i in range(1):
        print("{} {} - Gündüz: {} °C\tGece: {} °C\t{}".format(tarih[i], gun[i], gunduz[i], gece[i], aciklama[i]))
        print("-" * 75)
        speak("{} ilinde bugün gündüz sıcaklığı {} derece. Gece sıcaklığı ise {} derece olması bekleniyor.".format(tr_sehir, gunduz[i], gece[i]))