import requests as req
import json

nøkkel = '399c2091-bd5d-49da-a397-01796c492efa'

for i in range(1000):
    if i < 10:
        slutt = '00' + str(i)
    elif i < 100:
        slutt = '0' + str(i)
    else: 
        slutt = str(i)
    

    api_url = ('https://www.vegvesen.no/ws/no/vegvesen/kjoretoy/felles/datautlevering/enkeltoppslag/kjoretoydata?kjennemerke=SP23962')

    headers = {"SVV-Authorization" : "Apikey 399c2091-bd5d-49da-a397-01796c492efa"}

    response = req.get(api_url, headers = {"SVV-Authorization" : "Apikey 399c2091-bd5d-49da-a397-01796c492efa"})

    # response.json()

    data = response.content

    fil = open('bilData.json', 'w')
    fil.write(str(data)[2:-1])
    fil.close()


    try:
        data = json.loads(data)

        merke = data['kjoretoydataListe'][0]['godkjenning']['tekniskGodkjenning']['tekniskeData']['generelt']['merke'][0]['merke']
        modell = data['kjoretoydataListe'][0]['godkjenning']['tekniskGodkjenning']['tekniskeData']['generelt']['handelsbetegnelse'][0]
        status = data['kjoretoydataListe'][0]['registrering']['registreringsstatus']['kodeBeskrivelse']


        if merke == 'VOLKSWAGEN':
            print(f'Bil med regnr SP23{slutt} er en: {merke} {modell}, og er {status}')
    
    except:
        print(f'Bil med regnr SP23{slutt} finnes ikke')


# Bil med regnr SP23710 er en: VOLKSWAGEN VW
# Bil med regnr SP23711 er en: VOLKSWAGEN VW
# Bil med regnr SP23797 er en: VOLKSWAGEN VW
# Bil med regnr SP23832 er en: VOLKSWAGEN VW
# Bil med regnr SP23962 er en: VOLKSWAGEN VW