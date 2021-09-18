mensaje="""

Jueguemos adivinar el número, generaremos un número
entre 1 y 10. Nuestro objetivo es adivinar el
número. Si fallamos, nos dirán si es mayor o menor que el 
número buscado

"""
print(mensaje)

import random

NA= random.randint(1, 10)
NmD= int((input("Adivine el número: ")))

if NmD == NA:
	print("Adivinaste")
else:
	if NmD > NA:
	    print("El número que digitaste es mayor al buscado")
	else:
	    print("El número que digitaste es menor al buscado")

print(f"El número generado fue {NA}")

#Ejercicio 2

"""
Definir un algoritmo en python que evalue si una palabra o frase es palindorma, es decir, palabras 
que tienen el mismo aspecto escritas invertidas. Ejemplo: "Radar" tendría que devolver TRUE
"""

palabra=input("Ingrese una palabra: ").lower() #El ".lower()" sirve para convertir toda la palabra o frase en minuscula
palabra= palabra.replace(" ", "") #".replace" sirve para reemplazar ciertas cosas.
#".replace" en este caso me está reemplazando los espacios por ningún espacio
invertida=palabra[::-1] #Con el último comando le estoy indicando que me lea las palabras de derecha a izquierda

if palabra == invertida:
	print("La palabra sí es un palindromo")

else:	
	print("La palabra no es un palindromo")

#Ejercicio 3

"""Las personas adscritas a la jubilación por
antiguedad adulta deben tener 60 años o más
y una antiguedad en su empleo de 25 años o más.
Determinar en qué tipo de jubilación, quedará
adscrita una persona."""

edad= int(input("Ingrese su edad: "))
empleo= int(input("¿Cuántos años de antiguedad tiene su empresa? "))

if edad>=60 and empleo< 25:
	print("Usted quedará inscrito en la jubilación por edad")
elif edad <60 and empleo>=25:
	print("Usted quedará inscrito a la jubilación por antiguedad joven")
elif edad>=60 and empleo>=25:
	print("Usted quedaráinscrito a la jubilación por antiguedad adulta")
else:
	print("Usted aún no se jubila")