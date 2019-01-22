import pydest
import asyncio
from bungoAPI import *


async def main():

    destiny = pydest.Pydest(APIKey)
    activity1 = await destiny.decode_hash(60002467, 'DestinyActivityDefinition')
    await destiny.update_manifest()


    print("Activity Name: {}".format(activity1['displayProperties']['name']))
    print("Description: {}".format(activity1['displayProperties']['description']))
    print("")

    destiny.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
