
#apikey = "56a23970eb2042059e7727de84e9e498"
import pydest,asyncio,json,codecs
import requests
HEADERS = {"X-API-Key":'56a23970eb2042059e7727de84e9e498'}

apikey = "56a23970eb2042059e7727de84e9e498"
myuserid = "10061778"
async def main():


    destiny = pydest.Pydest(apikey)
    json = await destiny.api.get_destiny_manifest()
    await destiny.close()
    return json


asyncio.run(main())

manifestEndpoint = "Destiny2/Milestones/"

url = "https://www.bungie.net/Platform/" + manifestEndpoint


#decoded_data=codecs.decode(requests.text.encode(), 'utf-8-sig')

reqUrl = requests.get(url,headers=HEADERS)

print(reqUrl.json())
    

with open("destinyData.json","w") as jf:
    json.dump(reqUrl.json(),jf,indent=4)
jf.close()

#json = reqUrl.json()[]''