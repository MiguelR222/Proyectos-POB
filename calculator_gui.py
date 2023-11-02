import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import Menu

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Calculator")
        self.window.resizable(False, False)

        #Numeros
        self.zero = tk.Button(self.window, text="0", width=5, height=2, command=lambda: self.add_number("0"))
        self.zero.grid(column=0, row=4, sticky='nsew')
        self.number1 = tk.Button(self.window, text="1", width=5, height=2, command=lambda: self.add_number("1"))
        self.number1.grid(column=0, row=1, sticky='nsew')
        self.number2 = tk.Button(self.window, text="2", width=5, height=2, command=lambda: self.add_number("2"))
        self.number2.grid(column=1, row=1, sticky='nsew')
        self.number3 = tk.Button(self.window, text="3", width=5, height=2, command=lambda: self.add_number("3"))
        self.number3.grid(column=2, row=1, sticky='nsew')
        self.number4 = tk.Button(self.window, text="4", width=5, height=2, command=lambda: self.add_number("4"))
        self.number4.grid(column=0, row=2, sticky='nsew')
        self.number5 = tk.Button(self.window, text="5", width=5, height=2, command=lambda: self.add_number("5"))
        self.number5.grid(column=1, row=2, sticky='nsew')
        self.number6 = tk.Button(self.window, text="6", width=5, height=2, command=lambda: self.add_number("6"))
        self.number6.grid(column=2, row=2, sticky='nsew')
        self.number7 = tk.Button(self.window, text="7", width=5, height=2, command=lambda: self.add_number("7"))
        self.number7.grid(column=0, row=3, sticky='nsew')
        self.number8 = tk.Button(self.window, text="8", width=5, height=2, command=lambda: self.add_number("8"))
        self.number8.grid(column=1, row=3, sticky='nsew')
        self.number9 = tk.Button(self.window, text="9", width=5, height=2, command=lambda: self.add_number("9"))
        self.number9.grid(column=2, row=3, sticky='nsew')

        #Operadores
        self.multiplicar = tk.Button(self.window, text="X", width=5, height=2, command=lambda: self.add_operator("*"))
        self.multiplicar.grid(column=3, row=1, sticky='nsew')
        self.dividir = tk.Button(self.window, text="/", width=5, height=2, command=lambda: self.add_operator("/"))
        self.dividir.grid(column=3, row=2, sticky='nsew')
        self.sumar = tk.Button(self.window, text="+", width=5, height=2, command=lambda: self.add_operator("+"))
        self.sumar.grid(column=3, row=3, sticky='nsew')
        self.restar = tk.Button(self.window, text="-", width=5, height=2, command=lambda: self.add_operator("-"))
        self.restar.grid(column=3, row=4, sticky='nsew')
        self.igual = tk.Button(self.window, text="=", width=5, height=2, command=self.calculate)
        self.igual.grid(column=2, row=4, sticky='nsew')

        #Borrar
        self.borrar = tk.Button(self.window, text="CE", width=5, height=2, background='orange', command=self.clear)
        self.borrar.grid(column=3, row=0, sticky='nsew')

        #Punto
        self.punto = tk.Button(self.window, text=".", width=5, height=2, command=lambda: self.add_number("."))
        self.punto.grid(column=1, row=4, sticky='nsew')

        #Display
        self.display = tk.Entry(self.window, width=15, font=("Arial", 20), justify="right")
        self.display.grid(column=0, row=0, columnspan=3, sticky='nsew')

        self.window.mainloop()

    def add_number(self, number):
        self.display.insert(tk.END, number)
    
    def add_operator(self, operator):
        self.display.insert(tk.END, operator)
    
    def calculate(self):
        try:
            result = eval(self.display.get())
            self.clear()
            self.display.insert(tk.END, result)
        except Exception as e:
            messagebox.showerror("Error")

    def clear(self):
        self.display.delete(0, tk.END)

if __name__ == "__main__":
    Calculator()