import requests
import json

resp = requests.get('https://api.kraken.com/0/public/Assets')

assets = resp.text

#print(assets.keys())
#print(assets.values())

parsed = json.loads(assets)
print(json.dumps(parsed, indent=4, sort_keys=True))

assets = resp.json()

cur_keys = (assets.get('result').keys())


for x in cur_keys:
    if assets.get('result').get(x)['display_decimals'] == 6:
        print(assets.get('result').get(x))