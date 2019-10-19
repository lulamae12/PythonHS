
#apikey = "56a23970eb2042059e7727de84e9e498"
import pydest,asyncio,json,codecs,urllib.request
import requests,os
HEADERS = {"X-API-Key":'56a23970eb2042059e7727de84e9e498'}
apikey = "56a23970eb2042059e7727de84e9e498"
myuserid = "10061778"
sectionKeyList = ["DestinyLoreDefinition","DestinyDestinationDefinition","DestinyPlaceDefinition","DestinyRecordDefinition"]

async def getJsonManifest():
    destiny = pydest.Pydest(apikey)
    json = await destiny.api.get_destiny_manifest()
    await destiny.close()
    return json


def updateManifest(url):
    
    manifestEndpoint = "Destiny2/Manifest/"
    manifestUrl = "https://www.bungie.net/Platform/" + manifestEndpoint
    print("-----WARNING-----\n\nThis is a HUGE file and will proably take a long time to download.\n=========================")
    continueMan = input("Continue? (y/n) : ")
    
    if continueMan.lower == "y":
        
        manifestUrl = requests.get(url)
        manifestUrl.close()
        with open("destinyManifestData.json","w") as destinyRawManifestJson:
           json.dump(manifestUrl.json(),destinyRawManifestJson,indent=4)
        destinyRawManifestJson.close()

        try:
            reqUrl = requests.get(url,headers=HEADERS)
            with open("destinyData.json","w") as jf:
                json.dump(reqUrl.json(),jf,indent=4)
            jf.close()
        except:
            print("error")
            pass
    
    with open("destinyManifestData.json","r") as destMan:
        manifestDict = json.load(destMan)
        keyList = []
        for item in manifestDict:
            print("key [ ",item," ] \n")
            createSectionFile(item,manifestDict[item],sectionKeyList)
        print(manifestDict["DestinyPlaceDefinition"])
   
def createSectionFile(key,jsonDict,sectionList):
    currentPath = os.getcwd()
    print("current path is : ",currentPath)
    #filePath = "\\destinySections\\" + str(key)
    if key in sectionList:
        filePath = currentPath + "/" + "destiny_filtered_sections" + "/" + str(key)+ "/"
        try:
            os.makedirs(filePath, 777)
            print("created!\n    File: '",key,"'\n    Path: '",filePath,"'")
        except OSError:
            print ("Creation of the directory %s failed" % filePath)
            pass
        filePath2 = str(filePath)+"/jsonFile.json"
        with open(filePath2,"w") as jsonFile:
            json.dump(jsonDict,jsonFile,indent=4)
        jsonFile.close()







destiny = pydest.Pydest(apikey)
#asyncio.run(getJsonManifest())


manifestEndpoint = "Destiny2/Manifest/"
url = "https://www.bungie.net/Platform/" + manifestEndpoint


#decoded_data=codecs.decode(requests.text.encode(), 'utf-8-sig')

def run():
    updateManifestRun = input("would you like to update the manifest from source? y/n: ")
    if updateManifestRun.lower() == "y":
        updateManifest("https://www.bungie.net/common/destiny2_content/json/en/aggregate-f2cf75d7-0de6-4488-aad0-2fa02a0ac343.json")
    
if __name__ == "__main__":
    run()




#print(destiny.decode_hash(""))

#json = reqUrl.json()[]''