#Importar librerías

from tkinter import *
from datetime import date

# Ventana de inicializaión
root = Tk()
root.geometry('280x300')
root.resizable(0,0)
root.title("Calculador de edad")
statement = Label(root)

#Definiendo la función para calcular la edad

def ageCalc():
    global statement
    statement.destroy()
    today = date.today()
    birthDate = date(int(yearEntry.get()), int(
        monthEntry.get()), int(dayEntry.get()))
    age = today.year - birthDate.year
    
    if today.month < birthDate.month or today.month == birthDate.month and today.day < birthDate.day:
        age -= 1
    statement = Label(text=f"La edad de {nameValue.get()} es {age}.")
    statement.grid(row=6,column=1,pady=15)
    
    ##Creando un label para el nombre de la persona
    
l1 = Label(text="Nombre: ")
l1.grid(row=1,column=0)
nameValue = StringVar()
    
    ##creando la caja de entrada para el input
nameEntry =  Entry(root, textvariable = nameValue)
nameEntry.grid(row=1,column=1, padx=10,pady=10)
    
    #Label para el año de nacimiento de la persona
    
l2 = Label(text="Año: ")
l2.grid(row=2,column=0)
yearValue=StringVar()
yearEntry = Entry(root,textvariable=yearValue)
yearEntry.grid(row=2,column=1,padx=10,pady=10)
    
# Label para los meses del usuario

l3 = Label(text="Mes: ")
l3.grid(row=3,column=0)
monthValue =  StringVar()
monthEntry= Entry(root, textvariable=monthValue)
monthEntry.grid(row=3,column=1,padx=10,pady=10)

#Label para el día/fecha del usuario
l4 = Label(text="Día: ")
l4.grid(row=4, column=0)
dayValue = StringVar()
dayEntry = Entry(root,textvariable=dayValue)
dayEntry.grid(row=4,column=1,padx=10,pady=10)

#crear un boton que calcule la edad

button = Button(text="Calculadr de edad", command=ageCalc)
button.grid(row=5,column=1)

#El loop infinito

root.mainloop()






