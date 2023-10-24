# oppgave A

høyde = int(input('høyde:'))
bredde = int(input('bredde:'))

def bildeFormat(høyde, bredde) :
    if høyde > bredde :
        return('Portrait')
    elif høyde == bredde:
        return('Square')
    else :
        return('Landscape')

print(bildeFormat(høyde, bredde))

####################################################


# oppgave B

enTilHundre = []
for i in range(100) :
    enTilHundre.append(i+1)

print('lengde:', len(enTilHundre))

def deleligeTall(liste, divisor):
    print(f'ser etter delbare med {divisor}')
    delelige = []
    for i in liste :
        if (i // divisor) == (i / divisor):
            delelige.append(i)
    return(delelige)

for i in deleligeTall(enTilHundre, 7):
    print(i)

####################################################


# oppgave C

import datetime

def taFødselsnr():
    fødselsnr = input('skriv inn ditt fødselsnummer her:')
    try:
        int(fødselsnr)
        if len(fødselsnr) != 11:
            raise TypeError()
        return(fødselsnr)
    except:
        print('du må skrive inn et tall på 11 siffer')
        taFødselsnr()

# fødselsnr = taFødselsnr()
fødselsnr = '28120586779'

dag = fødselsnr[0: 2]
måned = fødselsnr[2: 4]
år = fødselsnr[4: 6]

kjønn = fødselsnr[8]


print(f'fødselsdatoen er: {dag}.{måned}.{år}')

def bedreDag(dag):
    if dag[0] == '0' :
        dag = dag[1] + '.'
    return(dag)


def bedreMåned1(måned):
    månedene = ['januar', 'februar', 'mars', 'april', 'mai', 'juni', 'juli', 'august', 'september', 'oktober', 'november', 'desember']
    måned = månedene[int(måned)-1]
    return(måned)


def bedreMåned2(måned):
    if måned == '01':
        måned = 'Januar'
    elif måned == '02':
        måned = 'Februar'
    elif måned == '03':
        måned = 'Mars'
    elif måned == '04':
        måned = 'April'
    elif måned == '05':
        måned = 'Mai'
    elif måned == '06':
        måned = 'Juni'
    elif måned == '07':
        måned = 'Juli'
    elif måned == '08':
        måned = 'August'
    elif måned == '09':
        måned = 'September'
    elif måned == '10':
        måned = 'Oktober'
    elif måned == '11':
        måned = 'November'
    elif måned == '12':
        måned = 'Desember'
    return(måned)

    
def bedreÅr(år):
    if int('20' + år) < datetime.datetime.now().year:
        år = '20' + år
    else :
        år = '19' + år
    return(år)

def bedreKjønn(kjønn):
    kjønn = int(kjønn)
    if (kjønn // 2) == (kjønn / 2):
        kjønn = 'kvinne'
    else :
        kjønn = 'mann'
    return(kjønn)


print(f'Du er født den {bedreDag(dag)} {bedreMåned1(måned)} {bedreÅr(år)}, og er en {bedreKjønn(kjønn)}')