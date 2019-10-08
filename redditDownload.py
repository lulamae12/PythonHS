#! /usr/bin/python3

#! /usr/bin/python3 linuix   #! python3 windows
import praw,requests,urllib.request,psraw,time,os,sys,requests,csv
from imgur_downloader.imgurdownloader import ImgurDownloader
import pandas as pd
import datetime as dt
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup
from soupMaker import soupGen







personalUseScript = "XAhJwhffVavIOw"
secretKey = "C1gRyuSNI0B2Ifd_2sJdBux2LDU"

reddit = praw.Reddit(client_id=personalUseScript,client_secret = secretKey,user_agent = 'subImageDownloader')

subList = ["pics"]


class Reddit():
    def __init__(self,subreddit):
        self.subreddit = subreddit
        self.filename = str(subreddit)

        self.submissions = ""
        self.fullFilename = ""
        self.url = ""
        self.gfyUrl = ""
    def gfyScrape(self,url):

        videoSrcList = [] #make list of video sources

        gfyPage = soupGen(str(url))#get curl and pass into soup gen to generate a soup
        videoSrc = gfyPage.find(class_ = "video media")#search for all classes of video media



        for i in videoSrc:
                videoSrcList.append(i)#add video sources to video source list

        for i in range(len(videoSrcList)):
            #print(videoSrcList[i])
            if 'type="video/mp4"/' in str(videoSrcList[i]) and "-mobile" not in str(videoSrcList[i]):
                videoSrc = str(videoSrcList[i])

                videoSrc = videoSrc.replace('<source src="',"")
                videoSrc = videoSrc.replace('" type="video/mp4"/>',"")

                return videoSrc


        #print(videoSrcList)

        #print(gfySoup.prettify())#order data better


        #print(gfyPage.content)


    def scrapeTweet(self,url):
        #stilll working on this
        TwitterSrcList = [] #make list of pic sources

        twitterPage = soupGen(str(url))#get curl and pass into soup gen to generate a soup
        twitterSrc = twitterPage.find(class_ = "css-1dbjc4n r-1niwhzg r-vvn4in r-u6sd8q r-4gszlv r-1p0dtai r-1pi2tsx r-1d2f490 r-u8s1d r-zchlnj r-ipm5af r-13qz1uu r-1wyyakw")
        print(str(twitterSrc))


        #for i in twitterSrc:
        #        TwitterSrcList.append(i)#add twitter sources to ist

        #for i in range(len(TwitterSrcList)):
            #print(TwitterSrcList[i])
        #    if 'pbs.twimg.com' in str(TwitterSrcList[i]) :
        #        print(TwitterSrcList[i])
        #        sys.exit()
        #        videoSrc = str(videoSrcList[i])

        #        videoSrc = videoSrc.replace('<source src="',"")
        #        videoSrc = videoSrc.replace('" type="video/mp4"/>',"")

        #        return videoSrc


    def subDownload(self): #main

        currentDir = os.getcwd()
        print("cwd is :",currentDir)
        currentDir = currentDir + "/" + str(self.subreddit)+ "/"

        try:
            os.mkdir(currentDir, 777)
        except:
            pass


        self.textFile = open(currentDir + "%soutput.txt" % self.filename, "w", errors ='ignore')

        self.submissions = reddit.subreddit(self.subreddit).hot(limit=50)
        for item in self.submissions:
            self.textFile.write(item.url+"\n")

        self.textFile.close()
        self.fullFilename = currentDir + self.filename + "output.txt"

        #cleanup lines
        with open(self.fullFilename) as f: lines = [line.rstrip('\n') for line in f]

        #print(lines)
        for item in lines:
            try:
                self.url = item
                filenm = self.url.split('/')[-1]
                r = requests.get(self.url, allow_redirects=True)#get link of image
                print(self.url+"\n")


                #do imgur album and twitter stuff here
                if "i.redd.it" in self.url:
                    open(currentDir+filenm, 'wb').write(r.content)#if its a reddit pciture download

                elif "i.imgur.com" in self.url and "imgur.com/a/" not in self.url: #is an imgur SINGLE picture:
                    open(currentDir+filenm, 'wb').write(r.content)#if its a reddit pciture download
                elif "i.ibb.co" in self.url:
                    open(currentDir+filenm, 'wb').write(r.content)

                elif "twitter.com" in self.url:
                    try:
                        #self.scrapeTweet(self.url)#is tweet extract url from it
                        pass
                    except:
                        pass
                elif "imgur.com/a/" in self.url:#if its an imgur album

                    #print("imgur album")
                    ImgurDownloader(self.url,currentDir ,delete_dne=False, debug=False).save_images()#download images to file in filenm
                elif "gfycat" in self.url:

                    try:
                        gfyUrl = self.gfyScrape(self.url)
                        print(gfyUrl)
                        r = requests.get(gfyUrl, allow_redirects=True)#get link of gfy
                        open(currentDir+filenm+".mp4", 'wb').write(r.content)#dpwnload gfy as webm or mp4 not sure yet which to do
                    except:
                        pass




            except OSError as e:
                print("ERROR ON: ",e)





downsSub = Reddit("pics")




while True:
    #picsSub.subDownload()
    for i in range(len(subList)):
        print(subList[i])
        subToDownload = Reddit(subList[i])
        subToDownload.subDownload()
    #time.sleep(60)
    break
