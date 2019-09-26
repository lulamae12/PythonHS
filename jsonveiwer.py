import json
with open('channel.json') as json_data:
    d = json.load(json_data)
    print(d)
