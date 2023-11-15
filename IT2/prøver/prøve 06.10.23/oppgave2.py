varedata = [
    {'Vare-ID':'Asus Zenbook GH215',
    'Varenavn':'Asus laptop',
    'Pris': '9999',
    'Varelager': '10',
    'Produktinfo': 'En bærbar PC med 15.6 tommer skjerm, 8 GB RAM og 256 GB SSD',
    'Tekniske egenskaper': { 
        'prosessor': 'Intel Core i5-1135G7',
        'grafikkort':'Intel Iris Xe Graphics',
        'batterikapasitet':'Opptil 8 timer',
        'vekt':' 1.8 kg '},
    'Farger': ['grå', 'svart', 'blå']},
    
    {'Vare-ID':' Samsung Galaxy S22 GH67',
    'Varenavn': 'Samsung mobiltelefon',
    'Pris': '6999',
    'Varelager': '20',
    'Produktinfo': 'En smarttelefon med 6.7 tommer skjerm, 128 GB lagring og 12 MP kamera',
    'Tekniske egenskaper': {
        'prosessor':'Qualcomm Snapdragon 888',
        'grafikkort':' Adreno 660',
        'batterikapasitet':' 4500 mAh',
        'vekt':' 200 g'},
    'Farger': ['svart', 'hvit']}
    ]


def skrivInfo(ordbok):
    for punkt in ordbok:

        if str(type(ordbok[punkt])).find('str') > 0:
        #hvis det er en string
            print(f'{punkt}: {ordbok[punkt]}')
            print()

        elif str(type(ordbok[punkt])).find('list') > 0:
            print(f'{punkt}:')
            print()
            for i in ordbok[punkt]:
                print(i)
                print()

        else: # hvis en dict
            print(f'{punkt}:')
            print()
            for i in ordbok[punkt]:
                print(f'{i}: {ordbok[punkt][i]}')
                print()
    print()
    print()

# for ordbok in varedata:
#     skrivInfo(ordbok)

def finnVare(fargeInn):
    for ordbok in varedata:
        for farge in ordbok['Farger']:
            if farge == fargeInn :
                skrivInfo(ordbok)

finnVare('blå')