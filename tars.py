import wolframalpha,wikipedia,datetime,os
from google_images_download import google_images_download
from questionTypes import *
from PIL import Image
from tarsConfig import *
from gtts import gTTS
from playsound import playsound



appID = "P6Y6GV-H9Y7RETQ37"
tars = wolframalpha.Client(appID)

def firstTimeSetup():

    setupFile = open("TarsSetup.txt","r+")
    configured = setupFile.readline()
    print(configured)
    if configured == "1":
        setupFile.close()
    else:
        configSetup()
        setupFile = open("TarsSetup.txt", "w")
        setupFile.write("1")

def getCurrentTime():#get time so i dont need to use api
    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute
    period = "AM"
    if hour > 12:#get rid of millitary time
        hour = hour - 12
        period = "PM"
    if minute < 9:
        minute = "0" + str(minute)#add 0
    print("TARS >>> The Current Time is,",hour,":",minute,period)

def imageSearch(term):
    searchCleanupList = [" show "," me "," picture "," pictures "]

    term = term.replace("show me pictures of a ","")
    term = term.replace("show me pictures of ","")
    term = term.replace("show me a ","")
    term = term.replace("show me an ","")
    term = term.replace("show a picture of ","")

    term = term.strip()#clean it up
#CLEANUP
    response = google_images_download.googleimagesdownload()
    arguments = {"keywords":term,"limit":1,"print_urls":True,"output_directory":"TARSPics","size":"large","format":"jpg"}#download to dir tarspics
    imagePath = response.download(arguments)
    imagePath = imagePath.pop(term)
#CLEANUP
    imagePathStr = str(imagePath)
    imagePathStr = imagePathStr.replace("\\\\","\\")
    imagePathStr = imagePathStr.replace("['","")
    imagePathStr = imagePathStr.replace("']","")
#CLEANUP

    print(imagePathStr)
    img = Image.open(imagePathStr)
    img.show()
    os.remove(imagePathStr)

    print("image removed")
#ubuntu is shotwell pm

def speak(words):
    tts = gTTS(text=str(words), lang='en')
    soundName = "TARSAudioTemp"
    soundName = soundName + ".mp3"
    tts.save(soundName)
    print(soundName)
    playsound(soundName)
    os.remove(soundName)






firstTimeSetup()

while True:
    question = input("Question:")
    question = question.lower()
    questionSplit = question.split()
    try:
        if "time" in questionSplit and "in" not in questionSplit:
            getCurrentTime()
        elif ("show" and "pictures" in questionSplit) or ("show" and "picture" in questionSplit or ("show" in questionSplit)):
            imageSearch(question)


        else:

            res = tars.query(question)
            answer = next(res.results).text
            print("TARS >>> ",answer)


    except:
        continue
