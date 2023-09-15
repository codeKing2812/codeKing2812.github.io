import json

fil = open('landData.json', 'r')

landListe = json.loads(fil.read())[1]

print(type(landListe))

for land in landListe:
    if land['capitalCity'] == "" :
        landListe.pop(land)
    print(land['capitalCity'])


temp_dict = {}
tKey = ""

for k, v in landListe.items():
    if k != tKey:
        temp_dict[k] = v

dict = temp_dict