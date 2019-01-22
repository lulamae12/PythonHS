import speech_recognition as sr

def main():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print ('Say Something!')
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print (text)

<<<<<<< HEAD
    except(UnknownValueError):
=======
    except(Traceback):
>>>>>>> 3bc0978b3a1570864d07f00b0b957fa701473452
        pass

while True:
    main()
