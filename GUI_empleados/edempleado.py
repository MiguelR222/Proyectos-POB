import eclase as e
import os
import tkinter as tk
from tkinter import messagebox

class EmpleadoArchivo:
    @staticmethod
    def agregar(emp:e.cemp):
        f1= open("empleados.txt","a")
        doc= open("empleados.txt","a")
        doc.write(f"{emp.id}, {emp.name}, {emp.ln}, {emp.sexo}, {emp.depto}, {emp.sueldo}\n")
        doc.close()

    @staticmethod
    def buscar(id:int)->e.cemp:
        f=open('empleados.txt', 'r')
        
        empr= None
        for empleado in f:
            emp= empleado.split(",")
            idemp= int(emp[0])
            if id == idemp:
                empr= e.cemp(idemp, emp[1], emp[2], emp[3], emp[4], int(emp[5]))
                break
            
        f.close()
        return empr
        
    @staticmethod
    def borrar(a:int):
        f1= open("empleados.txt","r")
        f2=open("empleados2.txt","a")
        for empleado in f1:
            en=empleado.split(", ")
            ide= int(en[0])
            if a not in f1:
                messagebox.showinfo(message="No existe empleado con ese ID")
            if (a!=ide):
                f2.write(empleado)

        f1.close()    
        os.remove("empleados.txt")
        f2.close()
        os.rename("empleados2.txt", "empleados.txt")


    @staticmethod
    def actualizar(emp:e.cemp):
        f1= open("empleados.txt", "r")
        f2= open("empleados2.txt", "w")
        for empleado in f1:
            e= empleado.split(",")
            ide= int(e[0])
            if (emp.id != ide):
                f2.write(empleado)
            else:
                f2.write(emp.__str__())
        f1.close()
        f2.close()
        os.remove("empleados.txt")
        os.rename("empleados2.txt","empleados.txt")