#amplifiScraper.py
from soupMaker import soupGen
from datetime import datetime
import csv,time
def findprice(price, first, last):
    try:
        start = price.index( first ) + len( first )
        end = price.index( last,start )
        return price[start:end]
    except ValueError:
        return "ERROR"
while True:
    currentTime = datetime.now().time()
    productPage = soupGen("https://www.bestbuy.com/site/ubiquiti-amplifi-hd-mesh-wi-fi-system-wireless-ac1750-dual-band-wi-fi-router-white/5736902.p?skuId=5736902") #opens soupmaker.py and inputs url
    price = productPage.find(class_= "priceView-hero-price priceView-purchase-price")
    price = str(price)
    print(findprice(price,'<div class="priceView-hero-price priceView-purchase-price"><span aria-label="Your price for this item is ','">$<!-- -->349.99</span></div>'),"as of,",str(currentTime))
    time.sleep(1)
