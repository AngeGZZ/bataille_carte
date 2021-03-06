# Creating window tkinter
from tkinter import *


def window():
    fenetre = Tk()
    fenetre.title("Bataille")
    fenetre.config(bg="#87CEEB")
    fenetre.geometry("1200x800")
    fenetre.resizable(width=False, height=False)
    # fenetre.mainloop()
