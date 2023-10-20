import datetime
from tts_api import speak
import json

def trafficStatus():
    
    with open("Library_9500.json", "r", encoding="utf-8") as f:
        trafficData = json.load(f)

    date = datetime.datetime.now()

    trafficStatus = trafficData["derece"] # 5 < Düşük # 5 = Orta # 5 > Yoğun #

    statusString = ""
    if trafficStatus > 5:
        statusString = "Yoğun"
    if trafficStatus == 5:
        statusString = "Orta"
    if trafficStatus < 5:
        statusString = "Düşük"

    speak("{} {} Bölgesinde, saat {} itibariyle araç trafik yoğunluğu {} derecede devam ediyor.".format(trafficData["sehir"], trafficData["ilce"],date.strftime("%H:%M"), statusString))