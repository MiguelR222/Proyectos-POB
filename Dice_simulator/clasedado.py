from dado import DiceFrame
import tkinter as tk
from tkinter import ttk

class Dado:
    def __init__(self):
        self.window = tk.Tk()
        self.dado1 = DiceFrame(self.window, dice_number=2)
        self.dado2 = DiceFrame(self.window)
        self.create_widgets()
        self.window.mainloop()

    def create_widgets(self):
        self.roll_button = ttk.Button(self.window, text="Lanzar dado", command=self.lanzar)
        self.roll_button.pack()

    def lanzar(self):
        self.dado1.roll_dice()
        self.dado2.roll_dice()
 
if __name__ == "__main__":
    Dado()
 