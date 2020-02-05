from tkinter import *
from tkinter import messagebox
import sqlite3

root=Tk()
barraMenu=Menu(root)
root.config(menu=barraMenu)
root.title("CRUD")

frame=Frame(root)
frame.pack()

frameBotones=Frame(root)
frameBotones.pack()

#variables

Identificador=StringVar()
Identificador.set("")
Password=StringVar()
Nombre=StringVar()
Apellido=StringVar()
Direccion=StringVar()

#variables 

#funciones

def Conectar():
	valor=messagebox.askokcancel("Conectar", "¿Deseas crear una nueva base de datos?")
	if valor:
		try:
			miConexion=sqlite3.connect("base_de_datos")
			miCursor=miConexion.cursor()
			miCursor.execute('''
				CREATE TABLE DATOS_PERSONAS(
				ID INTEGER PRIMARY KEY AUTOINCREMENT,
				NOMBRE_PERSONA VARCHAR(25),
				PASSWORD VARCHAR(50),
				APELLIDO VARCHAR(30),
				DIRECCION VARCHAR(50),
				COMENTARIOS VARCHAR(100))
				
				''')
			miConexion.commit()
			miConexion.close()
			messagebox.showwarning("Ok", "Base de datos creada con éxito.")
		except:
			messagebox.showwarning("Error", "Ya has creado una base de datos.")

def Salir():
	valor=messagebox.askokcancel("Salir", "¿Deseas salir de la aplicación?")

	if valor:
		root.destroy()

def Create():
	miConexion=sqlite3.connect("base_de_datos")
	miCursor=miConexion.cursor()
	miLista=[(Nombre.get(),Password.get(),Apellido.get(),Direccion.get(),cuadroComentarios.get(1.0, END))]
	miCursor.executemany("INSERT INTO DATOS_PERSONAS VALUES (NULL, ?,?,?,?,?)", miLista)
	miConexion.commit()
	miConexion.close()
	messagebox.showwarning("Create", "Datos añadidos con éxito.")

def Read():
	try:	
		cuadroComentarios.delete(1.0, END)
		Password.set("")
		Nombre.set("")
		Apellido.set("")
		Direccion.set("")
		miConexion=sqlite3.connect("base_de_datos")
		miCursor=miConexion.cursor()
		miCursor.execute("SELECT * FROM DATOS_PERSONAS WHERE ID=" + Identificador.get())
		obtained_data=miCursor.fetchall()
		vector=[]
		for i in obtained_data[0]:
			vector.append(i)
		Identificador.set(vector[0])
		Nombre.set(vector[1])
		Password.set(vector[2])
		Apellido.set(vector[3])
		Direccion.set(vector[4])
		cuadroComentarios.insert(1.0, vector[5])
		miConexion.commit()
		miConexion.close()
	except:
		messagebox.showwarning("Error", "Has introducido un ID inexistente.")

def Update():
	miConexion=sqlite3.connect("base_de_datos")
	miCursor=miConexion.cursor()
	miCursor.execute("UPDATE DATOS_PERSONAS SET NOMBRE_PERSONA='" + Nombre.get() + "'WHERE ID=" + Identificador.get())
	miCursor.execute("UPDATE DATOS_PERSONAS SET PASSWORD='" + Password.get() + "'WHERE ID=" + Identificador.get())
	miCursor.execute("UPDATE DATOS_PERSONAS SET APELLIDO='" + Apellido.get() + "'WHERE ID=" + Identificador.get())
	miCursor.execute("UPDATE DATOS_PERSONAS SET DIRECCION='" + Direccion.get() + "'WHERE ID=" + Identificador.get())
	miCursor.execute("UPDATE DATOS_PERSONAS SET COMENTARIOS='" + cuadroComentarios.get("1.0", END) + "'WHERE ID=" + Identificador.get())
	miConexion.commit()
	miConexion.close()
	messagebox.showwarning("Update", "Datos actualizados con éxito.")

def Delete():
	try:
		miConexion=sqlite3.connect("base_de_datos")
		miCursor=miConexion.cursor()
		miCursor.execute("DELETE FROM DATOS_PERSONAS WHERE ID="+Identificador.get())
		miConexion.commit()
		miConexion.close()
		messagebox.showinfo("Delete", "Datos eliminados con éxito.")
	except:
		messagebox.showwarning("Error", "No has escrito ningún ID.")

def Borrar():
	Identificador.set("")
	Password.set("")
	Nombre.set("")
	Apellido.set("")
	Direccion.set("")
	cuadroComentarios.delete(1.0, END)
	
#funciones


#labels y cuadros de texto

labelID=Label(frame, text="ID:", padx=20, pady=10)
labelID.grid(row=0, column=0)

cuadroID=Entry(frame, textvariable=Identificador, justify="right")
cuadroID.config(background="#0087ff", fg="white")
cuadroID.grid(row=0, column=1, padx=10, pady=10)

labelNombre=Label(frame, text="Nombre:", padx=20, pady=10)
labelNombre.grid(row=1, column=0)

cuadroNombre=Entry(frame, textvariable=Nombre, justify="right")
cuadroNombre.config(background="#0087ff", fg="white")
cuadroNombre.grid(row=1, column=1)

labelPassword=Label(frame, text="Contraseña:", padx=20, pady=10)
labelPassword.grid(row=2, column=0)

cuadroPassword=Entry(frame, textvariable=Password, justify="right")
cuadroPassword.grid(row=2, column=1, padx=10, pady=10)
cuadroPassword.config(background="#0087ff", fg="white")
cuadroPassword.config(show="*")

labelApellido=Label(frame, text="Apellido:", padx=20, pady=10)
labelApellido.grid(row=3, column=0)

cuadroApellido=Entry(frame, textvariable=Apellido, justify="right")
cuadroApellido.config(background="#0087ff", fg="white")
cuadroApellido.grid(row=3, column=1)

labelDireccion=Label(frame, text="Direccion:", padx=20, pady=10)
labelDireccion.grid(row=4, column=0)

cuadroDireccion=Entry(frame, textvariable=Direccion, justify="right")
cuadroDireccion.config(background="#0087ff", fg="white")
cuadroDireccion.grid(row=4, column=1)

labelComentarios=Label(frame, text="Comentarios:", padx=20, pady=10)
labelComentarios.grid(row=5, column=0)

cuadroComentarios=Text(frame, width=16, height=5)
cuadroComentarios.config(background="#0087ff", fg="white")
cuadroComentarios.grid(row=5, column=1, padx=10, pady=10)
scrollVert=Scrollbar(frame, command=cuadroComentarios.yview)
scrollVert.grid(row=5, column=2, sticky="nsew")
cuadroComentarios.config(yscrollcommand=scrollVert.set)

#labels y cuadros de texto

#botones

botonCreate=Button(frameBotones, text="Create", width=6, command=Create)
botonCreate.grid(row=0, column=0, padx=10, pady=10)

botonRead=Button(frameBotones, text="Read", width=6, command=Read)
botonRead.grid(row=0, column=1, padx=10, pady=10)

botonUpdate=Button(frameBotones, text="Update", width=6, command=Update)
botonUpdate.grid(row=0, column=2, padx=10, pady=10)

botonDelete=Button(frameBotones, text="Delete", width=6, command=Delete)
botonDelete.grid(row=0, column=3, padx=10, pady=10)

#botones

#menu

BDmenu=Menu(barraMenu, tearoff=0)
BDmenu.add_command(label="Conectar", command=Conectar)
BDmenu.add_command(label="Salir", command=Salir)

menuBorrar=Menu(barraMenu, tearoff=0)
menuBorrar.add_command(label="Borrar campos", command=Borrar)

CRUDmenu=Menu(barraMenu, tearoff=0)
CRUDmenu.add_command(label="Create", command=Create)
CRUDmenu.add_command(label="Read", command=Read)
CRUDmenu.add_command(label="Update", command=Update)
CRUDmenu.add_command(label="Delete", command=Delete)

barraMenu.add_cascade(label="BBDD", menu=BDmenu)
barraMenu.add_cascade(label="Borrar", menu=menuBorrar)
barraMenu.add_cascade(label="CRUD", menu=CRUDmenu)

#menu

root.mainloop()