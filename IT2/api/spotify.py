import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="238744af4cc644688b90c26fc9a73b62",
                                               client_secret="b97149e52b1a4d559ed8906d20a7f66f",
                                               redirect_uri="http://localhost:3000",
                                               scope="user-library-read"))

results = sp.current_user_saved_tracks()
likteLåter=[]
for i, item in enumerate(results['items']):
    track = item['track']

    likteLåter.append(track['name'])

    print(i, track['artists'][0]['name'], " – ", track['name'])

print(likteLåter[0]['artists'][0]['name'])



from tkinter import *
from tkinter import ttk, simpledialog



root = Tk()
program = ttk.Frame(root, padding=10)
program.grid()
ttk.Label(program, text='din siste likte låt er:').grid(column=0, row=0)
ttk.Label(program, text=likteLåter).grid(column=0, row=0)
ttk.Entry(program)
ttk.Button(program, text="Quit", command=root.destroy).grid(column=0, row=1)
root.mainloop()
