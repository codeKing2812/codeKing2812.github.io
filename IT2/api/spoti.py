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

app = Tk()
app.geometry("500x600")
main = ttk.Frame(app)
main.place(rely=0, relwidth=1)
#lager rammen for programmet

scroll = ttk.Scrollbar(app)
scroll.place(relx=1, anchor='ne', relheight=1)


ttk.Label(main, text='Dine siste likte låter er:').pack(pady=5)


def infoKnapp(låt):
    sangBoks = ttk.Frame(main).pack()
    i1 = ttk.Label(sangBoks, text='album: ' + låt['album']['name'])
    i2 = ttk.Label(sangBoks, text='artist: ' + låt['artists'][0]['name'])
    lukk = ttk.Button(sangBoks, text='lukk', command= lambda: [i1.forget(), i2.forget(), lukk.forget()])

    # skjulWidget(i1)
    # skjulWidget(i2)
    # skjulWidget(lukk)
    
    ttk.Button(sangBoks, text=låt['name'], command= lambda: [i1.pack(), i2.pack(), lukk.pack()]).pack()
                   
for låt in likteLåter:
    infoKnapp(låt)

# in_tekst = ''
# ttk.Entry(program,  textvariable = in_tekst)


# info1 = ttk.Label(main, text='album: ' + likteLåter[0]['album']['name'])
# info2 = ttk.Label(main, text='artist: ' + likteLåter[0]['artists'][0]['name'])


ttk.Button(main, text='Lukk program', command=app.destroy).pack()

app.mainloop()