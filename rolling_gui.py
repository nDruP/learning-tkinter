import tkinter as tk
from dice import Dice


HEIGHT = 400
WIDTH = 600

d = {4: Dice(4), 6: Dice(6), 8: Dice(8),
     10: Dice(10), 12: Dice(12), 20: Dice(20)}

def roll_check(faces, spin_result):
    x = []
    try:
        x = d[faces].roll(int(spin_result))
    except:
        x = d[faces].roll()
    dice_hist["text"] = str(x)

# def create_dice_frame(master, faces):

root = tk.Tk()


bg_canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
bg_canvas.pack()

dice_frame = tk.Frame(root)
dice_frame.pack()

dice_roll = tk.Button(dice_frame)
dice_roll["text"] = "Roll"
dice_roll["command"] = lambda: roll_check(4, num_rolls.get())
dice_roll.grid(row=0)

num_rolls = tk.Spinbox(dice_frame, from_=1, to=50)
num_rolls.grid(row=1)

dice_hist = tk.Label(dice_frame)
dice_hist["text"] = "wow"
dice_hist.grid(row=2)

root.mainloop()

