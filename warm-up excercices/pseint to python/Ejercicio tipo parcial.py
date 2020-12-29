global total
total = 0 

def intr (): 
    global product
    product = str (input ("Ingrese su producto (C/M/T): "))
    product.capitalize()
    if product == "C":
        x= 50
    elif product == "M":
        x=30
    elif product == "T":
        x=80
    else: 
        print ("Error, Ingresa C, M o T")
    global unity     
    unity = int(input ("Ingrese la unidad: "))
    global totalx
    totalx = total + x*unity

while int(product) != "*" and unity != 0: 
    print (intr())

print ("El precio total es: ", totalx, "$")