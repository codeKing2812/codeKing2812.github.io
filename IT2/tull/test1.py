navn = input('Navn: ')
alder = input('Alder: ')

alder = int(alder)

print('bokstav 1:', navn[0])

bokstavVerdi = ord(navn[0])

print('bokstavverdi:', bokstavVerdi)

if alder < 20 :
    print('Du heter', navn,'og er et barn')
