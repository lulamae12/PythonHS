from gtts import gTTS
from playsound import playsound
import os


#pip install --user --force-reinstall --ignore-installed --no-binary :all: gTTS
def speak(words):
    tts = gTTS(text=str(words), lang='en')
    soundName = "TARSAudioTemp"
    soundName = soundName + ".mp3"
    tts.save(soundName)
    print(soundName)
    playsound(soundName)
