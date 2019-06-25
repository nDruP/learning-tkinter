import tkinter as tk
from dice import Dice


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_dice(4)
        
    def create_dice(self, faces):
        
        
root = tk.Tk()
app = Application(master=root)
app.mainloop()

