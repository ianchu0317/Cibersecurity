#Generar la tanla de multiplicar de un número natural N, desde N*1 hasta N*10
tabla = int(input("Ingrese su número a multiplicar: "))
for i in range(1,11,1):
    print (tabla,"x", i, " = ", tabla*i)
