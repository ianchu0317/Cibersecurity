#Ian Chen 
#Importamos primero el módulo tkinter para la interfaz gráfica
from tkinter import * 

#Creamos nuestra propia ventana y la llamamos "Simple Calculator"
root = Tk()
root.title("Simple Calculator_Ian XD")

#Creamos una barra de entrada
introducir = Entry(root, width=40, borderwidth=2,fg="black",bg="white")
introducir.grid(row=0, column=0, columnspan=4, padx=10, pady=30)

#Definimos la función de los teclados para que puedan introducir
def click(number):
    current = introducir.get()
    introducir.delete(0, END)
    introducir.insert(0, str(current)+str(number)) 

# Creamos la funcion de eliminar contenido CLEAR
def clear():
    introducir.delete(0, END)

#Creamos la función de la suma y globalizamos el primer número 
def suma():
    first_number = introducir.get()
    global fstn
    fstn = int(first_number)
    introducir.delete(0, END)
    second = introducir.get()
    global operacion
    operacion = "+"

#Creamos la función de la resta
def resta():
    first_number = introducir.get()
    global fstn
    fstn = int(first_number)
    introducir.delete(0, END)
    global operacion
    operacion = "-"

#Creamos la función de la multiplicación
def multi():
    first_number = introducir.get()
    global fstn
    fstn = int(first_number)
    introducir.delete(0, END)
    global operacion
    operacion = "X"

#Creamos la funcion de la división
def divi():
    first_number = introducir.get()
    global fstn
    fstn = int(first_number)
    introducir.delete(0, END)
    global operacion
    operacion = "/"

#Creamos la funcion cuadrada 
def square():
    first_number = introducir.get()
    global fstn
    fstn = int(first_number)
    introducir.delete(0, END)
    global operacion
    operacion = "**"

#Creamos la funcion de raiz
def roott():
    first_number = introducir.get()
    global fstn
    fstn = int(first_number)
    introducir.delete(0, END)
    global operacion
    operacion = "√"

#Definimos el botón de Igual
def equal():
    second = introducir.get()
    introducir.delete(0,END)

    if str(operacion) == "+":
        introducir.insert(0, fstn + int(second))
    elif str(operacion) == "-":
        introducir.insert(0, fstn - int(second))
    elif str(operacion) == "X":
        introducir.insert(0, fstn * int(second))
    elif str(operacion) == "/":
        introducir.insert(0, fstn / int(second))
    elif str(operacion) == "**":
        introducir.insert(0, pow(fstn, int(second)))
        introducir.insert(0, fstn / int(second))
    elif str(operacion) == "√":
        import math
        introducir.insert(0, math.sqrt(fstn))
 
# Aplicamos la función para poder introducir botones, y definimos su tamaño y su texto 
# Utilizamos lamnda para asignar el valor de la funcion de cada botón

button_7 = Button(root, text="7", padx=40, pady=40, command= lambda: click(7))
button_8 = Button(root, text="8", padx=40, pady=40, command= lambda: click(8))
button_9 = Button(root, text="9", padx=40, pady=40, command= lambda: click(9))
button_4 = Button(root, text="4", padx=40, pady=40, command= lambda: click(4))
button_5 = Button(root, text="5", padx=40, pady=40, command= lambda: click(5))
button_6 = Button(root, text="6", padx=40, pady=40, command= lambda: click(6))
button_1 = Button(root, text="1", padx=40, pady=40, command= lambda: click(1))
button_2 = Button(root, text="2", padx=40, pady=40, command= lambda: click(2))
button_3 = Button(root, text="3", padx=40, pady=40, command= lambda: click(3))
button_0 = Button(root, text="0", padx=40, pady=40,command= lambda: click(0))

#Ubicamos e imprimimos los botones en la pantalla
button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
button_0.grid(row=5, column=1)


#Agregamos los botones adicionales para las funciones básicas de una calculadora 

button_add = Button(root, text="+", padx=40, pady=40, fg="White",bg="orange", command= lambda: suma())
button_clear = Button(root, text="C", padx=40, pady=40,fg="White",bg="orange", command= lambda: clear())
button_reste = Button(root, text="-", padx=40, pady=40, fg="White",bg="orange", command= lambda: resta())
button_multi = Button(root, text="X", padx=40, pady=40, fg="White",bg="orange", command= lambda: multi())
button_divi = Button(root, text="/", padx=40, pady=40, fg="White",bg="orange", command= lambda: divi())
button_float = Button(root, text=".", padx=40, pady=40)
button_square = Button(root, text="*", padx=40, pady=40,fg="White",bg="orange", command=lambda: square())
button_root = Button(root, text="√", padx=40, pady=40,fg="White",bg="orange", command=lambda: roott())
button_equal = Button(root, text="=", padx=80, pady=40,fg="White",bg="orange", command=lambda: equal())


button_add.grid(row=3, column=3)
button_clear.grid(row=1, column=0)
button_reste.grid(row=2, column=3)
button_multi.grid(row=1, column=3)
button_float.grid(row=5, column=0)
button_equal.grid(row=5, column=2, columnspan=3)
button_divi.grid(row=4, column=3)
button_square.grid(row=1, column=2)
button_root.grid(row=1, column=1)

#Cerramos la ventana creada y termnina el algoritmo
root.mainloop()