from ytmusicapi import YTMusic
from tkinter import *
from tkinter import ttk, simpledialog


api = YTMusic()

søkeresultat = api.search('dire straits')


root = Tk()
program = ttk.Frame(root, padding=10)
program.grid()
ttk.Label(program, text=søkeresultat[0]['artists'][0]['name']).grid(column=0, row=0)
ttk.Entry(program)
ttk.Button(program, text="Quit", command=root.destroy).grid(column=0, row=1)
root.mainloop()
