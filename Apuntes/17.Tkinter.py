#############
## TKINTER ##
#############

# Componente raíz
import tkinter

raiz = tkinter.Tk()
raiz.title("Mi programa")

raiz.mainloop()

# Componente frame
# Permite introducir otros componentes dentro
import tkinter

raiz = tkinter.Tk()
raiz.title("Mi programa")


frame = tkinter.Frame(raiz)
frame.config(bg="blue",width=400,height=300)
frame.pack() # Para mostrar el elemento

raiz.mainloop()

# Componente label

import tkinter

raiz = tkinter.Tk()
raiz.title("Mi programa")

texto = "Hola mundo"
etiqueta = tkinter.Label(raiz,text=texto)
etiqueta.config(fg="green",bg="lightgrey",font=("Cortana",30))
etiqueta.pack()

raiz.mainloop()

# Componente Entry

import tkinter

raiz = tkinter.Tk()
raiz.title("Mi programa")

entrada= tkinter.Entry(raiz)
entrada.config(justify="center")
entrada.pack()

raiz.mainloop()

# Componente text (campo comentarios)

import tkinter

raiz = tkinter.Tk()
raiz.title("Mi programa")

entrada = tkinter.Text(raiz)
entrada.config(width="20", height=10, font=("Verdana",15), padx=10,pady=10, fg="green")
entrada.pack()

raiz.mainloop()

# Componente button

import tkinter

raiz = tkinter.Tk()
raiz.title("Mi programa")

def accion():
		print("Hola mundo")

boton = tkinter.Button(raiz,text="Ejecutar", command=accion)
boton.pack()

raiz.mainloop()

# Componente radiobutton

import tkinter

raiz = tkinter.Tk()
raiz.title("Mi programa")

def seleccion():
	print("La opción seleccionada es {}".format(opcion.get()))

opcion = tkinter.IntVar()

radiobutton1 = tkinter.Radiobutton(raiz,text="Opcion 1", variable = opcion, value=1, command= seleccion)
radiobutton1.pack()

radiobutton1 = tkinter.Radiobutton(raiz,text="Opcion 2", variable = opcion, value=2, command= seleccion)
radiobutton1.pack()

radiobutton1 = tkinter.Radiobutton(raiz,text="Opcion 3", variable = opcion, value=3, command= seleccion)
radiobutton1.pack()
raiz.mainloop()

# Componente checkbutton

import tkinter

raiz = tkinter.Tk()
raiz.title("Mi programa")

def verificar():
	valor = check1.get()
	if (valor ==1):
		print("El check está activado")
	else:
		print("El check está desactivado")

check1 = tkinter.IntVar()

boton1 = tkinter.Checkbutton(raiz, text="Opción 1", variable=check1, onvalue=1, offvalue=0, command=verificar)
boton1.pack()

raiz.mainloop()

# Componente messagebox

import tkinter
from tkinter import messagebox

raiz = tkinter.Tk()
raiz.title("Mi programa")

def avisar():
	tkinter.messagebox.showinfo("Titulo", "Mensaje con la información")

boton = tkinter.Button(raiz, text="Pulsar para aviso", command=avisar)
boton.pack()

raiz.mainloop()