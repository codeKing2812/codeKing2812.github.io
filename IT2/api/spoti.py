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
app.geometry("700x350")
#lager rammen for programmet


ttk.Label(app, text='Din siste likte låt er:').pack()
ttk.Label(app, text=likteLåter[2]['name']).pack()

# in_tekst = ''
# ttk.Entry(program,  textvariable = in_tekst).pack()


info1 = ttk.Label(app, text='album: ' + likteLåter[2]['album']['name'])

def visInfo():
    info1.pack(pady=10)

def skjulInfo():
    info1.pack_forget()



ttk.Button(app, text='Se mer info', command=visInfo()).pack()


ttk.Button(app, text='Lukk program', command=app.destroy).pack()

app.mainloop()
