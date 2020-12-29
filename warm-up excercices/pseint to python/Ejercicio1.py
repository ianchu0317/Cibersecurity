#Se necesita un programa que pida el nombre y la edad de una persona, 
#si ésta es menor a 46 expresar "Sos muy joven, sino "Estás creciendo""

nombre= input("Ingresa su nombre aquí: ")
edad= int(input("Ingrese su edad aquí: "))
if edad<46: 
    print ("Sos muy joven")
else: 
    print ("Estás creciendo")
    