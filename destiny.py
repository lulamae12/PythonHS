import destinyUpdateManifest as dum 
import pydest,asyncio,os,json,sys
cls = lambda: os.system('cls')
classifieditemNum = 0000
valueList = ["name","description","hasIcon","hash","index","icon","subtitle"]


def writeLoreFile(name,subtitle,description,hasIcon,icon,hashVal,index):
    global classifieditemNum
    if str(name) == "Classified":
        classifieditemNum = classifieditemNum + 1 
        name = name + "-" +str(classifieditemNum)
    if str(name) == "":
        classifieditemNum = classifieditemNum + 1 
        name = "[REDACTED]"

    data = {
        name:{
            "name":name,
            "subtitle":subtitle,
            "description":description,
            "hasIcon":hasIcon,
            "icon":icon,
            "hash":hashVal,
            "index":index
        }
    }    
    print(data)
    
    with open("destinyLoreFile.json","a") as jsonFile:
        json.dump(data,jsonFile,indent=4)
    jsonFile.close()

def getManifestData(BaseFolderName,foldername):
    nameValue = ""
    descriptionValue = ""
    hasIconValue = ""
    hashValue =  ""
    indexValue = ""
    iconValue = ""

    
    
    
    
    
    currentPath = os.getcwd()
    dataPath = currentPath +"\\"+BaseFolderName+"\\"+foldername+"\\jsonFile.json"
    print(dataPath)
    with open(dataPath,"r") as file:
        jsonFile = json.loads(file.read())
    file.close()    
    #print(jsonFile)
    #jsonFile = json.dumps(str(jsonFile),indent=4,sort_keys=True)
    #for key in jsonFile:
    hashList = []
    
    for key in jsonFile.keys():
        
        hashList.append(key)
    #print(hashList)
    cls()
    for hash in hashList:
        valueList = ["name","description","hasIcon","hash","index","icon","subtitle"]
        #print("BRUJJJJJJJJJJJJJJJJJ")
        hashSection = jsonFile[hash]
        
        for key,value in hashSection.items():
            #print("KEY: ",key,":","VALUE: ",value)
            keyTypeList=["name","description","hasIcon","hash","index","icon","subtitle"]
            usedKeyList=[]
            
            currentKey = ""
            currentValue = ""
        #print(key)
            if str(key) == "displayProperties":

                for key,value in value.items():
                    
                    if str(key) == ("name"):
                        nameValue = value
                        #print(nameValue)
                        #sys.exit()
                    elif str(key) == ("description"):
                        descriptionValue = value
                        #print(descriptionValue)
                        #sys.exit()

                    elif str(key) == ("hasIcon"):
                        hasIconValue = value
                        #print(hasIconValue)
                        #sys.exit()       
            
            if str(key) == ("hash"):
                hashValue = value
                ##print(hashValue)
                #sys.exit()

            elif str(key) == ("index"):
                indexValue = value
                ##print(indexValue)
                #sys.exit()

        
            elif str(key) == ("icon"):
                iconValue = value
                ##print(iconValue)
                #sys.exit()

            elif str(key) == ("subtitle"):
                subValue = value
                ##print(subValue)
                #sys.exit()

        
        print(nameValue,":::",descriptionValue,":::",hasIconValue,":::",hashValue,":::",indexValue,":::",iconValue,":::",subValue)
        writeLoreFile(nameValue,subValue,descriptionValue,hasIconValue,iconValue,hashValue,indexValue)
            



getManifestData("destiny_filtered_sections","DestinyLoreDefinition")
