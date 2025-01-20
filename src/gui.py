import tkinter 
from tkinter import ttk
import sv_ttk

class MyGUI:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.geometry('500x800')

        sv_ttk.set_theme("dark")

        self.currTemp = ttk.Label(self.root, text="")
        self.currTemp.pack()

        self.currHigh = ttk.Label(self.root, text="")
        self.currHigh.pack()

        self.currLow = ttk.Label(self.root, text="")
        self.currLow.pack()
    
    def run(self):
        self.root.mainloop()
        