#Escribí un programa que solicite al usuario dos números y los almacene en dos variables. 
#En otra variable, almacená el resultado de la suma de esos dos números y luego mostrá ese resultado en pantalla.
#A continuación, el programa debe solicitar al usuario que ingrese un tercer número, el cual se debe almacenar en una nueva variable. Por último, mostrá en pantalla el resultado de la multiplicación de este nuevo número por el resultado de la suma anterior. 
import time
n1 = int (input ("Ingresa su primer número: "))
n2 = int (input ( "Ingresa su segundo número: "))
print ( n1, " + ", n2, " = ", n1+n2)
time.sleep(5)
n3 = int (input ( "Ingresa su tercer número: "))
print ("(", n1, " + ", n2, ") / ", n3, " = ", (n1+n2)/n3)
