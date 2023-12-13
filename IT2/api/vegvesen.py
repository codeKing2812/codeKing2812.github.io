import requests as req
import json

nøkkel = '399c2091-bd5d-49da-a397-01796c492efa'

api_url = 'https://www.vegvesen.no/ws/no/vegvesen/kjoretoy/felles/datautlevering/enkeltoppslag/kjoretoydata?kjennemerke=SP26055'

headers = {"SVV-Authorization" : "Apikey 399c2091-bd5d-49da-a397-01796c492efa"}

response = req.get(api_url, headers = {"SVV-Authorization" : "Apikey 399c2091-bd5d-49da-a397-01796c492efa"})

# response.json()

data = response.content

fil = open('bilData.json', 'w')
fil.write(str(data)[2:-1])
fil.close()


data = json.loads(data)

merke = data['kjoretoydataListe'][0]['godkjenning']['tekniskGodkjenning']['tekniskeData']['generelt']['merke'][0]['merke']
modell = data['kjoretoydataListe'][0]['godkjenning']['tekniskGodkjenning']['tekniskeData']['generelt']['handelsbetegnelse'][0]

print('Bilen er en:', merke, modell)