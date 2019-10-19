import requests
import urllib.request
from urllib.request import Request
import time,sys
from bs4 import BeautifulSoup
from soupMaker import soupGen



class grimoreScrape():
    def __init__(self,link):
        self.url = link
        self.response = requests.get(self.url)
        print(self.response)
    def makeSoup(self):
        soup = BeautifulSoup(self.response.text,"html.parser")
        soupPretty = soup.prettify()
        #print(soupPretty)
        self.findLoreEntryObjects(soup)
        

    def findLoreEntryObjects(self,soup):
        
        maincontent = soup.findAll("div",class_="panel panel-default clearfix grimoire-card")
        list1 = str(maincontent).split("</div>")
        #print(maincontent.title)
        #for i in list1:
         #   print(i)
        print(list1[0])

g= grimoreScrape("https://db.destinytracker.com/d1/grimoire/guardian/classes")
g.makeSoup()