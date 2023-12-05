navn = input('Navn: ')
alder = int(input('Alder: '))

bokstavVerdi = ord(navn[0])

if bokstavVerdi < 80 :
    smak = 'sur, som eirik'
elif bokstavVerdi < 90 :
    smak = 'søt, som linus'
elif bokstavVerdi < 110 :
    smak = 'sur, som linus'
else :
    smak = 'søt, som eirik'

print(f'Du heter {navn} og er en {alder} år gammel {smak} frukt')
