#Escribí un programa que le solicite al usuario ingresar una fecha formada por 8 números, 
# donde los primeros dos representan el día, los siguientes dos el mes y los últimos cuatro el año (DDMMAAAA).
#  Este dato debe guardarse en una variable con tipo int (número entero).
#  Finalmente, mostrar al usuario la fecha con el formato DD / MM / AAAA. 
dat = str (input ("Ingrese nacimiento en formato DD/MM/AAAA: "))
print (dat[0,1], "/",dat[2,3], "/",dat[4,7]  )