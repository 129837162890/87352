import requests
import random
from playsound import playsound
import os
from colorama import Fore,init
init(autoreset=True)
import json

def speak(txt):
    
    with open("Library_9500.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    CHUNK_SIZE = 1024
    url = "https://api.elevenlabs.io/v1/text-to-speech/{}".format(data["tts_voice"])

    headers = {
    "Accept": "audio/mpeg",
    "Content-Type": "application/json",
    "xi-api-key": "{}".format(data["tts_api"])
    }

    data = {
    "text": "{}".format(txt),
    "model_id": "eleven_multilingual_v2",
    "voice_settings": {
        "stability": 0.5,
        "similarity_boost": 0.5
    }
    }

    response = requests.post(url, json=data, headers=headers)
    rand = random.randint(0, 10000)
    file_name = "audio-" + str(rand) + ".mp3"

    with open(file_name, 'wb') as f:
        for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
            if chunk:
                f.write(chunk)
                
    print(Fore.GREEN+"SB-9500: " + Fore.WHITE + "{}".format(txt))
    playsound(file_name)
    os.remove(file_name)