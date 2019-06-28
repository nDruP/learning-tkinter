from random import randint
import tkinter as tk


class Dice:
    def __init__(self, faces):
        self.faces = faces
        self.history = []
        
    def roll(self, num_rolls=1):
        for _ in range(num_rolls):
            self.history.append(randint(1, self.faces))
        return self.history[-1*num_rolls:]
        
    def roll_display(self, num_roll_input):
        try:
            roll_result = self.roll(int(num_roll_input))
        except:
            roll_result = self.roll()
        finally:
            self.dice_hist["text"] = str(roll_result)[1:-1]
    
    def tk_frame(self, tk_root):
        self.dice_frame = tk.Frame(tk_root)
        self.dice_frame.pack(side="left")
        
        self.dice_roll = tk.Button(self.dice_frame)
        self.dice_roll["text"] = "Roll"
        self.dice_roll["command"] = lambda: self.roll_display(self.num_rolls.get())
        self.dice_roll.grid(row=0)

        self.num_rolls = tk.Spinbox(self.dice_frame, from_=1, to=50)
        self.num_rolls.grid(row=1)

        self.dice_hist = tk.Label(self.dice_frame)
        self.dice_hist["text"] = "wow"
        self.dice_hist.grid(row=2)

    
if __name__ == '__main__':
    d = {4: Dice(4), 6: Dice(6), 8: Dice(8),
         10: Dice(10), 12: Dice(12), 20: Dice(20)}

    root = tk.Tk()
    
    for x in d.keys():
        d[x].tk_frame(root)

    root.mainloop()
