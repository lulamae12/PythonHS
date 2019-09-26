import wolframalpha,wikipedia,datetime,os,subprocess
from google_images_download import google_images_download
from questionTypes import *
from PIL import Image
from tarsConfig import *
from chatterbot import ChatBot
from playsound import playsound
import pyttsx3
appID = "P6Y6GV-H9Y7RETQ37"
tars = wolframalpha.Client(appID)
tarsChatBot = ChatBot(
    'TarsChat',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'

)
tts = pyttsx3.init()
rate = tts.getProperty('rate')
tts.setProperty('rate', 180)
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
    speak("the current time is " + str(hour)  + " " + str(minute) + " " + str(period))

def imageSearch(term):



    term = term.replace("show me ","")

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
    speak("showing pictures of "+ term)
    img.show()



    os.remove(imagePathStr)

    print("image removed")
#ubuntu is shotwell pm
def speak(words):
    tts.say(words)
    tts.runAndWait()

def trainTars(trainingIterations):
    while trainingIterations != 0:
        tarsChatBot.train("chatterbot.corpus.english")
        trainingIterations = trainingIterations - 1





firstTimeSetup()
trainTars(1)
while True:

    question = input("Question:")
    question = question.lower()
    questionSplit = question.split()
    try:
        if "time" in questionSplit and "in" not in questionSplit:
            getCurrentTime()
        elif "show" in questionSplit:
            imageSearch(question)

        else:

            res = tars.query(question)
            answer = next(res.results).text
            print("TARS >>> ",answer)
            speak(answer)


    except:
        try:
            print(wikipedia.summary(question))
            speak(wikipedia.summary(question))
        except:
            answer = tarsChatBot.get_response(question)
            print('Tars: >>> ',answer)
            speak(answer)
