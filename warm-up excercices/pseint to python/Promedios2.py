mapr=0
ingresados=0
mepr=7
may=0
prom1=0
prom2=0
prom3=0
promedio=0

for i in range(1,2+1):
    name=input("Introduce su nombre: ")
    age = int(input("Introduce su edad: "))
    if age > 18: 
        may=may+1
    prom1=int(input("Introduce la nota del primer trimestre: "))
    prom2=int(input("Introduce la nota del segundo trimestre: "))
    prom3=int(input("Introduce la nota del tercer trimestre: "))
    promedio = (prom1+prom2+prom3)/3
    if promedio > mapr:
        mapr=int((prom1+prom2+prom3)/3)
    elif promedio < mepr:
        mepr=mepr+1
    ingresados=ingresados+1

print ("El mayor promedio fue: ", int(mapr))
print ("El ", may/ingresados*100, "% ", "es mayor de edad")
print ( mepr," alumnos tuvieron promedios menores de 7")