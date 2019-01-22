from pytube import YouTube as YT
from pytube import Playlist
import os
cls = lambda: os.system('cls')

def singleVideo():
    cls()
    print("╔════════════════════════════╗")
    print("║Download type : Single video║")
    print("╚════════════════════════════╝")
    path = os.getcwd()#get dir for download
    print ("\nThe current directory is : %s" % path)
    Url = input("Paste the Youtube URL Here: ")
    YT(Url).streams.first().download()
    print("Done!")

def playlist():
    cls()
    print("╔════════════════════════════╗")
    print("║Download type : Playlist    ║")
    print("╚════════════════════════════╝")
    path = os.getcwd()#get dir for download
    print ("The current directory is : %s" % path)
    newFolderPath = input("Please enter the name of the folder that the playlist will be saved under: ")
    access_rights = 777 #folder access_rights
    try:
        os.mkdir(newFolderPath, access_rights)#make directory
    except OSError:
        print ("Creation of the directory %s failed" % path)
    else:
        print ("Successfully created the directory %s " % path)
    Url = input("\nPaste the Youtube Playlist URL Here: ")
    pl = Playlist(Url)
    fullFilePath = "D:/Programs/Python/" + str(newFolderPath)
    pl.download_all(fullFilePath)
    print("Done!")




downloadType = input("download a (1)playlist or a (2)video: ")
if int(downloadType) == 1:
    playlist()
elif int(downloadType) == 2:
    singleVideo()
