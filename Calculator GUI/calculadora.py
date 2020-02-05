from tkinter import * 

root=Tk()
root.title("Calculadora chida")
root.resizable(1,1)
root.iconbitmap("538560_1.ico")
root.config(bg="grey")
root.config(bd=7)
root.config(relief="groove")

frame=Frame(root, width=1000, height=1000)
frame.pack()

#Funciones

listaNumero=[]
num=IntVar()
ope=IntVar()
minumero=IntVar()
num1=IntVar()
num2=IntVar()
cuenta=IntVar()


def nueve():
	num.set(9)
	listaNumero.append(num.get())

def ocho():
	num.set(8)
	listaNumero.append(num.get())

def siete():
	num.set(7)
	listaNumero.append(num.get())

def seis():
	num.set(6)
	listaNumero.append(num.get())

def cinco():
	num.set(5)
	listaNumero.append(num.get())

def cuatro():
	num.set(4)
	listaNumero.append(num.get())

def tres():
	num.set(3)
	listaNumero.append(num.get())

def dos():
	num.set(2)
	listaNumero.append(num.get())

def uno():
	num.set(1)
	listaNumero.append(num.get())

def cero():
	num.set(0)
	listaNumero.append(num.get())

def punto():
	minumero.set(".")

def delete():
	minumero.set(0)
	num1.set(0)
	num2.set(0)
	cuenta.set(0)

def por():
	ope.set(1)
	if (cuenta.get() == 0):
		num1.set(notacion(listaNumero))
		minumero.set(num1.get())
		cuenta.set(1)
	elif (cuenta.get()==1):
		num2.set(notacion(listaNumero))
		minumero.set(num2.get())
		cuenta.set(2)
	elif (cuenta.get()==2):
		num1.set(num2.get())
		num2.set(notacion(listaNumero))
		minumero.set(num2.get())
		cuenta.set(3)
		
	else:
		num1.set(num2.get())
		num2.set(notacion(listaNumero))
		minumero.set(num2.get())

	listaNumero.clear()

def mas():
	ope.set(2)
	if (cuenta.get() == 0):
		num1.set(notacion(listaNumero))
		minumero.set(num1.get())
		cuenta.set(1)
	elif (cuenta.get()==1):
		num2.set(notacion(listaNumero))
		minumero.set(num2.get())
		cuenta.set(2)
	elif (cuenta.get()==2):
		num1.set(num2.get())
		num2.set(notacion(listaNumero))
		minumero.set(num2.get())
		cuenta.set(3)
		
	else:
		num1.set(num2.get())
		num2.set(notacion(listaNumero))
		minumero.set(num2.get())

	listaNumero.clear()


def entre():
	ope.set(3)
	if (cuenta.get() == 0):
		num1.set(notacion(listaNumero))
		minumero.set(num1.get())
		cuenta.set(1)
	elif (cuenta.get()==1):
		num2.set(notacion(listaNumero))
		minumero.set(num2.get())
		cuenta.set(2)
	elif (cuenta.get()==2):
		num1.set(num2.get())
		num2.set(notacion(listaNumero))
		minumero.set(num2.get())
		cuenta.set(3)
		
	else:
		num1.set(num2.get())
		num2.set(notacion(listaNumero))
		minumero.set(num2.get())

	listaNumero.clear()

def menos():
	ope.set(4)
	if (cuenta.get() == 0):
		num1.set(notacion(listaNumero))
		minumero.set(num1.get())
		cuenta.set(1)
	elif (cuenta.get()==1):
		num2.set(notacion(listaNumero))
		minumero.set(num2.get())
		cuenta.set(2)
	elif (cuenta.get()==2):
		num1.set(num2.get())
		num2.set(notacion(listaNumero))
		minumero.set(num2.get())
		cuenta.set(3)
		
	else:
		num1.set(num2.get())
		num2.set(notacion(listaNumero))
		minumero.set(num2.get())

	print("num1 es: ", num1.get())
	print("num2 es: ", num2.get())

	listaNumero.clear()

def ac():
	minumero.set(0)
	num1.set(0)
	num2.set(0)
	cuenta.set(0)

def igual():
	if ope.get() == 1: #multiplicacion
		minumero.set(num1.get()*num2.get())		

	if ope.get() == 2: #suma
		minumero.set(num1.get()+num2.get())

	if ope.get() == 3: #division
		minumero.set(num1.get()/num2.get())

	if ope.get() == 4: #resta
		minumero.set(num1.get()-num2.get())

def notacion(n):
	ac=0
	cont=0
	large=len(n)
	for i in n:
		x=i*10**(large-cont-1)
		y=large-cont
		ac=ac+x
		cont+=1
	return ac


#Funciones

pantalla=Entry(frame, textvariable=minumero)
pantalla.config(background="black", fg="#03f943",justify="right")
pantalla.grid(row=0, column=0, padx=5, pady=5, columnspan=5)

boton9=Button(frame, text="9", command=nueve, width=3)
boton9.grid(row=1, column=2, padx=5, pady=5)

boton8=Button(frame, text="8", command=ocho, width=3)
boton8.grid(row=1, column=1, padx=5, pady=5)

boton7=Button(frame, text="7", command=siete, width=3)
boton7.grid(row=1, column=0, padx=2, pady=2)

boton6=Button(frame, text="6", command=seis, width=3)
boton6.grid(row=2, column=2, padx=2, pady=2)

boton5=Button(frame, text="5", command=cinco, width=3)
boton5.grid(row=2, column=1, padx=2, pady=2)

boton4=Button(frame, text="4", command=cuatro, width=3)
boton4.grid(row=2, column=0, padx=2, pady=2)

boton3=Button(frame, text="3", command=tres, width=3)
boton3.grid(row=3, column=2, padx=2, pady=2)

boton2=Button(frame, text="2", command=dos, width=3)
boton2.grid(row=3, column=1, padx=2, pady=2)

boton1=Button(frame, text="1", command=uno, width=3)
boton1.grid(row=3, column=0, padx=2, pady=2)

boton0=Button(frame, text="0", command=cero, width=3)
boton0.grid(row=4, column=1, padx=2, pady=2)

botonPunto=Button(frame, text=".", command=punto, width=3)
botonPunto.grid(row=4, column=2, padx=2, pady=2)

botonDEL=Button(frame, text="DEL", command=delete, width=3)
botonDEL.grid(row=1, column=3, padx=2, pady=2)

botonX=Button(frame, text= "x", command=por, width=3)
botonX.grid(row=2, column=3, padx=2, pady=2)

botonMas=Button(frame, text="+", command=mas, width=3)
botonMas.grid(row=3, column=3, padx=2, pady=2)

botonDiv=Button(frame, text="÷", command=entre, width=3)
botonDiv.grid(row=4, column=3, padx=2, pady=2)

botonAC=Button(frame, text="AC", command=ac, width=3)
botonAC.grid(row=1,column=4, padx=2, pady=2)

botonMinus=Button(frame, text="-", command=menos, width=3)
botonMinus.grid(row=2,column=4, padx=2, pady=2)

botonIgual=Button(frame, text="=", command=igual, width=3)
botonIgual.grid(row=3,column=4, padx=2, pady=2)

root.mainloop()