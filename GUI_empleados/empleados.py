import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog
from tkinter.simpledialog import askstring
from tkinter import messagebox
import eclase as e
import edempleado as edi

class App:
    def __init__(self) -> None:
        self.window = tk.Tk()
        self.window.title("Empleados")

        foto= tk.PhotoImage(file= './img/enuevo.png')
        tk.Label(self.window, image=foto).grid(row=0,column=1, columnspan=2, sticky="WE")

        tk.Label(self.window, text="ID empleados").grid(row=1, column=0, sticky= "W")
        tk.Label(self.window, text="Nombre").grid(row=2, column=0, sticky= "W")
        tk.Label(self.window, text="Apellido").grid(row=3, column=0, sticky= "W")
        tk.Label(self.window, text="Sexo").grid(row=4, column=0, sticky= "W")
        tk.Label(self.window, text="Departamento").grid(row=7, column=0, sticky= "W")
        tk.Label(self.window, text="Sueldo").grid(row=8, column=0, sticky= "W")


        #Entradas de datos
        self.id= tk.IntVar(value= 0)
        tk.Entry(self.window, textvariable= self.id, width= 20).grid(row=1, column=1)
        self.name= tk.StringVar(value=" ")
        tk.Entry(self.window, textvariable= self.name, width= 20).grid(row=2, column=1)
        self.ln= tk.StringVar(value= " ")
        tk.Entry(self.window, textvariable= self.ln, width= 20).grid(row=3, column=1)
        self.sueldo= tk.IntVar(value=0)
        tk.Entry(self.window, textvariable= self.sueldo, width= 20).grid(row=8, column=1)


        #Combobox deptos

        self.departamento=ttk.Combobox(self.window, state="readyonly", width=20,  values= ['A','B','C'])
        self.departamento.grid(row=7, column=1)

        #Radiobotones
        self.a= tk.StringVar(value="h")
        ttk.Radiobutton(self.window, variable= self.a, value="h", text= "Hombre").grid(row=4, column=1)
        ttk.Radiobutton(self.window, variable= self.a, value="m", text= "Mujer").grid(row=5, column=1)

        #Acciones texto
        ttk.Button(self.window, text= "Borrar", command= self.borrar).grid(column=1, row=11, sticky= "WE")
        ttk.Button(self.window, text= "Agregar", command= self.agregar).grid(column=1, row=10, sticky= "WE")
        ttk.Button(self.window, text= "Actualizar", command= self.actualizar).grid(column=0, row=11, sticky= "WE")
        ttk.Button(self.window, text= "Buscar", command= self.buscar).grid(column=2, row=10, sticky="WE")
        ttk.Button(self.window, text= "Nuevo", command= self.nuevo).grid(column=0, row=10, sticky="WE")
        ttk.Button(self.window, text= "Salir", command=self.window.destroy). grid(column=2, row=11, sticky= "WE")
 
        self.window.mainloop()

    def agregar(self):
        emp= e.cemp(self.id.get(), self.name.get(), self.ln.get(),self.a.get(), self.departamento.get(), self.sueldo.get())
        edi.EmpleadoArchivo.agregar(emp)

    def borrar(self):
        # emp= e.cemp(self.id.get(), self.name.get(), self.ln.get(),self.a.get(), self.departamento.get(), self.sueldo.get())
        # edi.EmpleadoArchivo.borrar(emp)
        idb= simpledialog.askinteger("Busqueda","Escriba el ID a borrar", parent= self.window, minvalue=0, maxvalue=100)
        edi.EmpleadoArchivo.borrar(idb)

    def actualizar(self):
        emp= e.cemp(self.id.get(), self.name.get(), self.ln.get(),self.a.get(), self.departamento.get(), self.sueldo.get())
        edi.EmpleadoArchivo.actualizar(emp)

    def buscar(self):
        idb= simpledialog.askinteger("Busqueda","Escriba el ID", parent= self.window, minvalue=0, maxvalue=100)
        emp= edi.EmpleadoArchivo.buscar(idb)
        if emp is None:
            self.nuevo()
            messagebox.showinfo(message="El empleado no existe")
        else:
            self.id.set(emp.id)
            self.name.set(emp.name)
            self.ln.set(emp.ln)
            self.a.set(emp.sexo)
            self.departamento.set(emp.depto)
            self.sueldo.set(int(emp.sueldo))

        


    def nuevo(self):
          self.id.set(0)
          self.name.set("")
          self.ln.set("")
          self.a.set("h")
          self.sueldo.set(0)
          self.departamento.set("A")




if __name__== "__main__":
    App()