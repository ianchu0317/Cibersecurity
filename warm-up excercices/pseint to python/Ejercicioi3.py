import random  
azar= int(random.randint(1,10))
adivinanza=int(input("Introduzca su número: "))
while adivinanza != azar:
    if int(adivinanza) < int(azar): 
        print("El número es mayor !")
    else: 
        print("El número es menor")      
    adivinanza=int(input("Introduzca su número: "))

print("Enhorabuena !!!")
print("El número correcto es: ", azar)