#Escribí un programa que solicite al usuario un número y le reste el 15%,
#  almacenando todo en una única variable. A continuación, mostrar el resultado final en pantalla. 
n = int (input("Ingrese un número: "))
porc = n - n*15/100
print (n, "- 15% = ", porc)