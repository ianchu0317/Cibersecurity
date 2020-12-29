#Escribí un programa que solicite al usuario el ingreso de un texto y almacene ese texto en una variable.
#  A continuación, mostrar en pantalla la primera letra del texto ingresado. 
# Luego, solicitar al usuario que ingrese un número positivo menor a la cantidad de caracteres que tiene el texto que ingresó 
# (por ejemplo, si escribió la palabra “HOLA”, tendrá que ser un número entre 0 y 4) y almacenar este número en una variable llamada indice.
#Mostrar en pantalla el carácter del texto ubicado en la posición dada por indice. 

import time 

text = str (input ("Ingresa una palabra: "))
print ("La primera letra de la palabra es: ", text[0])
time.sleep(5)
pos = int (input ("Ingresa la posición que quuiera buscar: "))
if pos < (len(text))+1: 
    print ("La letra buscada es: ",  text[pos+1])
elif pos > (len(text))+1: 
    print ("La letra buscada no existe")

    