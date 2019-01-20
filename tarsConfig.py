import subprocess

packageList = ["wolframalpha","wikipedia","google-images-download","pillow","docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew","kivy","kivy.deps.gstreamer"]

def configSetup():
    setupFile = open("TarsSetup.txt","w")
    setupFile.write("1")
    setupFile.close()
    for package in packageList:
        subprocess.call("py -3 -m pip install "+ package)#install
configSetup()
