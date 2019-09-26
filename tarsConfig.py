import subprocess

packageList = ["wolframalpha","wikipedia","google-images-download","pillow","playsound","wxpython","pyttsx3"]

def configSetup():
    setupFile = open("TarsSetup.txt","w")
    setupFile.write("1")
    setupFile.close()
    for package in packageList:
        subprocess.call("py -3 -m pip install "+ package)#install
