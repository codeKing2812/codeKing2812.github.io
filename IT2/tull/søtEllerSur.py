navn = input('Navn: ')
alder = int(input('Alder: '))

bokstavVerdi = ord(navn[0])

if bokstavVerdi < 80 :
    smak = 'sur'
elif bokstavVerdi < 90 :
    smak = 'søt'
elif bokstavVerdi < 110 :
    smak = 'sur'
else :
    smak = 'søt'

print(f'Du heter {navn} og er en {alder} år gammel {smak} frukt')