import tkinter as tk
import random


class DiceFrame(tk.Frame):
    def __init__(self, master=None, dice_number=1) -> None:
        super().__init__(master)
        self.dice_label = tk.Label(self.master)
        self.dice_number= dice_number
        dice_image = tk.PhotoImage(file=f"img/dado{self.dice_number}.png")
        self.dice_label.configure(image=dice_image)
        self.dice_label.pack()
        self.dice_label.image = dice_image

    @property
    def dice_number(self):
        return self.__dice_number
    
    @dice_number.setter
    def dice_number(self, dice_number):
        if not isinstance (dice_number, int):
            raise TypeError("El número del dado debe ser un entero")
        if dice_number not in range(1,6):
            raise ValueError("El número del dado debe ser un entero entre 1 y 6")
        self.__dice_number = dice_number


    def roll_dice(self):
        dice_number = random.randint(1, 6)
        dice_image = tk.PhotoImage(file=f"img/dado{dice_number}.png")
        self.dice_label.configure(image=dice_image)
        self.dice_label.image = dice_image
        print(dice_number)

    

