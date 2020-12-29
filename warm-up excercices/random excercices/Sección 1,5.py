#Escribí un programa que solicite al usuario el ingreso de una temperatura en escala Fahrenheit (debe permitir decimales) 
# #y le muestre el equivalente en grados Celsius. La fórmula de conversión que se usa para este cálculo es:
# # _Celsius = (5/9) * (Fahrenheit-32)_
import time
f = float (input ("Introduce su temperatura en Fahrenheit: "))
print ("Celsius: ",(5/9) * (f-32) )
time.sleep(5)