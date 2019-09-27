import markovify
import datetime,re,time,sys
from PyLyrics import *

#I had the same error and I fix it changing line 62
#url = "http://lyrics.wikia.com/api.php?artist={0}&fmt=xml".format(album.artist())
#by
#url = "http://lyrics.wikia.com/api.php?action=lyrics&artist={0}&fmt=xml".format(album.artist())

def possibleRhymeWord(lyric):
    lyricSplit = lyric.split()
    print(str(lyricSplit))
    sys.exit()

def getAlbmums(artist):
    albums = PyLyrics.getAlbums(singer=artist)
    print(albums)
    return albums
def selectAlbum(albumList):
    allOrOne = int(input("Would you like to get lyrics for one(1) album, \nor all albums in list(2)?\nChoice: "))

    if allOrOne == 1:
        albumsList = []
        for i in range(len(albumList)):
            albumsList.append(albumList[i])
        for i in range(len(albumList)):
            print(i+1," - ",albumList[i])
        albumSelection = int(input("Which album?: "))
        
        tracks = PyLyrics.getTracks(albumsList[albumSelection-1])
        lyricList = []
        songCounter = 0
    
        
        for track in tracks:
            try:
                lyricList.append(track.getLyrics())
                lyricList.append("\n\n\n")
                songCounter = songCounter + 1
            except ValueError:
                pass
        print(lyricList)
        print(songCounter)
        
        #clean
        for lyric in lyricList:
            

            
            print(lyric)
            
            time.sleep(1)
            
        corpusTitle = "lyricCorpus"+ datetime.datetime.today().strftime("%Y%m%d%S") +".txt"
        print(corpusTitle)
        
        songCorpus = open(corpusTitle,"w+")

        for line in lyricList:
            songCorpus.write(line)
        
        
        
        


    elif allOrOne == 2:
        print("")
    else:
        print("error not choce")





albumArtist = input("Enter album artist: ")



selectAlbum(getAlbmums(albumArtist))
