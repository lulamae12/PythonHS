from pytube import YouTube as YT
from pytube import Playlist
import os,pytube
cls = lambda: os.system('cls')

def singleVideo():
    cls()
    print("╔════════════════════════════╗")
    print("║Download type : Single video║")
    print("╚════════════════════════════╝")
    path = os.getcwd()#get dir for download
    print ("\nThe current directory is : %s" % path)
    Url = input("Paste the Youtube URL Here: ")
    ytStream = YT(Url)

    print("\nTitle: ",ytStream.title)
    sureToDL = input("Download? (y,n) : ")
    if sureToDL == "y":
        YT(Url).streams.first().download()
        print("Done!")
    else:
        print("Not downloaded.")

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
    pl = Playlist('https://www.youtube.com/playlist?list=PLKJ7g305OHDEUNF_BzAUdcxt4d_ey8m6z')

    fullFilePath = "D:/Programs/Python/" + str(newFolderPath)
    while True:
        try:

            pl.download_all(fullFilePath)
            print("Done!")
        except pytube.exceptions.RegexMatchError:
            pass


downloadType = input("Download a (1)playlist, (2)video: ")
if int(downloadType) == 1:
    playlist()
elif int(downloadType) == 2:
    singleVideo()
