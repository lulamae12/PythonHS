import markovify
from PyLyrics import *

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
        albumSelection = input()
        
        
        
        


    elif allOrOne == 2:
        print("")
    else:
        print("error not choce")



albumArtist = input("Enter album artist: ")



selectAlbum(getAlbmums(albumArtist))
