import requests as req
import os
import json


from dotenv import load_dotenv
load_dotenv()

nøkkel = os.getenv('APIKEY')
print(nøkkel)


VWliste =[]

for i in range(1000):
    if i < 10:
        slutt = '00' + str(i)
    elif i < 100:
        slutt = '0' + str(i)
    else: 
        slutt = str(i)
    

    api_url = ('https://www.vegvesen.no/ws/no/vegvesen/kjoretoy/felles/datautlevering/enkeltoppslag/kjoretoydata?kjennemerke=SP23'+slutt)

    headers = {"SVV-Authorization" : nøkkel}

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
        tidspunkt = data['kjoretoydataListe'][0]['registrering']['fomTidspunkt'][0:10]

        if modell == 'VW':
            VWliste.append(f'Bil med regnr SP23{slutt} er en: {merke} {modell}, og er {status} siden {tidspunkt}')
        
        print(f'Bil med regnr SP23{slutt} er en: {merke} {modell}, og er {status} siden {tidspunkt}')
    
    except:
        print(f'Bil med regnr SP23{slutt} finnes ikke')

print('Liste over VW busser:')

for bil in VWliste:
    print(bil)


#Liste over VW bussser:
'Bil med regnr SP23008 er en: VOLKSWAGEN VW, og er Vraket siden 1995-04-06'
'Bil med regnr SP23133 er en: VOLKSWAGEN VW, og er Vraket siden 1995-11-13'
'Bil med regnr SP23153 er en: VOLKSWAGEN VW, og er Vraket siden 1992-06-02'
'Bil med regnr SP23133 er en: VOLKSWAGEN VW, og er Vraket siden 1995-11-13'
'Bil med regnr SP23153 er en: VOLKSWAGEN VW, og er Vraket siden 1992-06-02' 
'Bil med regnr SP23182 er en: VOLKSWAGEN VW, og er Vraket siden 1989-05-08' 
'Bil med regnr SP23249 er en: VOLKSWAGEN VW, og er Avregistrert siden 1986-03-17'
'Bil med regnr SP23263 er en: VOLKSWAGEN VW, og er Vraket siden 1989-03-14'
'Bil med regnr SP23484 er en: VOLKSWAGEN VW, og er Vraket siden 1996-09-24'
'Bil med regnr SP23536 er en: VOLKSWAGEN VW, og er Vraket siden 1991-01-24'
'Bil med regnr SP23537 er en: VOLKSWAGEN VW, og er Avregistrert siden 1986-01-27'
'Bil med regnr SP23538 er en: VOLKSWAGEN VW, og er Vraket siden 1998-10-14'
'Bil med regnr SP23539 er en: VOLKSWAGEN VW, og er Vraket siden 1990-03-15'
'Bil med regnr SP23548 er en: VOLKSWAGEN VW, og er Vraket siden 1993-02-26'
'Bil med regnr SP23610 er en: VOLKSWAGEN VW, og er Vraket siden 1990-09-12' 
'Bil med regnr SP23710 er en: VOLKSWAGEN VW, og er Vraket siden 1987-04-21'
'Bil med regnr SP23711 er en: VOLKSWAGEN VW, og er Vraket siden 1990-06-13'
'Bil med regnr SP23797 er en: VOLKSWAGEN VW, og er Vraket siden 1996-01-08'
'Bil med regnr SP23832 er en: VOLKSWAGEN VW, og er Vraket siden 1993-12-10'
'Bil med regnr SP23962 er en: VOLKSWAGEN VW, og er Vraket siden 1991-10-11'

