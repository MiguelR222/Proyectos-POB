import tkinter as tk
from tkinter import ttk     
from tkinter import filedialog, messagebox
import tkinter.scrolledtext as st
import os

class App():
    def __init__(self) -> None:
        self.window =tk.Tk()
        self.window.title("Bloc de notas")
        self.menu()
        self.sc = st.ScrolledText(self.window, width=80, height=30)
        self.sc.grid(row=0, column=0, sticky='nsew')
        self.window.grid_rowconfigure(0, weight=1)
        self.window.grid_columnconfigure(0, weight=1)
        self.window.mainloop()

    def menu(self):
        self.menu_bar = tk.Menu()

        menu_archivo = tk.Menu(self.menu_bar, tearoff= False)
        self.menu_bar.add_cascade(menu= menu_archivo, label= "Archivo")
        menu_archivo.add_command(label="Nuevo", command= self.nuevo)
        #Abrir
        menu_archivo.add_command(label="Abrir...", command= self.abrir)
        #Guardar
        menu_archivo.add_command(label="Guardar...", command= self.guardar)
        #Salir
        menu_archivo.add_command(label="Salir", command= self.window.destroy)
        
        menu_ayuda = tk.Menu(self.menu_bar, tearoff=False)
        self.menu_bar.add_cascade(menu=menu_ayuda, label="Ayuda")
        #Acerca
        menu_ayuda.add_command(label="Acerca...", command=self.acerca)
    
        self.window.config(menu=self.menu_bar)

    def nuevo(self):
        self.sc.delete("1.0","end")

    def abrir(self):
        file= filedialog.askopenfile()
        if file:
            self.window.title(f"{os.path.basename(file.name)} Bloc de Notas")
            self.sc.delete("1.0", "end")
            self.sc.insert("1.0", file.read())
            file.close()
    def guardar(self):
        file = filedialog.asksaveasfile(defaultextension=".txt",
                                        filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")])
        if file:
            c = self.sc.get("1.0", "end-1c")
            file.write(c)
            file.close()

    def acerca(self):
        messagebox.showinfo(message="Bloc de Notas hecho en Python")


App()