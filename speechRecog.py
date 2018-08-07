import speech_recognition as sr

def main():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print ('Say Something!')
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print (text)

    except():
        pass
while True:
    main()
