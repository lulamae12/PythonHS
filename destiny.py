
from bungoAPI import *


import requests

#dictionary to hold extra headers
HEADERS = {"X-API-Key":APIKey}

#make request for Gjallarhorn
r = requests.get("https://www.bungie.net/platform/Destiny/Manifest/InventoryItem/1274330687/", headers=HEADERS);

#convert the json object we received into a Python dictionary object
#and print the name of the item
inventoryItem = r.json()
print(inventoryItem['Response']['data']['inventoryItem']['itemName'])
