import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="238744af4cc644688b90c26fc9a73b62",
                                               client_secret="b97149e52b1a4d559ed8906d20a7f66f",
                                               redirect_uri="http://localhost:3000",
                                               scope="user-library-read"))

results = sp.current_user_saved_tracks()

# print(results['items'])

likteLåter=[]
for item in results['items']:
    låt = item['track']

    likteLåter.append(låt)
    # print(låt['name'])




from tkinter import *
from tkinter import ttk


def visWidget(widget):
    widget.place()

def skjulWidget(widget):
    widget.place_forget()


app = Tk()
app.geometry("500x500")
#lager rammen for programmet

scroll = ttk.Scrollbar(app)
scroll.place(relx=1)

ttk.Label(app, text='Dine siste likte låter er:').place(rely=0, relx=0.5)


def infoKnapp(låt):
    i1 = ttk.Label(app, text='album: ' + låt['album']['name'])
    i2 = ttk.Label(app, text='artist: ' + låt['artists'][0]['name'])
    skjulWidget(i1)
    skjulWidget(i2)
    
    ttk.Button(app, text=låt['name'], command= lambda: [visWidget(i1), visWidget(i2)]).place(rely=0.2, relx=0.5)
                   
    ttk.Button(app, text='lukk', command= lambda: [skjulWidget(i1), skjulWidget(i2)]).place(rely=0.3, relx=0.5)

for låt in likteLåter:
    infoKnapp(låt)

# in_tekst = ''
# ttk.Entry(program,  textvariable = in_tekst)


# info1 = ttk.Label(app, text='album: ' + likteLåter[0]['album']['name'])
# info2 = ttk.Label(app, text='artist: ' + likteLåter[0]['artists'][0]['name'])


ttk.Button(app, text='Lukk program', command=app.destroy).place(rely=1, relx=0.5)

app.mainloop()