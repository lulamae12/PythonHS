#soupmaker.py
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
def soupGen(url):
    webpage = urlopen(url)
    html = webpage.read()
    webpage.close()
    urlsoup = soup(html, "html.parser")
    return urlsoup
