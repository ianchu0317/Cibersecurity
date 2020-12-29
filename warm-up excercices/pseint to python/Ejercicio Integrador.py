#Predefinimos nuestras variables a usar
global productos
productos = {}
global price 
price = 0
global total
total = 0

#Añadimos una funcion que nos guarda los datos 
def entrada ():
    product = str(input("Ingrese el nombre de producto: "))
    global cantidad
    cantidad = int(input("Ingrese la cantidad: "))
    global precio
    precio = int(input("Ingrese el precio: "))
    price = int (cantidad*precio)
    print (price)
    pricex = (str(price)+ "$")
    productos[product]=pricex

#Ingresa 6 productos
for x in range(1,2+1):
    print (entrada())
    total = total + cantidad*precio


#Le mostramos lo seleccionado y dejamos elegir su medio de pago
print ("")
print ("Estos son los productos y sus respectivos precios: ", productos)
print ("El precio total es: ", total, "$")
print ("")
print ("")
print ("1) Efectivo, 10% " + "de Descuento")
print ("2) Débito, 5% " + "de Descuento")
print ("3) Tarjeta")
medio = int(input("Introduzca un medio de pago (1, 2, 3; 3 por defecto): "))

#Le ofrecemos su pago final
if medio == 1: 
    print ("Su total a pagar es: ",total-total*10/100 )
if medio == 2: 
    print ("Su total a pagar es: ",total-total*5/100 )
else: 
    print ("Su total a pagar es: ",total)
