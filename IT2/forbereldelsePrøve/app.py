# Modul 1


from tkinter import *
from tkinter import ttk

app = Tk()
app.geometry("500x600")
main = ttk.Frame(app)
main.place(rely=0, relwidth=1)

scroll = ttk.Scrollbar(app)
scroll.place(relx=1, anchor='ne', relheight=1)


def innData():
    K_inn = int(input('Skriv inn K-punktet til bakken'))
    if 70 < K_inn and K_inn < 250 :
        bestemMeterpoeng(K_inn)
    else:
        print('Skriv inn et tall mellom 70 og 250')
        innData()

def bestemMeterpoeng(K_punkt):
    global meterverdi
    if K_punkt < 79:
        meterverdi = 2.2
    elif K_punkt < 99:
        meterverdi = 2
    elif K_punkt < 169:
        meterverdi = 1.8
    elif K_punkt < 250:
        meterverdi = 1.2
    
    

innData()
print(meterverdi)


# Modul 2

def lengdepoeng(hopplengde, K_punkt, meterverdi):
    Lengdepoeng = 60 + (hopplengde - K_punkt) * meterverdi
    return Lengdepoeng


