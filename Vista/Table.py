from tkinter import *
from tkinter import ttk
import tkinter as tk

class Table:
    def __init__(self):
        self.Ventana = Tk()
        self.Ventana.title("ZINOBE")
        self.Ventana.geometry("700x400")
        
    def show_Table(self,countrys, TTotal, TPromedio, TMinimo, TMaximo):
        table = ttk.Treeview(self.Ventana)

        table["columns"]=("one","two","three")
        table.column("#0", width=100, minwidth=50, stretch=tk.NO)
        table.column("one", width=150, minwidth=150, stretch=tk.NO)
        table.column("two", width=280, minwidth=280)
        table.column("three", width=150, minwidth=100, stretch=tk.NO)

        table.heading("#0",text="Region",anchor=tk.W)
        table.heading("one", text="Country",anchor=tk.W)
        table.heading("two", text="Language",anchor=tk.W)
        table.heading("three", text="Time",anchor=tk.W)

        for i in reversed(countrys):
            table.insert("",0,text=i['region'], values=(i['country'],i['language'],i['time']))
        
        table.pack(side=tk.TOP,fill=tk.X)

        label1= Label(self.Ventana, text="Tiempo Total: "+TTotal)
        label2= Label(self.Ventana, text="Tiempo Promedio: "+TPromedio)
        label3= Label(self.Ventana, text="Tiempo Minimo: "+TMinimo)
        label4= Label(self.Ventana, text="Tiempo Maximo: "+TMaximo)

        label1.place(x=100, y=250, width=200, height=30)
        label2.place(x=400, y=250, width=200, height=30)
        label3.place(x=100, y=300, width=200, height=30)
        label4.place(x=400, y=300, width=200, height=30)
        self.Ventana.mainloop()
